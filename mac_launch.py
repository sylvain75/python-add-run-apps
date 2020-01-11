import requests
import os
import tkinter
from tkinter.filedialog import askopenfilename

from tkinter import ttk
from tkinter.ttk import *

from subprocess import Popen
import subprocess

root = tkinter.Tk()
apps = []

default_path = os.path.expanduser('~/Desktop')

if os.path.isfile('save.txt'):
    # IF THERE IS A save.txt OPEN AND READ ITS CONTENT AND BUILD A LIST FROM IT IN apps
    with open('save.txt', 'r') as f:
        temp_files = f.read()
        print('path', temp_files, type(temp_files))
        temp_files = temp_files.split(',')

        # BELOW WE ARE BUILDING A LIST IF ITEM.STRIP IS TRUTHY FROM TEMP_FILES
        apps = [x for x in temp_files if x.strip()]
        # apps = temp_files
        print('apps', apps)


def add_app():
    for widget in frame.winfo_children():
        widget.destroy()

    filename=askopenfilename(parent=root,
                            initialdir="/Applications",
                             title="Select App",
                             multiple=True,
                             filetypes=[("all files", "*.app")])
    print('FILENAME', filename)
    apps.append(filename)
    for app in apps:
        label = tkinter.Label(frame, text=app, bg='gray')
        label.pack()

def run_apps():
    for app in apps:
        # app is a tuple we need to convert as string
        app_string=''.join(app)
        print('app_string', app_string)
        # THE CODE BELOW ALSO WORKS FINE
        # subprocess.call(
        #     ["/usr/bin/open", "-W", "-n", "-a", app_string]
        # )
        command = "open '{}'".format(app_string)
        os.system(command)

canvas = tkinter.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()  # Attach to the root

frame = tkinter.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# style = ttk.Style()
# style.configure('W.OpenFile', font =
#                ('calibri', 10, 'bold', 'underline'),
#                 foreground = 'red')

openFile = tkinter.Button(root, text='Open File', padx=10,
                          pady=5, command=add_app)
openFile.pack()

runApps = tkinter.Button(root, text='Run Apps', padx=10,
                         pady=5, fg='white', bg='#263D42', command=run_apps)
runApps.pack()

for app in apps:
    label = tkinter.Label(frame, text=app)
    label.pack()

root.mainloop()

# BELOW WE WRITE THE APP_NAME ON CLOSE WINDOW => CODE NEEDS TO BE AFTER root.mainloop()
with open('save.txt', 'w') as f:
    for app in apps:
        app_string = ''.join(app)
        f.write(app_string + ',')
