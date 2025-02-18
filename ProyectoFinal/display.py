import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

class SubjectViewer:
    def create_widgets_SubjectViewer(self):
        self.SubjectsViewer_frame.pack_propagate(0)
        
        self.label_cohort_id = tk.Label(self.SubjectsViewer_frame, text="Seleccione Cohort ID:")
        self.label_cohort_id.pack()

        self.combobox_cohort_id = ttk.Combobox(self.SubjectsViewer_frame, state="readonly")
        self.combobox_cohort_id.pack()

        self.search_button = tk.Button(self.SubjectsViewer_frame, text="Buscar", command=self.search_subjects)
        self.search_button.pack()

        self.subjects_frame = tk.Frame(self.SubjectsViewer_frame)
        self.subjects_frame.pack()

        self.create_weekday_table()

        self.populate_combobox()

    
    def populate_combobox(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="siiau"
            )
            self.cursor = self.conn.cursor()

            # Consulta para obtener el username del usuario con el login_id más alto
            self.cursor.execute("SELECT users.user_username FROM users JOIN login ON users.user_username = login.username ORDER BY login.login_id DESC LIMIT 1")
            current_username = self.cursor.fetchone()[0]

            # Consulta para obtener el rol del usuario
            self.cursor.execute("SELECT user_role FROM users WHERE user_username = %s", (current_username,))
            user_role = self.cursor.fetchone()[0]

            # Si el usuario es 'Admin', mantener la consulta original
            if user_role == "Admin":
                self.cursor.execute("SELECT DISTINCT cohort_id FROM subjects")
            # Si el usuario es 'Student', obtener los cohort_id relacionados con el usuario actual
            elif user_role == "Student":
                # Consulta para obtener cohort_id relacionados con el usuario actual
                self.cursor.execute("SELECT DISTINCT cohort_id FROM students WHERE user_id = (SELECT user_id FROM users WHERE user_username = %s)", (current_username,))
            else:
                # Manejar cualquier otro caso de rol de usuario
                messagebox.showerror("Error", "Rol de usuario desconocido.")
                return

            cohort_ids = self.cursor.fetchall()

            self.combobox_cohort_id["values"] = [cohort_id[0] for cohort_id in cohort_ids]

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error al conectar a la base de datos: {e}")

    def create_weekday_table(self):
        self.weekday_table = ttk.Treeview(self.subjects_frame, style="Custom.Treeview")
        self.weekday_table["columns"] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")


        self.weekday_table.heading("Monday", text="Monday")
        self.weekday_table.heading("Tuesday", text="Tuesday")
        self.weekday_table.heading("Wednesday", text="Wednesday")
        self.weekday_table.heading("Thursday", text="Thursday")
        self.weekday_table.heading("Friday", text="Friday")

        self.weekday_table.tag_configure("oddrow", background="lightgray")
        self.weekday_table.tag_configure("evenrow", background="white")
        self.weekday_table.configure(yscrollcommand=lambda f, l: self.autoscroll(self.weekday_table, f, l))

        self.weekday_table.bind("<ButtonRelease-1>", self.show_subject_details)
        self.weekday_table.pack()

    def search_subjects(self):
        cohort_id = self.combobox_cohort_id.get()
        if not cohort_id:
            messagebox.showwarning("Advertencia", "Por favor seleccione un Cohort ID.")
            return

        self.show_subjects(cohort_id)

    def show_subjects(self, cohort_id):

        self.weekday_table.delete(*self.weekday_table.get_children())

        self.cursor.execute("SELECT * FROM subjects WHERE cohort_id = %s ORDER BY FIELD(subject_schedule, 'L | 07:00 - 09:00', 'L | 09:00 - 11:00', 'L | 11:00 - 13:00', 'M | 07:00 - 09:00', 'M | 09:00 - 11:00', 'M | 11:00 - 13:00', 'I | 07:00 - 09:00', 'I | 09:00 - 11:00', 'I | 11:00 - 13:00', 'J | 07:00 - 09:00', 'J | 09:00 - 11:00', 'J | 11:00 - 13:00', 'V | 07:00 - 09:00', 'V | 09:00 - 11:00', 'V | 11:00 - 13:00')", (cohort_id,))
        subjects = self.cursor.fetchall()


        day_mapping = {
            "L": "Monday",
            "M": "Tuesday",
            "I": "Wednesday",
            "J": "Thursday",
            "V": "Friday"
        }

        for i, subject in enumerate(subjects):
            
            day = subject[5][0]  
            full_day = day_mapping.get(day)  
            if full_day is None:
                messagebox.showerror("Error", f"Invalid day abbreviation found: {day}")
                continue

            day_column_index = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"].index(full_day)
    
            unique_iid = f"{cohort_id}_{subject[0]}"
        
            if i % 2 == 0:
                self.weekday_table.insert("", "end", values=("",)*day_column_index + (subject[1],) + ("",)*(4-day_column_index), iid=unique_iid, tags=("evenrow",))
            else:
                self.weekday_table.insert("", "end", values=("",)*day_column_index + (subject[1],) + ("",)*(4-day_column_index), iid=unique_iid, tags=("oddrow",))

    def show_subject_details(self, event):
        item = self.weekday_table.selection()[0]
        values = self.weekday_table.item(item, "values")
        subject_id = item.split("_")[1]  
        self.cursor.execute("SELECT * FROM subjects WHERE subject_id = %s", (subject_id,))
        subject_details = self.cursor.fetchone()
        messagebox.showinfo("Subject Details", f"Subject ID: {subject_details[0]}\nSubject Name: {subject_details[1]}\nSubject Credit: {subject_details[2]}\nSubject Semester: {subject_details[3]}\nSubject Degree: {subject_details[4]}\nSubject Schedule: {subject_details[5]}\nRoom ID: {subject_details[6]}\nSubject Student Max: {subject_details[7]}\nAvailable: {subject_details[8]}\nCohort ID: {subject_details[9]}")

    def __del__(self):
        try:
            self.conn.close()
        except:
            pass

    def autoscroll(self, tree, first, last):
        tree.yview_moveto(1)
        self.after(100, lambda: self.autoscroll(tree, first, last))


