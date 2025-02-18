import tkinter as tk

from tkinter import messagebox, ttk



# from studentsBack import *
# from usersBack import *
# from studentsBack import *
# from subjectBack import *
# from groupsBack import *
# from teachersBack import *

from Frontlogin import *
from FrontUsers import *
from FrontStudent import *
from FrontTeacher import *
from FrontSubject import *
from FrontGroup import *
from FrontSchedule import *
from FrontClassroom import *
from FrontDegree import *
from display import *




loginmain = None


##########################################################################################

class MainPage(tk.Toplevel, fUser, fStudent, fSubject, fTeacher, fGroup, fSchedule, fClassroom, fDegree, SubjectViewer):
    def __init__(self, master=None):
        super().__init__(master)


        self.title("Main Page")
        self.notebook=ttk.Notebook(self)
        self.notebook.bind("<<NotebookTabChanged>>", lambda event: self.quit() if self.notebook.index(self.notebook.select()) == 9 else None)
        #NOTE: make sure to change the index number whenever a new frame is added.


        self.users_frame=tk.Frame(self.notebook, width=300, height=300)
        self.students_frame=tk.Frame(self.notebook, width=300, height=300)
        self.teachers_frame=tk.Frame(self.notebook, width=300, height=300)
        self.subjects_frame=tk.Frame(self.notebook, width=300, height=300)
        self.groups_frame=tk.Frame(self.notebook, width=300, height=300)
        self.schedule_frame=tk.Frame(self.notebook, width=300, height=300)
        self.classroom_frame=tk.Frame(self.notebook, width=300, height=300)
        self.degree_frame=tk.Frame(self.notebook, width=300, height=300)
        self.SubjectsViewer_frame=tk.Frame(self.notebook, width=300,height=300)
        self.exit_frame=tk.Frame(self.notebook, width=300, height=300)
        
        
        self.notebook.add(self.users_frame, text="Users")
        self.notebook.add(self.students_frame, text="Students")
        self.notebook.add(self.teachers_frame, text="Teachers")
        self.notebook.add(self.subjects_frame, text="Subjects")
        self.notebook.add(self.groups_frame, text="Groups")
        self.notebook.add(self.schedule_frame, text="Schedule")
        self.notebook.add(self.classroom_frame, text="Classroom")
        self.notebook.add(self.degree_frame, text="Degree")
        self.notebook.add(self.SubjectsViewer_frame, text="Display")
        self.notebook.add(self.exit_frame, text="Exit")


        self.notebook.pack(expand=1, fill="both")
        self.geometry("1280x720")
        self.dbU=DBuser()
        self.dbS=DBstudents()
        self.dbR= DBroom()
        self.dbD = DBdegree()
        self.dbT= DBteacher()
        self.dbSU= DBsubject()
        self.dbG = DBgroups()
        self.dbSC = DBschedule()


        self.combobox_degree_subjects = ttk.Combobox(self.subjects_frame, values=[])
        self.combobox_teacher_subjects = ttk.Combobox(self.subjects_frame, values=[])
        self.combobox_classroom_subjects = ttk.Combobox(self.subjects_frame, values=[])



        if loginmain[7] == "Admin":
            self.users_interface()
            self.subjects_interface()
            self.students_interface()
            self.groups_interface()
            self.schedules_interface()
            self.classrooms_interface()
            self.degrees_interface()
            self.create_widgets_SubjectViewer()
        
        elif loginmain[7] == "Student":
            self.students_interface()
            self.create_widgets_SubjectViewer()

        elif loginmain[7] == "Teacher":
            self.teachers_interface()


class LoginPage(Claselogin):

    def login(self, event=None):
        try:
            global loginmain
            username = self.entry_username_login.get()
            password = self.entry_password_login.get()

            lgn = self.db.login(username, password)
            loginmain = lgn


            print(lgn)
            if lgn is not None:
                messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
                self.db1.logindb(username)
                self.open_main_window()
            else:
                self.label_unsucces_login = CTkLabel(master=self.frame_ml, text="The Username/password is incorrect", font=('Century Gothic', 12))
                self.label_unsucces_login.place(x=50,y=195)
        except Exception as e:
            print(e)
            messagebox.showerror("Error", f"An error ocurred: {e}")

    def open_main_window(self):
        self.root.withdraw()
        self.main_page = MainPage(self.root)


if __name__ == "__main__":
    set_appearance_mode("System")  # Modes: system (default), light, dark
    set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

    root = CTk()
    login_page = LoginPage(root)
    root.mainloop()