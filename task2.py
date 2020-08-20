import pyttsx3
import os

pyttsx3.speak("welcome to mukesh assistant")

while True:
    print("what to want to open : ",end='')
    p = input()
    if(("run" in p) or ("open" in p) or ("execute" in p)) and (("chrome" in p) or ("browser" in p)):
        os.system("chrome")
    elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
        os.system("notepad")
    elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("player" in p) or ("media" in p)):
        os.system("wmplayer")
    elif (("run" in p) or ("open" in p) or ("execute" in p)) and (("visualstdio" in p) or ("code" in p)):
        os.system("Code")
    elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("zoom" in p) :
        os.system("zoom")
    elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("command prompt" in p) or ("cmd" in p)):
        os.system("cmd")
    elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("power shell" in p) :
        os.system("PowerShell")
    elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("anydesk" in p) :
        os.system("AnyDesk")
    elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("camera" in p) :
        os.system("start microsoft.windows.camera:")
    elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("code blocks" in p) or ("codeblocks" in p)):
        os.system("CodeBlocks")
    elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("team viewer" in p) or ("teamviewer" in p)):
        os.system("TeamViewer")
    elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("sublime text" in p) or ("sublimetext" in p)):
        os.system("sublime_text")
    elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("virtual box" in p) or ("virtualbox" in p)):
        os.system("VirtualBox")
    elif ("exit" in p)  or ("quit" in p):
        break
    else:
        print("don't support")
