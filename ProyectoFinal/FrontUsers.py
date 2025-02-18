
import tkinter as tk
from tkinter import messagebox, Menu, ttk
from usersBack import *
import re


class fUser:


    def users_interface(self):
        self.users_frame.pack_propagate(0)
        tk.Label(self.users_frame, text="Input User Code:").place(x=100, y=20)
        self.entry_search_users = tk.Entry(self.users_frame)
        self.entry_search_users.place(x=200, y=20)
        self.button_search_users = tk.Button(self.users_frame, text="Search",width=10, command=self.read_user)
        self.button_search_users.place(x=340, y=18)
        print("buscar")

        tk.Label(self.users_frame, text="ID:").place(x=90, y=80)
        self.entry_id_users = tk.Entry(self.users_frame, state="readonly")
        self.entry_id_users.place(x=120, y=80)

        tk.Label(self.users_frame, text="Name:").place(x=70, y=140)
        self.entry_name_users = tk.Entry(self.users_frame)
        self.entry_name_users.place(x=120, y=140)

        tk.Label(self.users_frame, text="P. Surname:").place(x=40, y=200)
        self.entry_psurname_users = tk.Entry(self.users_frame)
        self.entry_psurname_users.place(x=120, y=200)

        tk.Label(self.users_frame, text="M. Surname:").place(x=40, y=260)
        self.entry_msurname_users = tk.Entry(self.users_frame)
        self.entry_msurname_users.place(x=120, y=260)

        tk.Label(self.users_frame, text="Mail:").place(x=80, y=320)
        self.entry_mail_users = tk.Entry(self.users_frame)
        self.entry_mail_users.place(x=120, y=320)

        tk.Label(self.users_frame, text="Username:").place(x=300, y=140)
        self.entry_username_users = tk.Entry(self.users_frame)
        self.entry_username_users.place(x=370, y=140)

        tk.Label(self.users_frame, text="Password:").place(x=300, y=200)
        self.entry_password_users = tk.Entry(self.users_frame)
        self.entry_password_users.place(x=370, y=200)

        tk.Label(self.users_frame, text="Role:").place(x=330, y=260)
        self.combobox_role_users = ttk.Combobox(self.users_frame, values=["Admin", "Teacher", "Student"])
        self.combobox_role_users.place(x=370, y=260)

        
     
