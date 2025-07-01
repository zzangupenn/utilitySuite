import os
class keyMonitor:
    """
    Keyboard event monitor that updates environment variables based on key presses.

    Features:
    - Toggles or sets a custom environment variable `KEY_OPTION_ZZR` when right Alt or digit keys (0-9) are pressed.
    - Sets a one-time flag in `KEY_OPTION_ONCE_ZZR` when Up or Down arrow keys are pressed.
    - Runs a background keyboard listener using `pynput`.

    Environment Variables Used:
    ---------------------------
    KEY_OPTION_ZZR : str
        Stores the current option state toggled by right Alt key or set by digit keys.
    KEY_OPTION_ONCE_ZZR : str
        Stores a temporary one-time flag set by Up ('1') or Down ('2') arrow keys.

    Methods:
    --------
    option():
        Returns the current value of `KEY_OPTION_ZZR`.

    option_once():
        Returns the current value of `KEY_OPTION_ONCE_ZZR` and resets it to '0'.
    """
    def __init__(self, enable=True) -> None:
        os.environ['KEY_OPTION_ZZR'] = '0'
        os.environ['KEY_OPTION_ONCE_ZZR'] = '0'
        if enable:
            import pynput.keyboard as keyboard
            self.keyboard = keyboard
            
            def show(key):
                if "{0}".format(key) == "Key.alt_r":
                    if os.environ['KEY_OPTION_ZZR'] == '0':
                        os.environ['KEY_OPTION_ZZR'] = '1'
                    else:
                        os.environ['KEY_OPTION_ZZR'] = '0'
                    print('[keyMonitor]:' + os.environ['KEY_OPTION_ZZR'])
                elif "{0}".format(key) in list(map(lambda x: "'"+str(x)+"'", range(10))):
                    os.environ['KEY_OPTION_ZZR'] = "{0}".format(key)[1]
                    print('[keyMonitor]:' + os.environ['KEY_OPTION_ZZR'])
                elif "{0}".format(key) == "Key.up":
                    os.environ['KEY_OPTION_ONCE_ZZR'] = '1'
                elif "{0}".format(key) == "Key.down":
                    os.environ['KEY_OPTION_ONCE_ZZR'] = '2'
                        
            listener = keyboard.Listener(on_press = show)    
            listener.start()
        
    def option(self):
        return os.environ['KEY_OPTION_ZZR']
    
    def option_once(self):
        option = os.environ['KEY_OPTION_ONCE_ZZR']
        os.environ['KEY_OPTION_ONCE_ZZR'] = '0'
        return option