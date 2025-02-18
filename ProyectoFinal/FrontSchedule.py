from scheduleBack import *
import tkinter as tk
from tkinter import ttk, messagebox

class fSchedule:

    # def updateCombobox_subject(self, event):
    #     try:
    #         select = self.combobox_degree_schedule.get()
    #         subject_name = self.dbSC.comboboxSubject(select)
    #         print(subject_name)
    #     except Exception as e:
    #         messagebox.showerror("Error", f"An error has occurred: {e}")
            

    def schedules_interface(self):
        self.schedule_frame.pack_propagate(0)
        degrees = self.dbSC.comboboxDegree()
        #subjects = self.dbSC.comboboxSubject()

    

        tk.Label(self.schedule_frame, text="Input Group Code:").place(x=100, y=20)
        self.entry_search_schedule = tk.Entry(self.schedule_frame)
        self.entry_search_schedule.place(x=215, y=20)
        self.button_search_schedule = tk.Button(self.schedule_frame, text="Search",width=10, command=self.read_schedule)
        self.button_search_schedule.place(x=355, y=18)

        tk.Label(self.schedule_frame, text="ID Group:").place(x=52, y=80)
        self.entry_id_schedule = tk.Entry(self.schedule_frame, state="readonly")
        self.entry_id_schedule.place(x=120, y=80)

        # tk.Label(self.schedule_frame, text="Shift:").place(x=75, y=140)
        # self.combobox_shift_schedule = ttk.Combobox(self.schedule_frame)
        # self.combobox_shift_schedule.place(x=120, y=140)

        tk.Label(self.schedule_frame, text="Degree:").place(x=62, y=200)
        self.combobox_degree_schedule = ttk.Combobox(self.schedule_frame, values=degrees)
        self.combobox_degree_schedule.place(x=120, y=200)
        #self.combobox_subject_schedule.bind("<<ComboboxSelected>>", self.updateCombobox_subject)

        tk.Label(self.schedule_frame, text="Semester:").place(x=52, y=260)
        self.combobox_semester_schedule = ttk.Combobox(self.schedule_frame, values=["6", "7", "8", "9"])
        self.combobox_semester_schedule.place(x=120, y=260)

        tk.Label(self.schedule_frame, text="Subject:").place(x=60, y=320)
        self.combobox_subject_schedule = ttk.Combobox(self.schedule_frame, values=[])
        self.combobox_subject_schedule.place(x=120, y=320)
        


#------------------ Botones ----------------------------------
        
        self.button_new_schedule = tk.Button(self.schedule_frame, text="NEW",width=10, command=self.new_schedule)
        self.button_new_schedule.place(x=30, y=380)

        self.button_save_schedule = tk.Button(self.schedule_frame, text="SAVE",width=10, command=self.create_schedule)
        self.button_save_schedule.place(x=150, y=380)


        self.button_Cancel_schedule = tk.Button(self.schedule_frame, text="CANCEL",width=10, command=self.cancel_schedule)
        self.button_Cancel_schedule.place(x=270, y=380)

        self.button_edit_schedule = tk.Button(self.schedule_frame, text="EDIT",width=10, command=self.update_schedule)
        self.button_edit_schedule.place(x=390, y=380)
        self.button_edit_schedule.config(state="disabled")

        self.button_drop_schedule = tk.Button(self.schedule_frame, text="DROP",width=10, command=self.drop_schedule)
        self.button_drop_schedule.place(x=510, y=380)
        self.button_drop_schedule.config(state="disabled")

        self.schedule_bottons = [self.button_new_schedule, self.button_save_schedule, self.button_Cancel_schedule, self.button_edit_schedule, self.button_drop_schedule]

#----------------------------Subject Functions--------------------------

    def read_schedule(self):

        try:
            self.entry_id_schedule.config(state="normal")
            subject_id=self.entry_search_schedule.get()
            subject = self.dbSC.read(subject_id)

            if subject:
                if subject[3]:
                    self.combobox_degree_schedule.delete(0, tk.END)
                    self.combobox_semester_schedule.delete(0, tk.END)
                    self.combobox_subject_schedule.delete(0, tk.END)

                    self.entry_id_schedule.insert(0, subject[0])
                    self.combobox_degree_schedule.insert(0, subject[1])
                    self.combobox_semester_schedule.insert(0, subject[2])

                    print(subject)
                else:
                    messagebox.showerror("Error", "Group no longer exist")
            else:
                messagebox.showerror("Error", "Group not found")
            self.entry_id_schedule.config(state="readonly")
            self.button_save_schedule.config(state="normal")
            self.button_drop_schedule.config(state="disabled")

        except Exception as e:
            print(e)

    def new_schedule(self):
        try:
            self.entry_id_schedule.config(state="normal")
            self.entry_id_schedule.delete(0, tk.END)
            self.entry_id_schedule.config(state="readonly")
            self.combobox_degree_schedule.delete(0, tk.END)
            self.combobox_semester_schedule.delete(0, tk.END)
            self.combobox_subject_schedule.delete(0, tk.END)
            self.button_save_schedule.config(state="normal")
            self.button_drop_schedule.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")


    def cancel_schedule(self):
        self.new_schedule()

    def create_schedule(self):
        try:
            self.entry_id_schedule.config(state="normal")
            schedule_id = self.entry_id_schedule.get()
            schedule_degree = self.combobox_degree_schedule.get()
            schedule_semester = self.combobox_semester_schedule.get()
            schedule_subject = self.combobox_subject_schedule.get()

            if not all([schedule_degree, schedule_semester, schedule_subject]):
                messagebox.showerror("Error","Error, llena todos los campos, son obligatorios")
                return


            #schedule = Schedule(schedule_id=schedule_id, schedule_degree= schedule_degree, schedule_semester=schedule_semester, schedule_subject=schedule_subject)
            self.dbSC.create(schedule_id, schedule_subject)

            messagebox.showinfo("Info","Materia registrada de manera exitosa")
            self.entry_id_schedule.config(state="readonly")
            self.new_schedule()
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")


    def update_schedule(self):
        pass

    def drop_schedule(self):
        try:
            self.entry_id_schedule.config(state="normal")
            schedule_id = self.entry_id_schedule.get()
            schedule_degree = self.combobox_degree_schedule.get()
            schedule_semester = self.combobox_semester_schedule.get()
            schedule_subject = self.combobox_subject_schedule.get()

            if not all([schedule_degree, schedule_semester, schedule_subject]):
                messagebox.showerror("Error","Error, llena todos los campos, son obligatorios")
                return


            #schedule = Schedule(schedule_id=schedule_id, schedule_degree= schedule_degree, schedule_semester=schedule_semester, schedule_subject=schedule_subject)
            self.dbSC.delete(schedule_subject)
            messagebox.showinfo("Info", "Materia borrada con éxito")
            #messagebox.showinfo("Info","Materia registrada de manera exitosa")
            self.entry_id_schedule.config(state="readonly")
            self.new_schedule()
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")


        



