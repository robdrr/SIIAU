# import tkinter as tk
# from tkinter import messagebox, Menu, ttk
# from usersBack import *
# from teachersBack import *
# from degreeBack import *


# loginmain = None
# login2 = None

# class fTeacher:
#     def teachers_interface(self):
#         self.teachers_frame.pack_propagate(0)
#         self.dbT = DBteacher()
#         self.dbD = DBdegree()
#         # degrees = self.dbT.comboboxDegree()
#         # self.combobox_degree_teachers['values'] = degrees

#         tk.Label(self.teachers_frame, text="ID:").place(x=90, y=80)
#         self.entry_id_teachers = tk.Entry(self.teachers_frame, state="readonly")
#         self.entry_id_teachers.place(x=120, y=80)

#         tk.Label(self.teachers_frame, text="Name:").place(x=70, y=140)
#         self.entry_name_teachers = tk.Entry(self.teachers_frame)
#         self.entry_name_teachers.place(x=120, y=140)

#         tk.Label(self.teachers_frame, text="P. Surname:").place(x=40, y=200)
#         self.entry_psurname_teachers = tk.Entry(self.teachers_frame)
#         self.entry_psurname_teachers.place(x=120, y=200)

#         tk.Label(self.teachers_frame, text="M. Surname:").place(x=39, y=260)
#         self.entry_msurname_teachers = tk.Entry(self.teachers_frame)
#         self.entry_msurname_teachers.place(x=120, y=260)

#         tk.Label(self.teachers_frame, text="Email:").place(x=75, y=320)
#         self.entry_email_teachers = tk.Entry(self.teachers_frame)
#         self.entry_email_teachers.place(x=120, y=320)


#         degrees = self.dbD.degree_list()
#         tk.Label(self.teachers_frame, text="Degree:").place(x=350, y=140)
#         self.combobox_degree_teachers = ttk.Combobox(self.teachers_frame, values=degrees)
#         self.combobox_degree_teachers.place(x=410, y=140)
#         self.combobox_degree_teachers.config(state="readonly")


#         tk.Label(self.teachers_frame, text="Educational Level:").place(x=297, y=260)
#         self.combobox_education_teachers = ttk.Combobox(self.teachers_frame, values=["Bachelor", "Master", "Doctorate"])
#         self.combobox_education_teachers.place(x=410, y=260)
#         self.combobox_education_teachers.config(state="readonly")

        
#         global loginmain
#         loginmain = self.dbU.get_login1()
#         self.entry_name_teachers.insert(0, loginmain[1])
#         self.entry_name_teachers.config(state="readonly")

#         self.entry_psurname_teachers.insert(0, loginmain[2])
#         self.entry_psurname_teachers.config(state="readonly")

#         self.entry_msurname_teachers.insert(0, loginmain[3])
#         self.entry_msurname_teachers.config(state="readonly")

#         self.entry_email_teachers.insert(0, loginmain[4])
#         self.entry_email_teachers.config(state="readonly")
        

# #------------------ Botones ----------------------------------
        
#         self.button_new_teachers = tk.Button(self.teachers_frame, text="NEW",width=10, command=self.new_teacher)
#         self.button_new_teachers.place(x=30, y=380)
#         self.button_new_teachers.config(state="disabled")

#         self.button_save_teachers = tk.Button(self.teachers_frame, text="SAVE",width=10, command=self.create_teacher)
#         self.button_save_teachers.place(x=150, y=380)

#         self.button_Cancel_teachers = tk.Button(self.teachers_frame, text="CANCEL",width=10, command=self.cancel_teacher)
#         self.button_Cancel_teachers.place(x=270, y=380)

#         self.button_edit_teachers = tk.Button(self.teachers_frame, text="EDIT",width=10, command=self.update_teacher)
#         self.button_edit_teachers.place(x=390, y=380)

#         self.button_drop_teachers = tk.Button(self.teachers_frame, text="DROP",width=10, state="disabled", command=None)
#         self.button_drop_teachers.place(x=510, y=380)
#         self.teachers_bottons = [self.button_new_teachers, self.button_save_teachers, self.button_Cancel_teachers, self.button_edit_teachers, self.button_drop_teachers]


        
#         global login2
        
