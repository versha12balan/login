from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

class Login_Window:
    def __init__(self,win):
        self.win=win
        self.win.title("Login")
        self.win.iconbitmap(r"C:\Users\HP\Desktop\New folder\images (1).png")
        self.win .geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\HP\Desktop\New folder\718-1-VUk7L.jpg")
        lb1_bg=Label(self.win,image=self.bg)
        lb1_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.win,bg="black")
        frame.place(x=610,y=170,height=500,width=340)
        

        img1=Image.open(r"C:\Users\HP\Desktop\New folder\images.jpeg")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbimg1=Label(image=self.photoimage1,borderwidth=0)
        lbimg1.place(x=730,y=175,width=100,height=100)

        label_1=Label(frame,text="Get Started",font=("Times New Roman",25,"bold"),fg="white",bg="black")
        label_1.place(x=90,y=100)

        #label
        username_lb1=Label(frame,text="Username",font=("Times New Roman",18,"bold"),fg="white",bg="black")
        username_lb1.place(x=50,y=155)

        self.txtname=ttk.Entry(frame,font=("Times New Roman",18,"bold"))
        self.txtname.place(x=30,y=190,width=270)

        password_lb1=Label(frame,text="Password",font=("Times New Roman",18,"bold"),fg="white",bg="black")
        password_lb1.place(x=50,y=225)

        self.password=ttk.Entry(frame,font=("Times New Roman",18,"bold"))
        self.password.place(x=30,y=260,width=270)

        #image======================= icon

        img1=Image.open(r"C:\Users\HP\Desktop\New folder\images (3).jpeg")
        img1=img1.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img1)
        lbimg1=Label(image=self.photoimage2,borderwidth=0,fg="white",bg="black")
        lbimg1.place(x=635,y=327,width=25,height=25)

        img1=Image.open(r"C:\Users\HP\Desktop\New folder\images (2).jpeg")
        img1=img1.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img1)
        lbimg1=Label(image=self.photoimage3,borderwidth=0,fg="white",bg="black")
        lbimg1.place(x=635,y=399,width=25,height=25)

        #login button
        login_button=Button(frame,command=self.login,text="Login",font=("Times New Roman",18,"bold"),relief=GROOVE,bd=3,fg="white",bg="red",activeforeground="white",activebackground="red")
        login_button.place(x=110,y=300,height=50,width=120)
        

        # registor button

        button=Button(frame,text="Create New Account",font=("Times New Roman",15,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        button.place(x=10,y=370,width=200)
        
        # forgot button
        button=Button(frame,text="Forget Password ?",font=("Times New Roman",15,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        button.place(x=8,y=400,width=200)

    def login(self):
        if self.txtname.get()==""  or self.password.get()=="":
              messagebox.showerror("error","all fields mandantory")
        elif  self.txtname.get()=="hi" and self.password.get()=="123":
             messagebox.showinfo("Success","welcome")
        else:
             messagebox.showerror("Invalid","Invalid username & password")

        


if __name__ =="__main__":
    win=Tk()   
    app=Login_Window(win)  
    win.mainloop() 

