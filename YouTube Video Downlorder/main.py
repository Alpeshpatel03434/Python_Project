import tkinter as tk
from pytube import YouTube

root = tk.Tk()
root.title("YouTube Video Downloader")

root.geometry("600x400")

title = tk.Label(root, text='YouTube Video Downloader', bg='blue', font=('calibre', 14, 'italic'), bd = 5)
title.pack()

# Set icon
try:
    root.wm_iconbitmap("Notepad.ico")
except:
    pass

name_var = tk.StringVar()
path_var = tk.StringVar()


# defining a function that will
# get the name and password and
# print them on the screen
def submit():
    name = name_var.get()

    print("The YouTube Link : " + name)

    name_var.set("")
    YouTube('"' + name + '"').streams.first().download("/YouTube Video-Download")
    print("Wait some time when Screen Or GUI screen clear")


# creating a label for
# name using widget Label
name_label = tk.Label(root, text='YouTube Link', bg='yellow', font=('calibre', 12, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 12, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', bg='green', font=('calibre', 14, 'bold'), activebackground='red', height = 1, width = 8, command=submit)

exit_btn = tk.Button(root, text='Exit', bg='green', font=('calibre', 14, 'bold'), activebackground='red',  width = 4, command=exit)
title.place(x=200, y=40)
name_label.place(x=150, y=150)
name_entry.place(x=300, y=150)
sub_btn.place(x=280, y=200)
exit_btn.place(x=250, y=260)

root.configure(bg='#808080')
root.mainloop()