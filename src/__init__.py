

from typing import List
import os

from .ASID import Core

class Application:
    def __init__(self, app_path : str):
        self._app_path = app_path

        plugin_dir = os.path.join(app_path,'plugins')
        core = Core(plugin_dir)
        
    def run(self, argv):
        app = App()
        try:
            app.cmdloop()
        except KeyboardInterrupt:
            print ("завершение сеанса...")