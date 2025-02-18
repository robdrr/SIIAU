import tkinter as tk
from tkinter import messagebox, Menu, ttk
from usersBack import *
import re
# from intermedario import loginmain
from tkcalendar import DateEntry
from studentsBack import *
from usersBack import *

loginmain = None
class fStudent:

    def students_interface(self):
        
        self.students_frame.pack_propagate(0)  
        cohorts = self.dbS.comboboxCohorts()
        degrees = self.dbS.comboboxDegree()
       
        # tk.Label(self.students_frame, text="Student Code:").place(x=20, y=100)
        # self.entry_usercode_student = tk.Entry(self.students_frame)
        # self.entry_usercode_student.place(x=250, y=100)
        # self.button_search_student = tk.Button(self.students_frame, text="Search")
        # self.button_search_student.place(x=450, y=100, width=100, height=30)

        tk.Label(self.students_frame, text="ID:").place(x=20, y=140)
        self.entry_id_student = tk.Entry(self.students_frame, state='readonly')
        self.entry_id_student.place(x=250, y=140)

        tk.Label(self.students_frame, text="Name:").place(x=20, y=180)
        self.entry_name_student = tk.Entry(self.students_frame)
        self.entry_name_student.place(x=250, y=180)

        tk.Label(self.students_frame, text="Last Name:").place(x=20, y=220)
        self.entry_last_name_student = tk.Entry(self.students_frame)
        self.entry_last_name_student.place(x=250, y=220)

        tk.Label(self.students_frame, text="M Last Name:").place(x=20, y=260)
        self.entry_mother_last_name_student = tk.Entry(self.students_frame)
        self.entry_mother_last_name_student.place(x=250, y=260)

        tk.Label(self.students_frame, text="Email:").place(x=20, y=300)
        self.entry_email_student = tk.Entry(self.students_frame)
        self.entry_email_student.place(x=250, y=300)

        tk.Label(self.students_frame, text="State:").place(x=20, y=340)
        self.combobox_state_student = ttk.Combobox(self.students_frame, values=["Guadalajara", "CDMX"])
        self.combobox_state_student.place(x=250, y=340)

        tk.Label(self.students_frame, text="Birth day:").place(x=600, y=140)
        self.date_entry_borndate_student = DateEntry(self.students_frame)
        self.date_entry_borndate_student.place(x=750, y=140)

        tk.Label(self.students_frame, text="Degree:").place(x=600, y=180)
        self.combobox_career_student = ttk.Combobox(self.students_frame, values=degrees)
        self.combobox_career_student.place(x=750, y=180)

    
        tk.Label(self.students_frame, text="ID Groups:").place(x=600, y=260)
        self.combobox_idgroups_student = ttk.Combobox(self.students_frame, values=cohorts)
        self.combobox_idgroups_student.place(x=750, y=260)

        global loginmain
        loginmain = self.dbU.get_login1()


        self.entry_name_student.insert(0, loginmain[1])
        self.entry_name_student.config(state="readonly")

        self.entry_last_name_student.insert(0, loginmain[2])
        self.entry_last_name_student.config(state="readonly")

        self.entry_mother_last_name_student.insert(0, loginmain[3])
        self.entry_mother_last_name_student.config(state="readonly")

        self.entry_email_student.insert(0, loginmain[4])
        self.entry_email_student.config(state="readonly")

            # -------------------- Botones ----------------------------------
        self.button_create_student = tk.Button(self.students_frame, text="Nuevo", command=self.new_student)
        self.button_create_student.place(x=20, y=380, width=80, height=30)

        self.button_read_student = tk.Button(self.students_frame, text="Guardar", command=self.create_student)
        self.button_read_student.place(x=120, y=380, width=80, height=30)

        self.button_cancel_student = tk.Button(self.students_frame, text="Cancelar", command=self.cancel_student)
        self.button_cancel_student.place(x=220, y=380, width=80, height=30)
        self.button_cancel_student.config(state='disabled')

        self.button_update_student = tk.Button(self.students_frame, text="Editar", command=self.update_student)
        self.button_update_student.place(x=320, y=380, width=80, height=30)
        self.button_update_student.config(state='disabled')

        self.button_drop_student = tk.Button(self.students_frame, text="Baja", state="disabled", command=None)
        self.button_drop_student.place(x=420, y=380, width=80, height=30)
        


        self.student_buttons= [self.button_create_student, self.button_read_student, self.button_cancel_student, self.button_update_student, self.button_drop_student]

    def cancel_student(self):
        try:
            self.entry_name_student.delete(0, tk.END)
            self.entry_last_name_student.delete(0,tk.END)
            self.entry_mother_last_name_student.delete(0, tk.END)
            self.entry_email_student.delete(0, tk.END)
            self.combobox_status_student.set("")
            self.date_entry_borndate_student.delete(0, tk.END)
            self.combobox_career_student.set("")

        # self.estado_nuevo(self.student_buttons) falta declarar una funcion para el boton nuevo
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            
    def new_student(self):
        try:
            self.entry_name_student.delete(0, tk.END)
            self.entry_last_name_student.delete(0,tk.END)
            self.entry_mother_last_name_student.delete(0, tk.END)
            self.entry_email_student.delete(0, tk.END)
            self.combobox_status_student.set("")
            self.date_entry_borndate_student.delete(0, tk.END)
            self.combobox_career_student.set("")
        # self.estado_nuevo(self.student_buttons) falta declarar una funcion para el boton nuevo
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def create_student(self):
        # name = self.entry_name_student.get()
        # psurname = self.entry_last_name_student.get()            
        # msurname = self.entry_mother_last_name_student.get()
        # email = self.entry_email_student.get()
        state = self.combobox_status_student.get()
        birthday = self.date_entry_borndate_student.get_date()
        degree = self.combobox_career_student.get()
        cohort_id = self.combobox_idgroups_student.get()
        user_id= loginmain[0]
        new_student =Students(user_id = user_id, student_degree= degree,  student_state=state, student_birthday=birthday, cohort_id=cohort_id)
        self.dbS.create(new_student)

    def update_student(self):
        user_id = loginmain[0]
        state = self.combobox_status_student.get()
        birthday = self.date_entry_borndate_student.get_date()
        degree = self.combobox_career_student.get()

        self.dbS.update(user_id, degree, state, birthday)