#         login2 = self.dbU.get_teacher()
#         print(login2)

#         if login2[0] is None:
#             print("Hola")
#         else:
#             print("Adios")
#             self.combobox_degree_teachers.config(state="normal")
#             self.combobox_degree_teachers.insert(0, login2[0])
#             self.combobox_degree_teachers.config(state="readonly")

#             self.combobox_education_teachers.config(state="normal")
#             self.combobox_education_teachers.insert(0, login2[1])
#             self.combobox_education_teachers.config(state="readonly")

#             self.button_save_teachers.configure(state="disabled")
        
        
        


# #----------------------------Teachers Functions--------------------------

#     def new_teacher(self):
#         try:
#             self.entry_name_teachers.delete(0, tk.END)
#             self.entry_psurname_teachers.delete(0,tk.END)
#             self.entry_msurname_teachers.delete(0, tk.END)
#             self.entry_email_teachers.delete(0, tk.END)
#             self.combobox_degree_teachers.set("")
#             self.combobox_education_teachers.set("")
            
#             #self.estado_nuevo(self.teachers_buttons) falta declarar una funcion para el boton nuevo

#         except Exception as e:
#             messagebox.showerror("Error", f"An error has occured: {e}")

#     def cancel_teacher(self):
#         try:
#             self.combobox_degree_teachers.config(state="normal")
#             self.combobox_education_teachers.config(state="normal")
#             self.entry_name_teachers.delete(0, tk.END)
#             self.entry_psurname_teachers.delete(0,tk.END)
#             self.entry_msurname_teachers.delete(0, tk.END)
#             self.entry_email_teachers.delete(0, tk.END)
#             self.combobox_degree_teachers.delete(0, tk.END)
#             self.combobox_degree_teachers.insert(0, login2[0])
#             self.combobox_education_teachers.delete(0, tk.END)
#             self.combobox_education_teachers.insert(0, login2[1])
#             self.combobox_degree_teachers.config(state="readonly")
#             self.combobox_education_teachers.config(state="readonly")

            
#             #self.estado_nuevo(self.teachers_buttons) falta declarar una funcion para el boton nuevo

#         except Exception as e:
#             messagebox.showerror("Error", f"An error has occured: {e}")

#     def create_teacher(self):
#         try:
#             degree = self.combobox_degree_teachers.get()
#             education = self.combobox_education_teachers.get()
#             user_id = loginmain [0]
#             new_teacher = Teachers(user_id = user_id, teacher_degree = degree, teacher_level = education)
#             self.dbT.create(new_teacher)
#         except Exception as e:
#             messagebox.showerror("Error", f"An error has occurred: {e}")

#     def update_teacher(self):
#         try:
#             user_id = loginmain [0]
#             degree = self.combobox_degree_teachers.get()
#             education = self.combobox_education_teachers.get()

#             self.dbT.update(user_id, degree, education)
#         except Exception as e:
#             messagebox.showerror("Error", f"An error has occurred: {e}")
            
#     def drop_teacher(self):
#         try:
#             teacher_id = self.entry_id_teachers.get()

#             if not teacher_id:
#                 messagebox.showerror("Error", "Por favor, primero selecciona un profesor.")
#                 return

#             confirmation = messagebox.askyesno("Confirmación", "¿Estás seguro que quieres eliminar este profesor?")

#             if confirmation:
#                 self.dbT.delete(teacher_id)
#                 messagebox.showinfo("Éxito", "Profesor eliminado exitosamente.")

#                 # Limpiar los campos después de eliminar al profesor
#                 self.entry_id_teachers.delete(0, tk.END)
#                 self.entry_name_teachers.delete(0, tk.END)
#                 self.entry_psurname_teachers.delete(0, tk.END)
#                 self.entry_msurname_teachers.delete(0, tk.END)
#                 self.entry_email_teachers.delete(0, tk.END)
#                 self.combobox_degree_teachers.set("")
#                 self.combobox_subject_teachers.set("")
#                 self.combobox_education_teachers.set("")
#         except Exception as e:
#             messagebox.showerror("Error", f"Ha ocurrido un error: {e}")




