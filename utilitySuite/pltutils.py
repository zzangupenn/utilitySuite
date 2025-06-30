import numpy as np
class pltUtils:
    """
    Utility class for simplifying common matplotlib plotting tasks.

    Features:
    - Create figures with customizable grid layouts.
    - Access individual axes easily for further customization.
    - Support for grid lines, axis equalization, background color, and box aspect ratio.
    - Convenience methods for hiding axes, adding colorbars, setting axis limits.
    - Handles window close events to support interactive plotting with pauses.
    - Methods to show, pause with event handling, save figures, and close all figures.

    Attributes:
    -----------
    plt : module
        Imported matplotlib.pyplot module.
    GridSpec : class
        matplotlib.gridspec.GridSpec for flexible subplot grid layout.
    fig : matplotlib.figure.Figure
        The current figure.
    gs : matplotlib.gridspec.GridSpec
        The grid specification of the current figure.
    axs : list of matplotlib.axes.Axes
        List of subplot axes.
    win_closed : bool
        Flag set when the figure window is closed, used to break pause loops.

    Methods:
    --------
    get_fig(grid=[1, 1], figsize=[8, 6], dpi=100, gridline=False):
        Creates a figure with a grid of subplots and returns the list of axes.

    equal(ax_num):
        Sets equal scaling on the specified axis.

    background(color, ax_num):
        Sets the background color of the specified axis.

    box(ax_num):
        Sets aspect ratio to 'equal' and adjusts box aspect for the specified axis.

    grid(ax_num):
        Enables grid lines on the specified axis.

    hide_xy(ax_num):
        Hides the x and y axis ticks and labels on the specified axis.

    colorbar(ax_num, cmap='viridis', data_ind=0, location='right', label=''):
        Adds a colorbar to the specified axis based on its collections or images.

    y(ax_num, limit):
        Sets y-axis limits for the specified axis.

    x(ax_num, limit):
        Sets x-axis limits for the specified axis.

    show():
        Displays all open figures.

    show_pause():
        Updates the figure and waits for user input, closing the figure if the window is closed.

    save_fig(filename):
        Saves the current figure to a file.

    close_all():
        Closes all matplotlib figures.

    Example:
    --------
    pu = pltUtils()
    axs = pu.get_fig(grid=[2,2], gridline=True)
    pu.background('lightgrey', 0)
    pu.show_pause()
    """
    def __init__(self) -> None:
        import matplotlib.pyplot as plt
        from matplotlib.gridspec import GridSpec
        self.plt = plt
        self.GridSpec = GridSpec
        self.win_closed = False
        
    def get_fig(self, grid=[1, 1], figsize=[8, 6], dpi=100, gridline=False):
        fig = self.plt.figure(figsize=figsize, dpi=dpi)
        self.fig = fig
        self.fig.tight_layout()
        self.gs = self.GridSpec(grid[0], grid[1])
        self.axs = []
        for ind in range(np.prod(grid)):
            self.axs.append(fig.add_subplot(self.gs[ind]))
        if gridline:
            for ind in range(len(self.axs)):
                self.grid(ind)
            
        def handle_close(evt):
            self.win_closed = True
        self.fig.canvas.mpl_connect('close_event', handle_close)
        return self.axs
    
    def equal(self, ax_num):
        self.axs[ax_num].axis('equal')
        
    def background(self, color, ax_num):
        self.axs[ax_num].set_facecolor(color)
    
    def box(self, ax_num):
        self.axs[ax_num].set_aspect('equal', 'box')
    
    def grid(self, ax_num):
        self.axs[ax_num].grid(which='both', axis='both')
    
    def hide_xy(self, ax_num):
        self.axs[ax_num].get_xaxis().set_visible(False)
        self.axs[ax_num].get_yaxis().set_visible(False)

    def colorbar(self, ax_num, cmap='viridis', data_ind=0, location='right', label=''):
        if len(self.axs[ax_num].collections) > 0:
            cbar = self.plt.colorbar(self.axs[ax_num].collections[data_ind], 
                                     ax=self.axs[ax_num], cmap=cmap, 
                                     location=location, label=label)
        elif len(self.axs[ax_num].images) > 0:
            cbar = self.plt.colorbar(self.axs[ax_num].images[data_ind], 
                                     ax=self.axs[ax_num], cmap=cmap, 
                                     location=location, label=label)
        
            
    def y(self, ax_num, limit):
        self.axs[ax_num].set_ylim(limit)
    
    def x(self, ax_num, limit):
        self.axs[ax_num].set_xlim(limit)
        
    def show(self):
        self.plt.show()
    
    def show_pause(self):
        self.plt.draw()
        while self.plt.waitforbuttonpress(0.2) is None:
            if self.win_closed:
                break
        self.plt.close(self.fig)
        self.win_closed = False
    
    def save_fig(self, filename):
        self.plt.savefig(filename, bbox_inches='tight')
        
    def close_all(self):
        self.plt.close('all')