# -------------------- Botones ----------------------------------
        
        self.button_new_users = tk.Button(self.users_frame, text="NEW",width=10, command=self.new_users)
        self.button_new_users.place(x=30, y=380)

        self.button_save_users = tk.Button(self.users_frame, text="SAVE",width=10, command=self.create_users)
        self.button_save_users.place(x=150, y=380)

        self.button_Cancel_users = tk.Button(self.users_frame, text="CANCEL",width=10, command=self.cancel_users)
        self.button_Cancel_users.place(x=270, y=380)

        self.button_edit_users = tk.Button(self.users_frame, text="EDIT",width=10, command=self.update_user)
        self.button_edit_users.place(x=390, y=380)
        self.button_edit_users.config(state="disabled")

        self.button_drop_users = tk.Button(self.users_frame, text="DROP",width=10, command=self.delete_user)
        self.button_drop_users.place(x=510, y=380)
        self.button_drop_users.config(state="disabled")
        self.user_bottons = [self.button_new_users, self.button_save_users, self.button_Cancel_users, self.button_edit_users, self.button_drop_users]


    def search_state(self, bottons):
        try:
            bottons[0].config(state="normal")
            bottons[1].config(state="disabled")
            bottons[2].config(state="normal")
            bottons[3].config(state="normal")
            bottons[4].config(state="normal")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")




    def cancel_users(self):
        try:
            self.entry_id_users.config(state="normal")
            self.entry_id_users.delete(0, tk.END)
            self.entry_name_users.delete(0, tk.END)
            self.entry_psurname_users.delete(0, tk.END)
            self.entry_msurname_users.delete(0, tk.END)
            self.entry_mail_users.delete(0, tk.END)
            self.entry_username_users.delete(0, tk.END)
            self.entry_password_users.delete(0, tk.END)
            self.combobox_role_users.delete(0, tk.END)
            self.entry_id_users.config(state="readonly")
            self.button_save_users.config(state="normal")
            self.button_edit_users.config(state="disabled")
            self.button_drop_users.config(state="disabled")

            #self.new_states(self.user_buttons)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            
    def new_users(self):
        try:
            self.entry_id_users.config(state="normal")
            self.entry_id_users.delete(0, tk.END)
            self.entry_name_users.delete(0, tk.END)
            self.entry_psurname_users.delete(0, tk.END)
            self.entry_msurname_users.delete(0, tk.END)
            self.entry_mail_users.delete(0, tk.END)
            self.entry_username_users.delete(0, tk.END)
            self.entry_password_users.delete(0, tk.END)
            self.combobox_role_users.delete(0, tk.END)
            #self.search_state(self.user_bottons)
            self.entry_id_users.config(state="readonly")
            self.button_save_users.config(state="normal")
            self.button_edit_users.config(state="disabled")
            self.button_drop_users.config(state="disabled")

            #self.new_states(self.user_buttons)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


    def read_user(self):
        try: 
            self.cancel_users()
            self.entry_id_users.config(state="normal")
            user_id = self.entry_search_users.get()
            user = self.dbU.read(user_id)
            if user:
                if user[8]:
                    self.entry_id_users.delete(0, tk.END)
                    self.entry_name_users.delete(0, tk.END)
                    self.entry_psurname_users.delete(0, tk.END)
                    self.entry_msurname_users.delete(0, tk.END)
                    self.entry_mail_users.delete(0, tk.END)
                    self.entry_username_users.delete(0, tk.END)
                    self.entry_password_users.delete(0, tk.END)
                    self.combobox_role_users.delete(0, tk.END)

                    self.entry_id_users.insert(0, user[0])
                    self.entry_name_users.insert(0, user[1])
                    self.entry_psurname_users.insert(0, user[2])
                    self.entry_msurname_users.insert(0, user[3])
                    self.entry_mail_users.insert(0, user[4])
                    self.entry_username_users.insert(0, user[6])
                    self.entry_password_users.insert(0, user[5])
                    self.combobox_role_users.insert(0, user[7])
                    print(user[0])

                else:
                    messagebox.showerror("Error", "User no longer exists")
                    self.new_users()
            else:
                messagebox.showerror("Error", "User does not exist")
                self.new_users()
            self.entry_id_users.config(state="readonly")
            self.button_save_users.config(state="disabled")
            self.button_edit_users.config(state="normal")
            self.button_drop_users.config(state="normal")
            print("p")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")
            print("aqui")
        finally:
            self.search_state(self.user_bottons)
            print("5")


    def create_users(self):
        try:
            # Obtener los valores de los campos
            name = self.entry_name_users.get()
            psurname = self.entry_psurname_users.get()
            msurname = self.entry_msurname_users.get()
            email_name = name.replace(" ", "")
            email_psurname = psurname.replace(" ", "")
            email_msurname = msurname.replace(" ", "")

            # Generar el correo electrónico automáticamente
            mail = f"{email_name}{email_psurname}{email_msurname}@alumnos.udg.mx"
            username = self.entry_username_users.get()
            password = self.entry_password_users.get()
            role = self.combobox_role_users.get()

            # Validar campos vacíos
            if not all([name, psurname, msurname, username, password, role]):
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            # Validar que no haya números en los campos de nombre y apellidos
            if any(char.isdigit() for char in name + psurname + msurname):
                messagebox.showerror("Error", "Los campos de nombre y apellidos no pueden contener números.")
                return

            # Validar el formato de la contraseña
            if not re.match(r"^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=.{6,})", password):
                messagebox.showerror("Error", "La contraseña debe tener mínimo 6 caracteres, mayúsculas, números y al menos un símbolo válido '!@#$%^&*'.")
                return

            # Validar si ya existe un usuario con el mismo nombre de usuario
            existing_user = self.dbU.get_user_by_name(username)
            if existing_user:
                messagebox.showerror("Error", "Ya existe un usuario con el mismo nombre de usuario.")
                return

            # Crear el usuario
            new_user = User(user_name=name, user_paternalSurname=psurname, user_maternalSurname=msurname,
                            user_email=mail, user_password=password, user_username=username, user_role=role)
            self.dbU.create(new_user)
            self.cancel_users()
            #messagebox.showinfo("Éxito", "El usuario se ha creado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occured: {e}")

    def update_user(self):
        try:
            # Obtener los valores de los campos
            user_id = self.entry_search_users.get()
            name = self.entry_name_users.get()
            psurname = self.entry_psurname_users.get()
            msurname = self.entry_msurname_users.get()
            email_name = name.replace(" ", "")
            email_psurname = psurname.replace(" ", "")
            email_msurname = msurname.replace(" ", "")

            # Generar el correo electrónico automáticamente
            mail = f"{email_name}{email_psurname}{email_msurname}@alumnos.udg.mx"
            username = self.entry_username_users.get()
            password = self.entry_password_users.get()
            role = self.combobox_role_users.get()

            # Validar campos vacíos
            if not all([user_id, name, psurname, msurname, username, password, role]):
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            # Validar que no haya números en los campos de nombre y apellidos
            if any(char.isdigit() for char in name + psurname + msurname):
                messagebox.showerror("Error", "Los campos de nombre y apellidos no pueden contener números.")
                return

            # Validar el formato de la contraseña
            if not re.match(r"^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=.{6,})", password):
                messagebox.showerror("Error", "La contraseña debe tener mínimo 6 caracteres, mayúsculas, números y al menos un símbolo.")
                return
            
            # existing_user = self.dbU.get_user_by_name(username)
            # if existing_user:
            #     messagebox.showerror("Error", "Ya existe un usuario con el mismo nombre de usuario.")
            #     return

            # Actualizar el usuario
            update_user = User(user_id=user_id, user_name=name, user_paternalSurname=psurname,
                            user_maternalSurname=msurname, user_email=mail, user_password=password,
                            user_username=username, user_role=role)
            self.dbU.update(update_user)
            #messagebox.showinfo("Éxito", "El usuario se ha actualizado correctamente.")
        except Exception as e:
            messagebox.showerror("Erros", f"An error has occurred: {e}")



    def delete_user(self):
        try:
            user_id = int(self.entry_search_users.get())  # Convertir a int
            self.dbU.delete(user_id)  # Llamar al método delete con el user_id
            self.entry_id_users.delete(0, tk.END)
            self.entry_name_users.delete(0, tk.END)
            self.entry_psurname_users.delete(0, tk.END)
            self.entry_msurname_users.delete(0, tk.END)
            self.entry_mail_users.delete(0, tk.END)
            self.entry_username_users.delete(0, tk.END)
            self.entry_password_users.delete(0, tk.END)
            self.combobox_role_users.delete(0, tk.END)
            messagebox.showinfo("Éxito", "El usuario se ha eliminado correctamente.")
            self.new_users()
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al eliminar el usuario: {str(e)}")


