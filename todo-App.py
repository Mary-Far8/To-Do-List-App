from tkinter import *
from tkinter import messagebox

# create the main app window
TDL_App = Tk()

# set the window title
TDL_App.title(" To_Do List App  ")

# set a fixed window size: 400px wide, 600px tall
TDL_App.geometry('400x600')

# set the window's background color
TDL_App.configure(bg="green")



# heading label telling the user what to do
TDL_Label1 = Label(TDL_App,text=" Enter Your Task  ",fg = "white", bg = "green",font=('Arial',20,'bold'),pady=20,padx=10)
TDL_Label1.pack(pady=(30, 0)) 


# StringVar bridges the Entry box on screen with a plain Python value
task = StringVar()

# placeholder text shown before the user types a real task
placeholder ="ex: working 2h"

# preload the Entry box with the placeholder text
task.set(placeholder)


# Entry box where the user types a new task
# width is sized to fit the placeholder text's length + a little extra room
TDL_Label2 = Entry(TDL_App, textvariable=task , font=('Arial',12,'bold'), width=len(task.get())+3 ,borderwidth=0,fg='grey')
TDL_Label2.pack(pady=15)


# runs automatically when the user clicks INTO the Entry box (gains focus)
def when_clicked_in(event):
    # only clear it if it's still showing the placeholder, not real typed text
    if task.get() == placeholder:
        task.set("")
        event.widget.config(fg='black')

# runs automatically when the user clicks AWAY from the Entry box (loses focus)
def when_clicked_out(event):
    # only restore the placeholder if the user left the box empty
    if task.get() == "" :
        task.set(placeholder)
        event.widget.config(fg='grey')

# connect the two functions above to their events on the Entry box
TDL_Label2.bind("<FocusIn>", when_clicked_in)
TDL_Label2.bind("<FocusOut>", when_clicked_out) 


# runs when the "Add to To-Do List" button is clicked
def add_to_tdl():
    task_variable = task.get()

    # ignore empty input, the untouched placeholder, or a single space
    if task_variable == "" or task_variable == placeholder or task_variable == " ":
        return

    # add the task as a new line at the bottom of the Listbox
    The_list.insert("end", task_variable)

    # clear the Entry box so it's ready for the next task
    task.set("")


# runs when the "Delete from To-Do List" button is clicked
def delete_selected() :
    # get the currently selected item's index, as a tuple e.g. (2,)
    selected_task = The_list.curselection()

    # if nothing is selected, curselection() returns an empty tuple — do nothing
    if selected_task == () :
        return

    # remove the selected task from the Listbox
    The_list.delete(selected_task[0]) 


# button that adds the typed task to the list
btn = Button(TDL_App,
              bg="#1B5E20",
             text='Add to To-Do List',
             font=('Arial',10,'bold'),
             fg='#E8F5E9',
             borderwidth=0.5,
             command=add_to_tdl)
btn.pack(pady=10)


# the list widget that displays all added tasks
The_list = Listbox(TDL_App, bg='#E8F5E9',width=40, borderwidth=0,height=20 )
The_list.pack(pady=10) 


# button that deletes whichever task is currently selected
btn2 = Button(TDL_App,
               bg="#1B5E20",
                 text='Delete from To-Do List',
                 font=('Arial',10,'bold'),
                 fg='#E8F5E9',
                 borderwidth=0.5,
                 command=delete_selected)
btn2.pack(pady=10) 

# start the app's event loop keeps the window open and 
# continuously watches for events

TDL_App.mainloop()