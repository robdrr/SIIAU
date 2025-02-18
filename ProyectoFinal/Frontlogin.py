from usersBack import *

from customtkinter import *
from PIL import ImageTk, Image
import tkinter as tk





class Claselogin:
    def __init__(self, root):
        self.db=DBuser()
        self.db1 = DBuser()
        self.root = root
        self.root.geometry("600x440")
        self.root.title('Login')
        self.main_page = None

        background_image_login = ImageTk.PhotoImage(Image.open("./assets/pattern.png"))
        l1 = CTkLabel(master=root, image=background_image_login)
        l1.pack()

        self.frame_ml = CTkFrame(master=l1, width=320, height=360, corner_radius=15)
        self.frame_ml.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        l2 = CTkLabel(master=self.frame_ml, text="Log into your Account", font=('Century Gothic', 20))
        l2.place(x=50, y=45)

        self.entry_username_login = CTkEntry(master=self.frame_ml, width=220, placeholder_text='Username')
        self.entry_username_login.place(x=50, y=110)
        self.entry_username_login.bind("<Return>", self.set_focus)

        

        self.entry_password_login = CTkEntry(master=self.frame_ml, width=220, placeholder_text='Password', show="*")
        self.entry_password_login.place(x=50, y=165)
        self.entry_password_login.bind("<Return>", self.login)


        button_login = CTkButton(master=self.frame_ml, width=220, text="Login", command=self.login, corner_radius=6)
        button_login.place(x=50, y=240)


    def login(self, event=None):
        try:
            global loginmain
            username = self.entry_username_login.get()
            password = self.entry_password_login.get()

            lgn = self.db.login(username, password)

            self.db1.logindb(username)

            print(lgn)
            if lgn is not None:
                messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
                self.open_main_window()
            else:
                self.label_unsucces_login = CTkLabel(master=self.frame_ml, text="The Username/password is incorrect", font=('Century Gothic', 12))
                self.label_unsucces_login.place(x=50,y=195)
        except Exception as e:
            print(e)
            messagebox.showerror("Error", f"An error ocurred: {e}")

    def set_focus(self, event):
        self.entry_password_login.focus_set()
    


    def odio_vivir(self, username):
        global user
        user = username





