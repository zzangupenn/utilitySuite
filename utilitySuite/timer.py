import numpy as np
class Timer:
    """
    A flexible timer utility for measuring elapsed time or frequency (Hz) of code sections.

    Features:
    - Supports named timers to track multiple independent time measurements.
    - Can measure single or multiple timings before computing averages.
    - Allows printing elapsed time or frequency with customizable labels and colors.
    - Integrates with a colored text printer for visually distinct outputs.
    - Supports automatic start-stop measurement sequences via `toctic`.

    Methods:
    --------
    tic(time_name=None, num=1):
        Starts or records a timestamp for the given timer name.

    toc(print_name='', time_name=None, Hz=False, show=True):
        Stops the timer and returns elapsed time or frequency.
        Optionally prints the result with color highlighting.

    toctic(print_name='', time_name=None, Hz=False, show=True, time_name2=None):
        Convenience method that calls `toc` followed by `tic` for chaining measurements.

    ding():
        Prints a blank line when enabled (placeholder for alert sounds or signals).
        
    Attributes:
    -----------
    enable : bool
        Enables or disables timing functionality.
    times : dict
        Stores lists of recorded times for each named timer.
    nums : dict
        Number of samples to collect before averaging for each timer.
    ct : coloredText
        Instance of a colored text printer used for output.
    """
    def __init__(self, enable=True) -> None:
        self.enable = enable
        self.times = {}
        self.nums = {}
        import time
        self.time = time
        from utilitySuite import coloredText
        self.ct = coloredText()
        
    def tic(self, time_name=None, num=1):
        if self.enable:
            if time_name is None:
                time_name = str(len(list(self.times.keys())))
                self.times[time_name] = self.time.time()
            else:
                if time_name in self.times:
                    self.times[time_name].append(self.time.time())
                else:
                    self.times[time_name] = [self.time.time()]
                    self.nums[time_name] = num

    def toc(self, print_name='', time_name=None, Hz=False, show=True):
        if self.enable:
            if time_name is None:
                time_name = str(len(list(self.times.keys())) - 1)
                if Hz: 
                    ret = 1/(self.time.time() - self.times[time_name])
                else:
                    ret = self.time.time() - self.times[time_name]
                if Hz and show: self.ct.print(f"{print_name} {ret} Hz", 'o')
                elif show: self.ct.print(f"{print_name} {ret} s", 'o')
                return ret
            else:
                if time_name in self.times:
                    if len(self.times[time_name]) < self.nums[time_name]:
                        self.times[time_name][-1] = self.time.time() - self.times[time_name][-1]
                        return None
                    else:
                        self.times[time_name][-1] = self.time.time() - self.times[time_name][-1]
                        ret = np.mean(self.times[time_name])
                        self.times[time_name] = []
                        if Hz: 
                            ret = 1 / ret
                        if Hz and show: self.ct.print(f"{print_name} {ret} Hz", 'o')
                        elif show: self.ct.print(f"{print_name} {ret} s", 'o')
                        return ret
                else:
                    self.ct.print('Timer Error: No such time name', time_name, 'r')

    def toctic(self, print_name='', time_name=None, Hz=False, show=True, time_name2=None):
        ret = self.toc(print_name, time_name, Hz, show)
        self.tic(time_name2)
        return ret
    
    def ding(self):
        if self.enable:
            print()