import tkinter as tk
from tkinter import messagebox, Menu, ttk
from usersBack import *
from teachersBack import *
from degreeBack import *


loginmain = None
login2 = None

class fTeacher:
    def teachers_interface(self):
        self.teachers_frame.pack_propagate(0)
        self.dbT = DBteacher()
        self.dbD = DBdegree()

        tk.Label(self.teachers_frame, text="ID:").place(x=90, y=80)
        self.entry_id_teachers = tk.Entry(self.teachers_frame, state="readonly")
        self.entry_id_teachers.place(x=120, y=80)

        tk.Label(self.teachers_frame, text="Name:").place(x=70, y=140)
        self.entry_name_teachers = tk.Entry(self.teachers_frame)
        self.entry_name_teachers.place(x=120, y=140)

        tk.Label(self.teachers_frame, text="P. Surname:").place(x=40, y=200)
        self.entry_psurname_teachers = tk.Entry(self.teachers_frame)
        self.entry_psurname_teachers.place(x=120, y=200)

        tk.Label(self.teachers_frame, text="M. Surname:").place(x=39, y=260)
        self.entry_msurname_teachers = tk.Entry(self.teachers_frame)
        self.entry_msurname_teachers.place(x=120, y=260)

        tk.Label(self.teachers_frame, text="Email:").place(x=75, y=320)
        self.entry_email_teachers = tk.Entry(self.teachers_frame)
        self.entry_email_teachers.place(x=120, y=320)


        degrees = self.dbD.degree_list()
        tk.Label(self.teachers_frame, text="Degree:").place(x=350, y=140)
        self.combobox_degree_teachers = ttk.Combobox(self.teachers_frame, values=degrees)
        self.combobox_degree_teachers.place(x=410, y=140)
        self.combobox_degree_teachers.config(state="readonly")


        tk.Label(self.teachers_frame, text="Educational Level:").place(x=297, y=260)
        self.combobox_education_teachers = ttk.Combobox(self.teachers_frame, values=["Bachelor", "Master", "Doctorate"])
        self.combobox_education_teachers.place(x=410, y=260)
        self.combobox_education_teachers.config(state="readonly")

        
        global loginmain
        loginmain = self.dbU.get_login1()
        self.entry_name_teachers.insert(0, loginmain[1])
        self.entry_name_teachers.config(state="readonly")

        self.entry_psurname_teachers.insert(0, loginmain[2])
        self.entry_psurname_teachers.config(state="readonly")

        self.entry_msurname_teachers.insert(0, loginmain[3])
        self.entry_msurname_teachers.config(state="readonly")

        self.entry_email_teachers.insert(0, loginmain[4])
        self.entry_email_teachers.config(state="readonly")
        

#------------------ Botones ----------------------------------
        
        self.button_new_teachers = tk.Button(self.teachers_frame, text="NEW",width=10, command=self.new_teacher)
        self.button_new_teachers.place(x=30, y=380)
        self.button_new_teachers.config(state="disabled")

        self.button_save_teachers = tk.Button(self.teachers_frame, text="SAVE",width=10, command=self.create_teacher)
        self.button_save_teachers.place(x=150, y=380)

        self.button_Cancel_teachers = tk.Button(self.teachers_frame, text="CANCEL",width=10, command=self.cancel_teacher)
        self.button_Cancel_teachers.place(x=270, y=380)

        self.button_edit_teachers = tk.Button(self.teachers_frame, text="EDIT",width=10, command=self.update_teacher)
        self.button_edit_teachers.place(x=390, y=380)
        self.button_edit_teachers.config(state="disabled")


        self.button_drop_teachers = tk.Button(self.teachers_frame, text="DROP",width=10, state="disabled", command=None)
        self.button_drop_teachers.place(x=510, y=380)
        self.button_drop_teachers.config(state="disabled")
        self.teachers_bottons = [self.button_new_teachers, self.button_save_teachers, self.button_Cancel_teachers, self.button_edit_teachers, self.button_drop_teachers]


        
        global login2
        
        login2 = self.dbU.get_teacher()
        print(login2)

        if login2[0] is None:
            print("Hola")
        else:
            print("Adios")
            self.combobox_degree_teachers.config(state="normal")
            self.combobox_degree_teachers.insert(0, login2[0])
            self.combobox_degree_teachers.config(state="readonly")

            self.combobox_education_teachers.config(state="normal")
            self.combobox_education_teachers.insert(0, login2[1])
            self.combobox_education_teachers.config(state="readonly")

            self.button_save_teachers.configure(state="disabled")
        
        
        


