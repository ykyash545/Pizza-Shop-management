from tkinter import *
import webbrowser

#Create an instance of tkinter frame
win = Tk()
win.title("Payment")
win.geometry("250x64")

#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

#Create a Label to display the link
link = Label(win,text="Pay to Pizza Safari",font=('Helveticabold', 15), fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e:
callback("https://rzp.io/l/7NYseiWi"))

win.mainloop()