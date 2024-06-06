from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


def addTask():
    task=entry_box.get()
    if task!="":
        l.insert(END,task)
        entry_box.delete(0,"end")
    else:
        messagebox.showwarning("Taskbox Empty! Please enter a task.")

def deleteTask():
    l.delete(ANCHOR)

#parentframe
w=tk.Tk()
w.title("To-Do List")
w.config(bg="PeachPuff3")
w.geometry('750x600+20+20')
w.resizable(width=True,height=True)

#childframe
f=tk.Frame(w)
f.pack(padx=20,pady=20)

#adding an entry box
entry_box=Entry(w,font=('Courier New',18,"bold"),bd=2,fg='black',bg='floral white',width=25)
entry_box.pack(pady=10)

#adding a listbox inside the frame
l=tk.Listbox(f,width=35,height=10,font=('Courier New',16),bd=2,fg="black",bg="floral white",highlightthickness=1,activestyle='underline',selectbackground='orange red')
l.pack(side=RIGHT,padx=10,pady=10)
 
 #adding a scrollbar to the frame
scroll=Scrollbar(f,command=l.yview)
scroll.pack(side=tk.RIGHT,fill=BOTH)
l.config(yscrollcommand=scroll.set)

#adding button to the frame
button=Frame(w)
button.pack(pady=20)

#add button
add=Button(button,text='ADD TASK',font=('Bookman Old Style',14),bg="Salmon3",padx=6,pady=5,command=addTask)
add.pack(expand=True,fill=BOTH,side=LEFT)


#delete button
delete=Button(button,text='DELETE TASK',font=('Bookman Old Style',14),bg="LightSalmon4",padx=6,pady=5,command=deleteTask)
delete.pack(expand=True,fill=BOTH,side=RIGHT)


#task list
task_list=['go to work',
           'code for an hour']
 
#adding tasks to the list
for item in task_list:
    l.insert(tk.END,item)

w.mainloop()