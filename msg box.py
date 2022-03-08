import ctypes 
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
for i in range (1,100):
    Mbox('Error', 'Page Unressponsive',1)
