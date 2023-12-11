class Shortcut:

    def __init__(self, linuxCommand, windowsCommand, linuxCallback=None, windowsCallback=None) -> None:
        self.linuxCommand = 'nohup ' + linuxCommand
        self.windowsCommand = windowsCommand
        self.linuxCallback = linuxCallback
        self.windowsCallback = windowsCallback
    
    def execute(self):
        import sys
        import subprocess
        
        if sys.platform.startswith('linux'):
            if self.linuxCallback:
                self.linuxCallback()
            subprocess.Popen(self.linuxCommand.split(' '))
        elif sys.platform.startswith('win32'):
            if self.windowsCallback:
                self.windowsCallback()
            subprocess.Popen(self.windowsCommand.split(' '))
        else:
            print(f"Unsupported OS: {sys.platform}")