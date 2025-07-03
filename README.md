# 🛠️ utilsuite

 Utility functions are designed to streamline your workflow, so you can focus on what matters.

<h3 align="center"> <em>🚀✨ Cut through boilerplate. Save time. Stay focused.</em> ⚡️🔥</h3>

## 🧱 Usage
The package is set up so that it only imports needed libraries when an object is created. Simply pip install the needed package as you go. 
```
git clone git@github.com:zzangupenn/utilitySuite.git
cd utilitySuite
pip install -e .
```
For example:

`import utilsuite` will only import a catalog; no functions/classes are imported.

`config = utilsuite.ConfigYAML()` First time using the functions/classes triggers the import.

See [`examples.ipynb`](https://github.com/zzangupenn/utilitySuite/blob/main/examples.ipynb) for usages.

## ⚙️ Available Tools
| Name             | Description |
|------------------|-------------|
| [`utilsuite`](https://github.com/zzangupenn/utilitySuite/blob/main/utilsuite/__init__.py)   | Root package entry — supports lazy loading so only the tools you import get loaded. Clean, efficient, and namespace-friendly. Can also be imported as an [***Suite***](https://github.com/zzangupenn/utilitySuite/blob/main/utilsuite/utilitysuite.py) |
| [`ConfigYAML`](https://github.com/zzangupenn/utilitySuite/blob/main/utilsuite/configyaml.py)      | Simplifies reading and writing YAML configuration files. Offers intuitive dot-access, saves and loads directly to YAML files, and supports nested structures, making experiment setup and configuration management clean and scriptable. |
| [`ListDict`](https://github.com/zzangupenn/utilitySuite/blob/main/utilsuite/listdict.py)      | A hybrid structure combining list ordering, dictionary style initialization, and dataclass access. Useful for recording data with many categories. Support simple save/load. |
| [`QtMatplotlib`](https://github.com/zzangupenn/utilitySuite/blob/main/utilsuite/qtmatplotlib.py)      | A high-level interface mimicking `matplotlib.pyplot`, but with real-time, fast, and multiprocess-capable rendering using PyQtGraph. Currently implemented `plot`, `scatter`. Can be used with `live=True` to continuously stream plots in a separate process. |
| [`keyMonitor`](https://github.com/zzangupenn/utilitySuite/blob/main/utilsuite/keymonitor.py)     | Captures keypress events in real time without blocking the program flow. Ideal for interactive command-line tools or live-control systems. |
| [`coloredText`](https://github.com/zzangupenn/utilitySuite/blob/main/utilsuite/coloredtext.py)    | Adds styled ANSI colors to terminal output. Great for improving readability in logs, CLI feedback, or debugging messages. |
| [`Logger`](https://github.com/zzangupenn/utilitySuite/blob/main/utilsuite/logger.py)         | A minimal, file-saving logger with optional color output and timestamping. Let you track events or experiment states without setting up complex logging frameworks. |
| [`Timer`](https://github.com/zzangupenn/utilitySuite/blob/main/utilsuite/timer.py)          | Simple stopwatch and context-based timing. Perfect for profiling function runtimes, monitoring loop durations, or annotating performance bottlenecks. |
| [`DataProcessor`](https://github.com/zzangupenn/utilitySuite/blob/main/utilsuite/dataprocessor.py)  | Contains helpers for filtering, structuring, and transforming datasets. Useful for preprocessing logs, lists, or config-driven data. |
| [`colorPalette`](https://github.com/zzangupenn/utilitySuite/blob/main/utilsuite/colorpalette.py)   | A curated set of visually balanced color themes for plots and visual output. Enables consistent aesthetics across matplotlib or CLI tools. |
| [`pltUtils`](https://github.com/zzangupenn/utilitySuite/blob/main/utilsuite/pltutils.py)       | Quick-plot functions built on matplotlib — for fast rendering of line plots, histograms, and comparisons with minimal code. Great for debugging or visually summarizing data. |

