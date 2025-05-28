from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():

    if usernameE.get()=='' or passwordE.get()=='':
        messagebox.showerror('Error','All details are required')
    elif usernameE.get()=='Jay' and passwordE.get()=='1234':
        messagebox.showinfo('Success','Login is Successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Wrong Credentials')


root=CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('login page')
image=CTkImage(Image.open('cover.jpg'),size=(930,478))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text='Employee Management System',bg_color='#FAFAFA',font=('Georgia',30,'bold'),text_color='#040410')
headinglabel.place(x=200,y=50)


usernameE=CTkEntry(root,placeholder_text='Enter Your Username',width=180)
usernameE.place(x=380,y=150)

passwordE=CTkEntry(root,placeholder_text='Enter Your Password',width=180,show='*')
passwordE.place(x=380,y=210)

loginbutton=CTkButton(root,text='Login',cursor='hand2',command=login)
loginbutton.place(x=400,y=280)
root.mainloop()


