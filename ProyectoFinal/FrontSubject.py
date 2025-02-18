import tkinter as tk
from tkinter import messagebox, Menu, ttk

from subjectBack import *


class fSubject:
    def subjects_interface(self):
        self.subjects_frame.pack_propagate(0)
        #self.dbSU = DBsubject()

        schedules = ["L | 07:00 - 09:00",
                     "L | 09:00 - 11:00",
                     "L | 11:00 - 13:00",
                     "M | 07:00 - 09:00",
                     "M | 09:00 - 11:00",
                     "M | 11:00 - 13:00",
                     "MI | 07:00 - 09:00",
                     "MI | 09:00 - 11:00",
                     "MI | 11:00 - 13:00",
                     "J | 07:00 - 09:00",
                     "J | 09:00 - 11:00",
                     "J | 11:00 - 13:00",
                     "V | 07:00 - 09:00",
                     "V | 09:00 - 11:00", "V | 11:00 - 13:00"]
        degrees = self.dbSU.comboboxDegree()
        teachers=self.dbSU.comboboxTeacher()
        classrooms=self.dbSU.comboboxRoom()
        # self.combobox_degree_subjects = degrees
        # self.combobox_teacher_subjects = teachers
        # self.combobox_classroom_subjects = classrooms        

        tk.Label(self.subjects_frame, text="Input Subject Code:").place(x=100, y=20)
        self.entry_search_subjects = tk.Entry(self.subjects_frame)
        self.entry_search_subjects.place(x=215, y=20)
        self.button_search_subjects = tk.Button(self.subjects_frame, text="Search",width=10, command=self.read_subject)
        self.button_search_subjects.place(x=355, y=18)

        tk.Label(self.subjects_frame, text="ID:").place(x=90, y=80)
        self.entry_id_subjects = tk.Entry(self.subjects_frame, state="readonly")
        self.entry_id_subjects.place(x=120, y=80)

        tk.Label(self.subjects_frame, text="Subject:").place(x=65, y=140)
        self.entry_name_subjects = tk.Entry(self.subjects_frame)
        self.entry_name_subjects.place(x=120, y=140)

        tk.Label(self.subjects_frame, text="Credits:").place(x=65, y=200)
        self.entry_credits_subjects = tk.Entry(self.subjects_frame)
        self.entry_credits_subjects.place(x=120, y=200)

        tk.Label(self.subjects_frame, text="Semester:").place(x=55, y=260)
        self.entry_semester_subjects = tk.Entry(self.subjects_frame)
        self.entry_semester_subjects.place(x=120, y=260)

        tk.Label(self.subjects_frame, text="Schedule:").place(x=55, y=320)
        self.combobox_schedule_subjects = ttk.Combobox(self.subjects_frame, values=schedules)
        self.combobox_schedule_subjects.place(x=120, y=320)

        tk.Label(self.subjects_frame, text="Degree:").place(x=350, y=140)
        self.combobox_degree_subjects = ttk.Combobox(self.subjects_frame, values=degrees)
        self.combobox_degree_subjects.place(x=410, y=140)

        tk.Label(self.subjects_frame, text="Teacher:").place(x=345, y=200)
        self.combobox_teacher_subjects = ttk.Combobox(self.subjects_frame, values=teachers)
        self.combobox_teacher_subjects.place(x=410, y=200)

        tk.Label(self.subjects_frame, text="Classroom:").place(x=330, y=260)
        self.combobox_classroom_subjects = ttk.Combobox(self.subjects_frame, values=classrooms)
        self.combobox_classroom_subjects.place(x=410, y=260)

        # tk.Label(self.subjects_frame, text="Max. number \n of students:").place(x=320, y=310)
        # self.combobox_numbersofstudents_subjects = ttk.Combobox(self.subjects_frame, values=[])
        # self.combobox_numbersofstudents_subjects.place(x=410, y=320)


