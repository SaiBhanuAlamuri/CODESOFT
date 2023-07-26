#Codsoft internship Task-1

from tkinter import *
from tkinter.font import Font
root =Tk()
root.title("CODESOFT TASK-1:TO DO LIST!")
root.geometry("500x500")
lb=Label(root,text="Task Bar",font="Algerian 20",fg="Violet",bg="black")
lb.pack()
#Define our font
my_font=Font(
    family="Garamond",
    size=30,
    weight="bold"
)
#Create frame
my_frame=Frame(root)
my_frame.pack(pady=10)
#Craete list box
my_list=Listbox(my_frame,
                font=my_font,
                width=25,
                height=5,
                bg ="black",
                bd=0,
                fg="Violet",
                highlightthickness=0,
                selectbackground="#a6a6a6",
                activestyle="none"
               
               )
my_list.pack(side=LEFT,fill=BOTH)
#Create dummy list
stuff=["Hello","Iam Sai Bhanu Alamuri","My first task","Developed using tkinter"]
#Add dummy list to list
for item in stuff:
    my_list.insert(END,item)
#Create scroll bar
my_scrollbar=Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)
#Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list)
#Create entry box to add items to the list
my_entry=Entry(root,font=("Garamond",24))
my_entry.pack(pady=20)
#Create a button frame
button_frame=Frame(root)
button_frame.pack(pady=20)
#Functions
def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END,my_entry.get())
    my_entry.delete(0,END)
def cross_off_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede"
    )
    my_list.selection_clear(0,END)
    
def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="Violet"
    )
    my_list.selection_clear(0,END)
def delete_crossed():
    count=0
    while count < my_list.size():
        if my_list.itemcget(count,"fg")=="#dedede":
            my_list.delete(my_list.index(count))
        count+=1
#Add some buttons
delete_button=Button(button_frame,text="Delete Item",command=delete_item,fg="dark blue",bg="white")
add_button=Button(button_frame,text="Add Item",command=add_item,fg="dark blue")
cross_off_button=Button(button_frame,text="Cross off Item",command=cross_off_item,fg="dark blue")
uncross_button=Button(button_frame,text="UnCross Item",command=uncross_item,fg="dark blue")
delete=Button(button_frame,text="Delete Crossed",command=delete_crossed,fg="dark blue")

delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1,padx=20)
cross_off_button.grid(row=0,column=2)
uncross_button.grid(row=0,column=3,padx=20)
delete.grid(row=0,column=4)
root.mainloop()
