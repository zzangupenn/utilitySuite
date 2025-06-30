# 🛠️ utilitySuite

 Utility functions designed to streamline your workflow — so you can focus on what matters.

<h3 align="center"> <em>🚀✨ Cut through boilerplate. Save time. Stay focused.</em> ⚡️🔥</h3>

## 🧱 Usage
The package is set up so that it only imports libraries needed when you create an object. So just pip install the needed package as you go.
```
import utilitySuite as utilsuite # Here only imports a catelog, no functions/classes are imported.
config = utilsuite.ConfigYAML() # First time using of the functions/classes triggers the import.
```

## ⚙️ Available Tools
| Name             | Description |
|------------------|-------------|
| [`utilitySuite`](https://github.com/zzangupenn/utilitySuite/blob/main/utilitySuite/__init__.py)   | Root package entry — supports lazy loading so only the tools you import get loaded. Clean, efficient, and namespace-friendly. Can also be imported as an [***Suite***](https://github.com/zzangupenn/utilitySuite/blob/main/utilitySuite/utilitysuite.py) |
| [`ConfigYAML`](https://github.com/zzangupenn/utilitySuite/blob/main/utilitySuite/configyaml.py)      | Simplifies reading and writing YAML configuration files. Offers intuitive dot-access, saves and loads directly to YAML files, and supports nested structures, making experiment setup and configuration management clean and scriptable. |
| [`ListDict`](https://github.com/zzangupenn/utilitySuite/blob/main/utilitySuite/listdict.py)      | A hybrid structure combining list ordering, dictionary style initialization, and dataclass access. Useful recording data with many categories. Support simple save/load. |
| [`keyMonitor`](https://github.com/zzangupenn/utilitySuite/blob/main/utilitySuite/keymonitor.py)     | Captures keypress events in real time without blocking the program flow. Ideal for interactive command-line tools or live-control systems. |
| [`coloredText`](https://github.com/zzangupenn/utilitySuite/blob/main/utilitySuite/coloredtext.py)    | Adds styled ANSI colors to terminal output. Great for improving readability in logs, CLI feedback, or debugging messages. |
| [`Logger`](https://github.com/zzangupenn/utilitySuite/blob/main/utilitySuite/logger.py)         | A minimal, file-saving logger with optional color output and timestamping. Let you track events or experiment states without setting up complex logging frameworks. |
| [`Timer`](https://github.com/zzangupenn/utilitySuite/blob/main/utilitySuite/timer.py)          | Simple stopwatch and context-based timing. Perfect for profiling function runtimes, monitoring loop durations, or annotating performance bottlenecks. |
| [`DataProcessor`](https://github.com/zzangupenn/utilitySuite/blob/main/utilitySuite/dataprocessor.py)  | Contains helpers for filtering, structuring, and transforming datasets. Useful for preprocessing logs, lists, or config-driven data. |
| [`colorPalette`](https://github.com/zzangupenn/utilitySuite/blob/main/utilitySuite/colorpalette.py)   | A curated set of visually balanced color themes for plots and visual output. Enables consistent aesthetics across matplotlib or CLI tools. |
| [`pltUtils`](https://github.com/zzangupenn/utilitySuite/blob/main/utilitySuite/pltutils.py)       | Quick-plot functions built on matplotlib — for fast rendering of line plots, histograms, and comparisons with minimal code. Great for debugging or visually summarizing data. |

