import tkinter as tk
from tkinter import messagebox, Menu, ttk
from usersBack import *
from tkcalendar import DateEntry
from groupsBack import *
from datetime import date

class fGroup:
    def groups_interface(self):

        # def updateCombobox(self, event):
        #     try:


        self.groups_frame.pack_propagate(0)
        degrees = self.dbG.comboboxDegree()

        tk.Label(self.groups_frame, text="Input Group Code:").place(x=100, y=20)
        self.entry_search_groups = tk.Entry(self.groups_frame)
        self.entry_search_groups.place(x=215, y=20)
        self.button_search_groups = tk.Button(self.groups_frame, text="Search",width=10, command=self.read_group)
        self.button_search_groups.place(x=355, y=18)

        tk.Label(self.groups_frame, text="ID:").place(x=88, y=80)
        self.entry_id_groups = tk.Entry(self.groups_frame, state="readonly")
        self.entry_id_groups.place(x=120, y=80)

        tk.Label(self.groups_frame, text="Group Name:").place(x=33, y=130)
        self.entry_groupname_groups = tk.Entry(self.groups_frame)
        self.entry_groupname_groups.place(x=120, y=130)

        tk.Label(self.groups_frame, text="Date:").place(x=75, y=180)
        self.date_entry_date_groups = DateEntry(self.groups_frame)
        self.date_entry_date_groups.place(x=120, y=180)

        
        tk.Label(self.groups_frame, text="Degree:").place(x=65, y=230)
        self.combobox_degree_groups = ttk.Combobox(self.groups_frame, values=degrees)
        self.combobox_degree_groups.place(x=120, y=230)

        # tk.Label(self.groups_frame, text="Subject:").place(x=65, y=240)
        # self.combobox_subject_groups = ttk.Combobox(self.groups_frame, values=[])
        # self.combobox_subject_groups.place(x=120, y=240)

        # tk.Label(self.groups_frame, text="Teacher:").place(x=65, y=280)
        # self.combobox_teacher_groups = ttk.Combobox(self.groups_frame, values=[])
        # self.combobox_teacher_groups.place(x=120, y=280)

        # tk.Label(self.groups_frame, text="Classroom:").place(x=338, y=140)
        # self.combobox_classroom_groups = ttk.Combobox(self.groups_frame, values=[])
        # self.combobox_classroom_groups.place(x=410, y=140)

        # tk.Label(self.groups_frame, text="Schedule:").place(x=345, y=180)
        # self.combobox_schedule_groups = ttk.Combobox(self.groups_frame, values=[])
        # self.combobox_schedule_groups.place(x=410, y=180)

        tk.Label(self.groups_frame, text="Semester:").place(x=55, y=280)
        self.combobox_semester_groups = ttk.Combobox(self.groups_frame, values=["2024A", "2023B", "2023A"])
        self.combobox_semester_groups.place(x=120, y=280)

        tk.Label(self.groups_frame, text="Max. number \n of students:").place(x=324, y=255)
        self.combobox_number_groups = ttk.Combobox(self.groups_frame, values=["15", "20", "25", "30"])
        self.combobox_number_groups.place(x=410, y=260)


#------------------ Botones ----------------------------------
        
        self.button_new_groups = tk.Button(self.groups_frame, text="NEW",width=10, command=self.new_group)
        self.button_new_groups.place(x=30, y=380)

        self.button_save_groups = tk.Button(self.groups_frame, text="SAVE",width=10, command=self.create_group)
        self.button_save_groups.place(x=150, y=380)

        self.button_Cancel_groups = tk.Button(self.groups_frame, text="CANCEL",width=10, command=self.cancel_group)
        self.button_Cancel_groups.place(x=270, y=380)

        self.button_edit_groups = tk.Button(self.groups_frame, text="EDIT",width=10, command=self.update_group)
        self.button_edit_groups.place(x=390, y=380)
        self.button_edit_groups.config(state="disabled")

        self.button_drop_groups = tk.Button(self.groups_frame, text="DROP",width=10, command=self.drop_group)
        self.button_drop_groups.place(x=510, y=380)
        self.button_drop_groups.config(state="disabled")
        
        self.group_bottons = [self.button_new_groups, self.button_save_groups, self.button_Cancel_groups, self.button_edit_groups, self.button_drop_groups]

