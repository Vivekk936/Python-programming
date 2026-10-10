import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Application")

my_frame=ttk.Frame()
my_frame.pack(side="left",fill="both",expand=True)

label1=tk.Label(my_frame,text="Hello world",bg="red",fg="white")
label1.pack(side="top",fill='both',expand=True)

label2=tk.Label(text="How are you?",bg="blue",fg="white")
label2.pack(side="top",fill='both',expand=True)

label3=tk.Label(window,text="Have you done this course?",bg="green",fg="white")
label3.pack(side="top",fill='both',expand=True)

"""quit_button=ttk.Button(text="Exit",command=window.destroy)
quit_button.pack()
"""
window.mainloop()