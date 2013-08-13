import sublime, sublime_plugin, json
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import win32api #, win32con
# 0x4B = k key; 0xa4 = left alt key; 0xa5 = right alt key; 0x12 = either alt key

class chordFlowCommand(sublime_plugin.WindowCommand):
    def run(self, commands):
        dic=json.loads(json.dumps(commands)) # command1: no modifier, command2: k key modifier, command3: dual alt key modifier, command4: k key modifier + dual alt key modifier
        dualAltModifier=win32api.GetAsyncKeyState(0xa4)<0 and win32api.GetAsyncKeyState(0xa5)<0

        #if keystate==0 or keystate==1:
        if win32api.GetAsyncKeyState(0x4B)<0:  # k key is down
            if dualAltModifier: #4
                if 'command4' in dic:
                    dic=dic['command4']
                elif 'command3' in dic:
                    dic=dic['command3']
                elif 'command2' in dic:
                    dic=dic['command2']
                else:
                    dic=dic['command1']
            else: #2
                if 'command2' in dic:
                    dic=dic['command2']
                else:
                    dic=dic['command1']
        elif dualAltModifier: #3
            if 'command3' in dic:
                dic=dic['command3']
            else:
                dic=dic['command1']
        else: #1
            dic=dic['command1']

        if (isinstance(dic, (list))):
            for c in dic:
                #print(c['name'])

                if 'args' in c:
                    self.window.run_command(c['name'], c['args'])
                else:
                    self.window.run_command(c['name'])                
        else:
            #print(dic['name'])

            if 'args' in dic:
                self.window.run_command(dic['name'], dic['args'])
            else:
                self.window.run_command(dic['name'])
