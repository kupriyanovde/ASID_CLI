

from typing import List
import os
from cmd import Cmd

from .ASID import Core

class App(Cmd):
    def __init__(self):  
        super().__init__()   

        self._path = 'main' 
        # self._menu = Menu('main', Main(self))
        # self._menu.addSubMenu('config', Config(self))
 
       
        
    def onecmd(self, line):
        cmd, arg, line = super().parseline(line) 
        if not line:
            return bool(self._menu.node(self._path).call('emptyline',line))
        if cmd is None:
            return bool(self._menu.node(self._path).call('default',line))
        self.lastcmd = line
        if line == 'EOF' :
            self.lastcmd = ''
        if cmd == '':
            return bool(self._menu.node(self._path).call('default',line))
        else:          
            try:              
                self._path = self._menu.node(self._path).call('do_' + cmd, arg) 
                pass
            except AttributeError:
                return bool(self._menu.node(self._path).call('default',line))
            return self._path == ""
         

class Application:
    def __init__(self, app_path : str, argv):
        self._app_path = app_path

        plugin_dir = os.path.join(app_path,'plugins')
        core = Core(plugin_dir)
        
    def run(self):
        app = App()
        try:
            app.cmdloop()
        except KeyboardInterrupt:
            print ("завершение сеанса...")
        return 0