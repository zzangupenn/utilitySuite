# import sys
# import numpy as np
# import time
# from PyQt6 import QtWidgets
# import pyqtgraph as pg

# class LockingPlot(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Expand Until 2π, Then Lock Axis Limits")

#         self.graph_widget = pg.GraphicsLayoutWidget()
#         self.setCentralWidget(self.graph_widget)

#         self.plot = self.graph_widget.addPlot()
#         self.plot.enableAutoRange('xy', True)  # Start with auto-range
#         self.plot.setAspectLocked(True)
#         self.curve = self.plot.plot(pen='w')  # White line for the sine wave

#         self.locked = False  # Track whether limits have been set

#     def animate(self, max_points=1000, delay_sec=0.01):
#         x_vals = []
#         for i in range(max_points):
#             x = i * 0.02
#             x_vals.append(x)
#             y_vals = np.sin(x_vals)

            
#             # Lock axis range once x reaches 2π
#             if x >= 2 * np.pi:
#                 self.plot.enableAutoRange(x=False, y=False)
#                 self.plot.setXRange(0, 2 * np.pi)
#                 self.plot.setYRange(-1.5, 1.5)
#                 # self.locked = True
#             # elif not self.locked:
#             #     self.plot.setXRange(0, x)
#             self.curve.setData(x_vals, y_vals)


#             QtWidgets.QApplication.processEvents()
#             time.sleep(delay_sec)

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = LockingPlot()
#     window.resize(800, 500)
#     window.show()

#     QtWidgets.QApplication.processEvents()
#     window.animate()

#     sys.exit(app.exec())


# This is a Qt-based plotter that behave like matplotlib
import utilsuite
import numpy as np
import time

## scatter and plot are implemented in utilsuite.qtPlt
if __name__ == "__main__":
    qt_plotter = utilsuite.QtMatplotlib(win_title="Sine Wave Animation")
    waypoints = np.stack([np.arange(10), np.arange(10), np.arange(10)]).T
    # qt_plotter.scatter(waypoints[:, 0], waypoints[:, 1], c=waypoints[:, 2], s=10, live=True, plot_num=0)
    # qt_plotter.plot(np.linspace(0, 10, 100), np.cos(np.linspace(0, 10, 100)), color='r', linewidth=4, live=True)

    ## Example of animating a sine wave using utilsuite.qtPlt
    qt_plotter = utilsuite.QtMatplotlib(win_title="Sine Wave Animation")
    fps = 144  # frames per second
    x = np.linspace(0, 2 * np.pi, 500)
    amplitude = np.sin(x)
    plot_num = 0 # reuse the same plot
    for i in range(5 * fps):  # animate 5 seconds
        phase_shift = i * 5 / fps
        y = np.sin(x + phase_shift)
        qt_plotter.plot(np.arange(len(y)), y, color='blue', linewidth=3, live=True, plot_num=plot_num)
        qt_plotter.ylim(-2, 2)
        qt_plotter.xlabel("X-axis")
        qt_plotter.ylabel("Y-axis")
        qt_plotter.xlim(0, len(y))
        
        time.sleep(1 / fps)  # control frame rate