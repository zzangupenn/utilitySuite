
import os
class utilitySuite:
    def __init__(self):
        pass
    
    def __new__(self, config=None, create_logger_file=False, config_path=None):
        from utilitySuite import ConfigYAML, Logger, Timer, DataProcessor, colorPalette, pltUtils, keyMonitor, ListDict
        if config is None:
            if config_path is None:
                self.config = ConfigYAML()
                self.config.kmonitor_enable = 0
            else:
                self.config = ConfigYAML()
                self.config.load_file(config_path)
                if 'kmonitor_enable' not in vars(self.config):
                    self.config.kmonitor_enable = 0
            self.log = Logger('./', '', create_file=create_logger_file)
        else:
            self.config = config
            self.log = Logger(config.save_dir, config.exp_name, 
                              create_file=create_logger_file)
        self.timer = Timer()
        self.dp = DataProcessor()
        self.colorpal = colorPalette()
        self.plt = pltUtils()
        self.kmonitor = keyMonitor(enable=self.config.kmonitor_enable)
        self.rec = ListDict()
        self.logline = self.log.line
        
        return self, self.logline

    
    def mkdir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)