#------------------ Botones ----------------------------------
        
        self.button_new_subjects = tk.Button(self.subjects_frame, text="NEW",width=10, command=self.new_subject)
        self.button_new_subjects.place(x=30, y=380)

        self.button_save_subjects = tk.Button(self.subjects_frame, text="SAVE",width=10, command=self.create_subject)
        self.button_save_subjects.place(x=150, y=380)

        self.button_Cancel_subjects = tk.Button(self.subjects_frame, text="CANCEL",width=10, command=self.cancel_subject)
        self.button_Cancel_subjects.place(x=270, y=380)

        self.button_edit_subjects = tk.Button(self.subjects_frame, text="EDIT",width=10, command=self.update_subject)
        self.button_edit_subjects.place(x=390, y=380)
        self.button_edit_subjects.config(state="disabled")

        self.button_drop_subjects = tk.Button(self.subjects_frame, text="DROP",width=10, command=self.drop_subject)
        self.button_drop_subjects.place(x=510, y=380)
        self.button_drop_subjects.config(state="disabled")

        self.user_bottons = [self.button_new_subjects, self.button_save_subjects, self.button_Cancel_subjects, self.button_edit_subjects, self.button_drop_subjects]

#----------------------------Subject Functions--------------------------

    def read_subject(self):
        try:
            self.cancel_subject()
            self.entry_id_subjects.config(state="normal")
            subject_id = self.entry_search_subjects.get()
            if not subject_id:
                messagebox.showerror("Error", "Por favor ingresa un ID a buscar")
                return

            subject, teacher_name, classroom = self.dbSU.read(subject_id)
            if subject:
                if subject[10]:
                    self.entry_id_subjects.insert(0, subject[0])
                    self.entry_name_subjects.insert(0, subject[1])
                    self.entry_credits_subjects.insert(0, subject[2])
                    self.entry_semester_subjects.insert(0, subject[3])
                    self.combobox_degree_subjects.insert(0, subject[4])
                    self.combobox_schedule_subjects.insert(0, subject[5])
                    self.combobox_teacher_subjects.insert(0, teacher_name)
                    self.combobox_classroom_subjects.insert(0, classroom)
                    self.combobox_schedule_subjects.config(state="disabled")
                    self.combobox_teacher_subjects.config(state="disabled")
                    self.combobox_classroom_subjects.config(state="disabled")

                else:
                    messagebox.showerror("Error", "Materia no encontrada")
                    self.new_subject()
            else:
                messagebox.showerror("Error", "Materia no encontrada")
                self.new_subject()
            self.entry_id_subjects.config(state="readonly")
            self.button_save_subjects.config(state="disabled")
            self.button_edit_subjects.config(state="normal")
            self.button_drop_subjects.config(state="normal")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")
            print(e)
        finally:
            self.button_save_subjects.config(state="disabled")

    def new_subject(self):
        try:
            self.entry_id_subjects.config(state="normal")
            self.button_save_subjects.config(state="normal")
            self.combobox_schedule_subjects.config(state="normal")
            self.combobox_teacher_subjects.config(state="normal")
            self.combobox_classroom_subjects.config(state="normal")
            self.entry_id_subjects.delete(0, tk.END)
            self.entry_name_subjects.delete(0, tk.END)
            self.entry_credits_subjects.delete(0, tk.END)
            self.entry_semester_subjects.delete(0, tk.END)
            self.combobox_schedule_subjects.set("")
            self.combobox_degree_subjects.set("")
            self.combobox_teacher_subjects.set("")
            self.combobox_classroom_subjects.set("")
            self.entry_id_subjects.config(state="readonly")
            self.button_save_subjects.config(state="normal")
            self.button_edit_subjects.config(state="disabled")
            self.button_drop_subjects.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occured{e}")


    def cancel_subject(self):
        try:
            self.entry_id_subjects.config(state="normal")
            self.button_save_subjects.config(state="normal")
            self.combobox_schedule_subjects.config(state="normal")
            self.combobox_teacher_subjects.config(state="normal")
            self.combobox_classroom_subjects.config(state="normal")
            self.entry_id_subjects.delete(0, tk.END)
            self.entry_name_subjects.delete(0, tk.END)
            self.entry_credits_subjects.delete(0, tk.END)
            self.entry_semester_subjects.delete(0, tk.END)
            self.combobox_schedule_subjects.set("")
            self.combobox_degree_subjects.set("")
            self.combobox_teacher_subjects.set("")
            self.combobox_classroom_subjects.set("")
            self.entry_id_subjects.config(state="readonly")
            self.button_save_subjects.config(state="normal")
            self.button_edit_subjects.config(state="disabled")
            self.button_drop_subjects.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occured{e}")


    def create_subject(self):
        try:

            self.combobox_schedule_subjects.config(state="normal")
            self.combobox_teacher_subjects.config(state="normal")
            self.combobox_classroom_subjects.config(state="normal")

            subject_id = self.entry_id_subjects.get()
            subject_name = self.entry_name_subjects.get()
            subject_credits = self.entry_credits_subjects.get()
            subject_semester = self.entry_semester_subjects.get()
            subject_schedule = self.combobox_schedule_subjects.get()
            subject_degree = self.combobox_degree_subjects.get()
            subject_teachers_name = self.combobox_teacher_subjects.get()
            subject_classroom_id = self.combobox_classroom_subjects.get()

            if not all([subject_name, subject_credits, subject_semester, subject_schedule, subject_degree, subject_teachers_name, subject_classroom_id]):
                messagebox.showerror("Error","Error, llena todos los campos, son obligatorios")
                return


            subject = Subject(subject_id=subject_id, subject_name = subject_name, subject_credits = subject_credits, subject_semester=subject_semester, subject_schedule=subject_schedule, subject_degree=subject_degree, teacher_id=subject_teachers_name, subject_room=subject_classroom_id)
            self.dbSU.create(subject)

            messagebox.showinfo("Info","Materia registrada de manera exitosa")

            self.combobox_schedule_subjects.config(state="disabled")
            self.combobox_teacher_subjects.config(state="disabled")
            self.combobox_classroom_subjects.config(state="disabled")
            self.cancel_subject()
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")

    def update_subject(self):
        try:
            self.combobox_schedule_subjects.config(state="normal")
            self.combobox_teacher_subjects.config(state="normal")
            self.combobox_classroom_subjects.config(state="normal")

            subject_id = self.entry_id_subjects.get()
            subject_name = self.entry_name_subjects.get()
            subject_credits = self.entry_credits_subjects.get()
            subject_semester = self.entry_semester_subjects.get()
            subject_degree = self.combobox_degree_subjects.get()

            if not subject_id:
                messagebox.showerror("Error","Error por favor busca primero una materia")
                return

            if not all([subject_name, subject_credits, subject_semester, subject_degree]):
                messagebox.showerror("Error", "Error, llena todos los campos, son obligatorios")
                return

            self.dbSU.update(subject_id, subject_name, subject_credits, subject_semester, subject_degree)

            self.combobox_schedule_subjects.config(state="disabled")
            self.combobox_teacher_subjects.config(state="disabled")
            self.combobox_classroom_subjects.config(state="disabled")

            messagebox.showinfo("Info","Materia actualizada con éxito")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occured: {e}")

    def drop_subject(self):
        subject_id = self.entry_id_subjects.get()

        if not subject_id:
            messagebox.showerror("Error, por favor busca primero una materia")
            return

        self.combobox_schedule_subjects.config(state="normal")
        self.combobox_teacher_subjects.config(state="normal")
        self.combobox_classroom_subjects.config(state="normal")



        if messagebox.askyesno("confirmacion", "estas seguro que quieres borrar esta materia?"):
            db_subject = DBsubject()
            db_subject.delete(subject_id)

            messagebox.showinfo("materia", "borrada exitosamente")
        self.cancel_subject()

