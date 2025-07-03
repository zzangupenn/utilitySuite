import os
import ast

excluded_names = {
    'QtPlotterProcess'
}

def extract_top_level_defs(filepath):
    """Extract top-level function and class names from a Python file."""
    with open(filepath, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    names = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name not in excluded_names:
            names.append(node.name)
    return names

def generate_init(package_dir="."):
    modules = []
    lazy_functions = {}

    exclude_files = {"__init__.py", "generate_init.py"}

    for filename in sorted(os.listdir(package_dir)):
        if not filename.endswith(".py") or filename in exclude_files:
            continue
        modname = filename[:-3]
        modules.append(modname)
        filepath = os.path.join(package_dir, filename)
        try:
            names = extract_top_level_defs(filepath)
            for name in names:
                lazy_functions[name] = (modname, name)
        except Exception as e:
            print(f"⚠️ Failed to parse {filename}: {e}")

    # Build lazy_functions dict string
    lazy_lines = ["_lazy_functions = {"]
    for name, (mod, cls) in sorted(lazy_functions.items()):
        lazy_lines.append(f'    "{name}": ("{mod}", "{cls}"),')
    lazy_lines.append("}\n")

    # Build TYPE_CHECKING import lines
    type_checking_lines = [
        "from typing import TYPE_CHECKING",
        "if TYPE_CHECKING:",
    ]
    for mod in modules:
        type_checking_lines.append(f"    from .{mod} import *")
    type_checking_lines.append("")

    # Build __getattr__ method lines
    getattr_lines = [
        "import importlib",
        "from typing import Any",
        "",
        "def __getattr__(name: str) -> Any:",
        "    if name in _lazy_functions:",
        "        module_name, class_name = _lazy_functions[name]",
        "        module = importlib.import_module(f\".{module_name}\", __name__)",
        "        cls = getattr(module, class_name)",
        "        globals()[name] = cls  # Cache to avoid repeated getattr calls",
        "        return cls",
        "    raise AttributeError(f\"module {__name__} has no attribute {name}\")",
    ]

    lines = []
    lines.extend(lazy_lines)
    lines.extend(type_checking_lines)
    lines.extend(getattr_lines)

    return "\n".join(lines)

if __name__ == "__main__":
    content = generate_init(".")
    with open("__init__.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated __init__.py successfully.")
