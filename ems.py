from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database

#function

def deleteall():
    result= messagebox.askyesno('Confirm','Do you really want to delete all records ?')
    if result:
        database.deleteall_records()
    else:
        pass

def showall():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search By')

def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror('Eror','Enter the value to select')
    elif searchBox.get()=='Search By':
        messagebox.showerror('Error','Please select an option')
    else:
        searched_data=database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('',END,values=employee)
def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select data to delete')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showeinfo('Error','Data is deleted')


def update_employee():
      selected_items=tree.selection()
      if not selected_items:
          messagebox.showerror('Error','Select data to update')
      else:
          database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),rolebox.get(),genderbox.get(),salaryEntry.get())
          treeview_data()
          clear()
          messagebox.showinfo('Success','Data is updated')


def selection(event=None):
        selected_item = tree.selection()
        if selected_item:
            row = tree.item(selected_item)['values']
            clear()
            idEntry.insert(0, row[0])
            nameEntry.insert(0, row[1])
            phoneEntry.insert(0, row[2])
            rolebox.set(row[3])
            genderbox.set(row[4])
            salaryEntry.insert(0, row[5])
def clear(value= False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    rolebox.set('Brand Manager')
    genderbox.set('Male')
    salaryEntry.delete(0, END)
def treeview_data():

    for row in tree.get_children():
        tree.delete(row)


    employees = database.fetch_employees()


    for employee in employees:
        tree.insert('', END, values=employee)
def add_employee():
    if idEntry.get() == '' or phoneEntry.get() == '' or nameEntry.get() == '' or salaryEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required.')
    elif database.id_exist(idEntry.get()):
        messagebox.showerror('Error', 'Id already exists.')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error', 'Invalid ID format.Use EMP with following numbers.')
    else:

        database.insert(idEntry.get(), nameEntry.get(), phoneEntry.get(), rolebox.get(), genderbox.get(), salaryEntry.get())


        treeview_data()


        clear()


#GUI part

window=CTk()
window.geometry('930x580+100+100')
window.resizable(0,0)
window.title('Employee Management System')
window.configure(fg_color='#020231')
logo=CTkImage(Image.open('bg.jpg'),size=(930,158))
logoLabel=CTkLabel(window,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan=2)

leftFrame=CTkFrame(window,fg_color='#020231')
leftFrame.grid(row=1,column=0)

idLabel=CTkLabel(leftFrame,text='Id',font=('arial',18,'bold'),text_color='white')
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')

idEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftFrame,text='Name',font=('arial',18,'bold'),text_color='white')
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')

nameEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)

phoneLabel=CTkLabel(leftFrame,text='Phone',font=('arial',18,'bold'))
phoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')

phoneEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
phoneEntry.grid(row=2,column=1)

roleLabel=CTkLabel(leftFrame,text='Role',font=('arial',18,'bold'))
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')
role_options=['Marketing Manager','Brand Manager','Digital Marketing Manager','Financial Analyst',
              'Risk Manager','HR Manager','Business Analyst','IT Manager','Data Analyst']
rolebox=CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',15,'bold'),state='readonly')
rolebox.grid(row=3,column=1)
rolebox.set(role_options[0])

genderLabel=CTkLabel(leftFrame,text='Gender',font=('arial',18,'bold'),text_color='white')
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')

gender_options=['Male','Female','Others']
genderbox=CTkComboBox(leftFrame,values=gender_options,width=180,font=('arial',15,'bold'),state='readonly')
genderbox.grid(row=4,column=1)
genderbox.set(gender_options[0])

salaryLabel=CTkLabel(leftFrame,text='Salary',font=('arial',18,'bold'))
salaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')

salaryEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
salaryEntry.grid(row=5,column=1)

rightFrame=CTkFrame(window)
rightFrame.grid(row=1,column=1)

search_options=['Id','Name','Phone','Role','Gender','Salary']
searchBox=CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')

searchEntry=CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame,text='Search',width=80,command=search_employee)
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightFrame,text='ShowAll',width=80,command=showall)
showallButton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Phone','Role','Gender','Salary')

tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.configure(show='headings')

tree.column('Id',width=100)
tree.column('Name',width=120)
tree.column('Phone',width=150)
tree.column('Role',width=160)
tree.column('Gender',width=120)
tree.column('Salary',width=130)

style=ttk.Style()

style.configure('Treeview.Heading',font=('arial',18,'bold'))
style.configure('Treeview',font=('arial',14,'bold') ,rowheight=30,background='#161C30',foreground='white')

scrollbar=ttk.Scrollbar(rightFrame,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame=CTkFrame(window,fg_color='#020231')
buttonFrame.grid(row=2,column=0,columnspan=2,pady=10)

newButton=CTkButton(buttonFrame,text='New Employee',font=('arail',18,'bold'),width=150,corner_radius=15,command= lambda: clear(True))
newButton.grid(row=0,column=0,pady=5,padx=5)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('arail',18,'bold'),width=150,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)

updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arail',18,'bold'),width=150,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arail',18,'bold'),width=150,corner_radius=15,command=delete_employee)
deleteButton.grid(row=0,column=3,pady=5,padx=5)

deleteallButton=CTkButton(buttonFrame,text='DeleteAll',font=('arail',18,'bold'),width=150,corner_radius=15,command=deleteall)
deleteallButton.grid(row=0,column=4,pady=5,padx=5)

treeview_data()

tree.bind('<ButtonRelease-1>', selection)

window.mainloop()
