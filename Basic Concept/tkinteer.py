import tkinter as tk
import tkinter.font as ttk1 #fonts
from tkinter import Entry #entry by user
from tkinter import ttk

#Tk
window = tk.Tk()
window.title("Application")
window.geometry("900x1600")
window.minsize(400,300)

custom_font = ttk1.Font(family="Times New Roman", size=25, weight="bold",slant="roman")
label =  ttk.Label(text="Student Details",font=custom_font,padding=15)
#label["text"]="Have a good day!"
#label.config(text="How great you are")
label.pack()
label.pack(side="top")
#label.config(font=custom_font)

#counter = 0


def function_button():
    input_text=user_input.get()
    label.config(text=input_text)
     # global counter
     # counter = counter + 1
     # print("You fool")
     # label.config(text="You fool",font="Roman",fg="black",bg="blue")
     #label.config(text=f"The button go clicked:{counter}")

#Taking user input using entry
user_input= ttk.Entry(width=30,font=custom_font,show="*")
user_input.pack()
user_input.focus()


#buttons
button = ttk.Button(text="Click",command=function_button,padding=10)
button.pack(pady=10)

#exit the window
quit_button = ttk.Button(text="Quit",command=window.destroy)
quit_button.pack(side="bottom")

sep=ttk.Separator(orient="horizontal")
sep.pack(fill="x",padx=10,pady=100)

text=tk.Text(height=5,width=30)
text.pack(padx=10,pady=10)
text.focus()#for cursor
text.insert("1.0","Enter your comments")#for default text
text_data=text.get("1.0","end")
print(text_data)

def text_function():
    text_data=text.get("1.0","end")
    print(text_data)

text_button=ttk.Button(text="Get Text",command=text_function)
text_button.pack()
"""
text["state"]="disabled"
def enable_text():
    text["state"]="normal"


enable_button = ttk.Button(text="Enable",command=enable_text)#enable button
enable_button.pack()

"""
check_option= tk.StringVar()
def check_option_task():
     print(check_option.get())

check_button=ttk.Checkbutton(text="Agree with terms and conditions",variable=check_option,command=check_option_task,onvalue="Yes",offvalue="No")
check_button.pack()

#radio button
radio_value=tk.StringVar()
def get_radio_value():
    print(radio_value.get())


option_1=ttk.Radiobutton(text="Male",variable=radio_value,value="Male",command=get_radio_value)

option_2=ttk.Radiobutton(text="Female",variable=radio_value,value="Female",command=get_radio_value)

option_3=ttk.Radiobutton(text="Other",variable=radio_value,value="Other",command=get_radio_value)
option_1.pack()
option_2.pack()
option_3.pack()

#Combo boxes
combo_box=tk.StringVar()
def combo_box_function(event):
    msg=f"Selected country: {combo_box.get()}"
    country_label = ttk.Label(text=msg, padding=15)
    # label["text"]="Have a good day!"
    # label.config(text="How great you are")
    country_label.pack()
    #print(f"Selected country: {combo_box.get()}")


countries=ttk.Combobox(textvariable=combo_box,value=("India","Australia","Canada","Africa","America"),state="readonly")
countries.pack()

countries.bind("<<ComboboxSelected>>",combo_box_function)

#list box
food_items=("Pizza","Salad","Paneer","Nachos","Garlic Bread")
fav_food= tk.StringVar(value=food_items)

food=tk.Listbox(listvariable=fav_food,height=5,selectmode="extended")
food.pack()

def food_function(event):
    food_indices=food.curselection()
    for i in food_indices:
        print(food.get(i))

food.bind("<<ListboxSelect>>",food_function)

#spinbox
def spin_box_function():
    print("Current Value:",spin_box.get())
counter=tk.IntVar(value=10)
spin_box=ttk.Spinbox(values=tuple(range(10,40,2)),textvariable=counter,wrap=True,command=spin_box_function)
spin_box.pack()





window.mainloop()