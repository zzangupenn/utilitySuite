import os
class Logger:
    """
    Simple logger class for recording experiment outputs and saving files.

    This logger captures printed lines to an in-memory buffer and appends them
    to a timestamped text file inside a specified directory. It can also save
    the content of a source file (e.g., a Python script) to the experiment folder.

    Attributes:
    -----------
    save_dir : str
        Directory where log files and saved scripts are stored.
    experiment_name : str
        Name of the experiment used to name log and script files.
    s : io.StringIO
        In-memory buffer used to accumulate lines before writing to file.

    Methods:
    --------
    create_file(experiment_name):
        Creates or appends a log file with a header including experiment name and timestamp.

    write_file(file):
        Copies the content of a given source file into a `.py` file in the save directory.

    line(*line, print_line=True):
        Prints and logs the provided line(s). Automatically appends to the log file.
    """
    def __init__(self, save_dir, experiment_name, create_file=True) -> None:
        from io import StringIO
        self.s = StringIO()
        self.save_dir = save_dir
        self.experiment_name = experiment_name
        if create_file:
            self.create_file(experiment_name)
    
    def create_file(self, experiment_name):
        import datetime
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        with open(self.save_dir + experiment_name + '.txt', "a") as tgt:
            tgt.writelines('\n' + '-' * 80 + '\n')
            tgt.writelines(experiment_name + ' ' + str(datetime.datetime.now()) + '\n')
        print(experiment_name + ' ' + str(datetime.datetime.now()))
            
    def write_file(self, file):
        with open(file, "r") as src:
            with open(self.save_dir + self.experiment_name + '.py', "w") as tgt:
                tgt.write(src.read())
    
    def line(self, *line, print_line=True):
        if print_line: print(*line)
        print(*line, file = self.s)
        with open(self.save_dir + self.experiment_name + '.txt', "a") as tgt:
            tgt.writelines(self.s.getvalue())
        self.s.truncate(0)
        self.s.seek(0)