#----------------------------Teachers Functions--------------------------

    def new_teacher(self):
        try:
            self.entry_name_teachers.delete(0, tk.END)
            self.entry_psurname_teachers.delete(0,tk.END)
            self.entry_msurname_teachers.delete(0, tk.END)
            self.entry_email_teachers.delete(0, tk.END)
            self.combobox_degree_teachers.set("")
            self.combobox_education_teachers.set("")
            #self.button_save_teachers.config(state="normal")
            self.button_edit_teachers.config(state="disabled")
            self.button_drop_teachers.config(state="disabled")
            
            #self.estado_nuevo(self.teachers_buttons) falta declarar una funcion para el boton nuevo

        except Exception as e:
            messagebox.showerror("Error", f"An error has occured: {e}")

    def cancel_teacher(self):
        try:
            self.combobox_degree_teachers.config(state="normal")
            self.combobox_education_teachers.config(state="normal")
            self.entry_name_teachers.delete(0, tk.END)
            self.entry_psurname_teachers.delete(0,tk.END)
            self.entry_msurname_teachers.delete(0, tk.END)
            self.entry_email_teachers.delete(0, tk.END)
            self.combobox_degree_teachers.delete(0, tk.END)
            self.combobox_degree_teachers.insert(0, login2[0])
            self.combobox_education_teachers.delete(0, tk.END)
            self.combobox_education_teachers.insert(0, login2[1])
            self.combobox_degree_teachers.config(state="readonly")
            self.combobox_education_teachers.config(state="readonly")
            #self.button_save_teachers.config(state="normal")
            self.button_edit_teachers.config(state="disabled")
            self.button_drop_teachers.config(state="disabled")
            
            #self.estado_nuevo(self.teachers_buttons) falta declarar una funcion para el boton nuevo

        except Exception as e:
            messagebox.showerror("Error", f"An error has occured: {e}")

    def create_teacher(self):
        try:
            degree = self.combobox_degree_teachers.get()
            education = self.combobox_education_teachers.get()
            user_id = loginmain [0]
            new_teacher = Teachers(user_id = user_id, teacher_degree = degree, teacher_level = education)
            self.dbT.create(new_teacher)
            self.new_teacher()
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")

    def update_teacher(self):
        try:
            user_id = loginmain [0]
            degree = self.combobox_degree_teachers.get()
            education = self.combobox_education_teachers.get()

            self.dbT.update(user_id, degree, education)
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")
            
    def drop_teacher(self):
        try:
            teacher_id = self.entry_id_teachers.get()

            if not teacher_id:
                messagebox.showerror("Error", "Por favor, primero selecciona un profesor.")
                return

            confirmation = messagebox.askyesno("Confirmación", "¿Estás seguro que quieres eliminar este profesor?")

            if confirmation:
                self.dbT.delete(teacher_id)
                messagebox.showinfo("Éxito", "Profesor eliminado exitosamente.")

                # Limpiar los campos después de eliminar al profesor
                self.entry_id_teachers.delete(0, tk.END)
                self.entry_name_teachers.delete(0, tk.END)
                self.entry_psurname_teachers.delete(0, tk.END)
                self.entry_msurname_teachers.delete(0, tk.END)
                self.entry_email_teachers.delete(0, tk.END)
                self.combobox_degree_teachers.set("")
                self.combobox_subject_teachers.set("")
                self.combobox_education_teachers.set("")
                self.new_teacher()
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")