#----------------------------Subject Functions--------------------------


    def read_group(self):
        try:
            cohort_id = self.entry_search_groups.get()
            dbG = DBgroups()
            group = dbG.read(cohort_id)
            if group:
                if group[6]:
                    self.entry_id_groups.config(state="normal")
                    self.entry_id_groups.delete(0, tk.END)
                    self.entry_id_groups.insert(0, group[0])
                    self.entry_id_groups.config(state="readonly")

                    self.entry_groupname_groups.delete(0, tk.END)
                    self.entry_groupname_groups.insert(0, group[1])

                    try:
                        self.date_entry_date_groups.set_date(group[2])
                    except ValueError:
                        self.date_entry_date_groups.set_date(date.today())

                    self.combobox_degree_groups.set(group[3])
                    self.combobox_semester_groups.set(group[4])
                    self.combobox_number_groups.set(str(group[5]))
                else:
                    messagebox.showerror("Error", f"An error has occurred: {e}")
            else:
                messagebox.showinfo("Error", "Group not found")
            self.button_save_groups.config(state="disabled")
            self.button_edit_groups.config(state="normal")
            self.button_drop_groups.config(state="normal")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")


    def new_group(self):
        try:
            self.entry_search_groups.delete(0, tk.END)
            self.entry_id_groups.config(state="normal")
            self.entry_id_groups.delete(0, tk.END)
            self.entry_id_groups.config(state="readonly")
            self.entry_groupname_groups.delete(0, tk.END)
            self.date_entry_date_groups.set_date(date.today())  # Set to today's date
            self.combobox_degree_groups.set('')
            self.combobox_semester_groups.set('')
            self.combobox_number_groups.set('')
            self.button_save_groups.config(state="normal")
            self.button_edit_groups.config(state="disabled")
            self.button_drop_groups.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")
    def cancel_group(self):
        self.new_group()  # Reuse new_group function to clear all fields


    def create_group(self):
        try:
            cohort_name = self.entry_groupname_groups.get()
            cohort_date = self.date_entry_date_groups.get_date()
            cohort_degree = self.combobox_degree_groups.get()
            cohort_semester = self.combobox_semester_groups.get()
            cohort_max = int(self.combobox_number_groups.get())

            new_group = Groups(
                cohort_name=cohort_name,
                cohort_date=cohort_date,
                cohort_degree=cohort_degree,
                cohort_semester=cohort_semester,
                cohort_max=cohort_max
            )
            dbG = DBgroups()
            dbG.create(new_group)
            messagebox.showinfo("Success", "Group created successfully")
            self.new_group()
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")


    def update_group(self):
        try:
            cohort_id = self.entry_id_groups.get()
            cohort_name = self.entry_groupname_groups.get()
            cohort_date = self.date_entry_date_groups.get_date()
            cohort_degree = self.combobox_degree_groups.get()
            cohort_semester = self.combobox_semester_groups.get()
            cohort_max = self.combobox_number_groups.get()
            
            # if DBgroups().update(cohort_id, cohort_name, cohort_date, cohort_degree, cohort_semester, cohort_max):
            #     messagebox.showinfo("Success", "Group updated successfully")
            # else:
            #     messagebox.showinfo("Error", "Failed to update group")

            self.dbG.update(cohort_id, cohort_name, cohort_date, cohort_degree, cohort_semester, cohort_max)
            messagebox.showinfo("Success", "Group updated successfully")

        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")


    def drop_group(self):
        dbG = DBgroups()
        try:
            cohort_id = int(self.entry_search_groups.get())  # Convertir a int
            self.dbG.delete(cohort_id)  # Llamar al método delete con el user_id
            self.entry_search_groups.delete(0, tk.END)
            self.entry_id_groups.delete(0, tk.END)
            self.entry_groupname_groups.delete(0, tk.END)
            self.combobox_degree_groups.delete(0, tk.END)
            self.combobox_semester_groups.delete(0, tk.END)
            self.combobox_number_groups.delete(0, tk.END)
            messagebox.showinfo("Éxito", "El grupo se ha eliminado correctamente.")
            self.new_group()

        except  Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al eliminar el usuario: {str(e)}")

