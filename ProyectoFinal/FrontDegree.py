from degreeBack import *
import tkinter as tk
from tkinter import ttk

class fDegree:
    def degrees_interface(self):
        self.degree_frame.pack_propagate(0)

        tk.Label(self.degree_frame, text="Input degree Code:").place(x=85, y=20)
        self.entry_search_degree = tk.Entry(self.degree_frame)
        self.entry_search_degree.place(x=215, y=20)
        self.button_search_degree = tk.Button(self.degree_frame, text="Search",width=10, command=self.read_degree)
        self.button_search_degree.place(x=355, y=18)

        tk.Label(self.degree_frame, text="ID:").place(x=88, y=80)
        self.entry_id_degree = tk.Entry(self.degree_frame, state="readonly")
        self.entry_id_degree.place(x=120, y=80)

        tk.Label(self.degree_frame, text="Degree:").place(x=60, y=160)
        self.entry_degree_degree = tk.Entry(self.degree_frame)
        self.entry_degree_degree.place(x=120, y=160)

        tk.Label(self.degree_frame, text="Semesters:").place(x=45, y=240)
        self.combobox_semester_degree = ttk.Combobox(self.degree_frame, values=["6", "7", "8", "9"])
        self.combobox_semester_degree.place(x=120, y=240)

        # tk.Label(self.degree_frame, text="Subjects:").place(x=55, y=320)
        # self.combobox_subjects_degree = ttk.Combobox(self.degree_frame, values=[])
        # self.combobox_subjects_degree.place(x=120, y=320)

#------------------ Botones ----------------------------------
        
        self.button_new_degree = tk.Button(self.degree_frame, text="NEW",width=10, command=self.new_degree)
        self.button_new_degree.place(x=30, y=380)

        self.button_save_degree = tk.Button(self.degree_frame, text="SAVE",width=10, command=self.create_degree)
        self.button_save_degree.place(x=150, y=380)

        self.button_Cancel_degree = tk.Button(self.degree_frame, text="CANCEL",width=10, command=self.cancel_degree)
        self.button_Cancel_degree.place(x=270, y=380)

        self.button_edit_degree = tk.Button(self.degree_frame, text="EDIT",width=10, command=self.update_degree)
        self.button_edit_degree.place(x=390, y=380)
        self.button_edit_degree.config(state="disabled")

        self.button_drop_degree = tk.Button(self.degree_frame, text="DROP",width=10, command=self.drop_degree)
        self.button_drop_degree.place(x=510, y=380)
        self.button_drop_degree.config(state="disabled")
        self.degree_bottons = [self.button_new_degree, self.button_save_degree, self.button_Cancel_degree, self.button_edit_degree, self.button_drop_degree]

#----------------------------Subject Functions--------------------------

    def read_degree(self):
        try:
            # Obtener el código del grado desde la entrada
            degree_id = self.entry_search_degree.get()
            
            # Validar que el código no esté vacío
            if degree_id.strip() == "":
                messagebox.showerror("Error", "Ingrese un código de grado válido.")
                return
            
            # Intentar leer el grado desde la base de datos
            degree_db = DBdegree()
            degree_data = degree_db.read(degree_id)
            
            # Si se encontró el grado, cargar los datos en los campos de entrada
            if degree_data:
                if degree_data[3]:

                    self.entry_id_degree.config(state="normal")
                    self.entry_id_degree.delete(0, tk.END)
                    self.entry_id_degree.insert(0, degree_data[0])
                    self.entry_id_degree.config(state="readonly")
                    
                    self.entry_degree_degree.delete(0, tk.END)
                    self.entry_degree_degree.insert(0, degree_data[1])
                    
                    self.combobox_semester_degree.set(str(degree_data[2]))
                
            else:
                messagebox.showerror("Error", "No se encontró ningún grado con ese código.")
            self.button_save_degree.config(state="disabled")
            self.button_edit_degree.config(state="normal")
            self.button_drop_degree.config(state="normal")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occuerred: {e}")


    def new_degree(self):
        try:
            # Limpiar los campos de entrada para agregar un nuevo grado
            self.entry_id_degree.config(state="normal")
            self.entry_id_degree.delete(0, tk.END)
            self.entry_id_degree.config(state="readonly")
            
            self.entry_degree_degree.delete(0, tk.END)
            self.combobox_semester_degree.set("")
            self.button_save_degree.config(state="normal")
            self.button_edit_degree.config(state="disabled")
            self.button_drop_degree.config(state="disabled")


        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")


    def cancel_degree(self):
        try:
            # Limpiar los campos de entrada para agregar un nuevo grado
            self.entry_id_degree.config(state="normal")
            self.entry_id_degree.delete(0, tk.END)
            self.entry_id_degree.config(state="readonly")
            
            self.entry_degree_degree.delete(0, tk.END)
            self.combobox_semester_degree.set("")
            self.button_save_degree.config(state="normal")
            self.button_edit_degree.config(state="disabled")
            self.button_drop_degree.config(state="disabled")

        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")
        
    def create_degree(self):
        try:
            # Obtener los datos del grado desde los campos de entrada
            degree_name = self.entry_degree_degree.get()
            semester = self.combobox_semester_degree.get()
            
            # Validar que los campos no estén vacíos
            if degree_name.strip() == "" or semester.strip() == "":
                messagebox.showerror("Error", "Por favor complete todos los campos.")
                return
            
            try:
                # Crear un objeto Degree con los datos ingresados
                degree = Degree(degree_name=degree_name, degree_semesters=int(semester))
                
                # Crear el grado en la base de datos
                degree_db = DBdegree()
                degree_db.create(degree)
                
                # Limpiar los campos después de la creación exitosa
                self.cancel_degree()
            except ValueError:
                messagebox.showerror("Error", "Ingrese un número válido para los semestres.")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")


    def update_degree(self):
        try:
            # Obtener los datos del grado desde los campos de entrada
            degree_id = self.entry_id_degree.get()
            degree_name = self.entry_degree_degree.get()
            semester = self.combobox_semester_degree.get()
            
            # Validar que el campo ID no esté vacío
            if degree_id.strip() == "":
                messagebox.showerror("Error", "Primero busque un grado para actualizar.")
                return
            
            # Validar que los campos no estén vacíos
            if degree_name.strip() == "" or semester.strip() == "":
                messagebox.showerror("Error", "Por favor complete todos los campos.")
                return
            
            try:
                # Crear un objeto Degree con los datos ingresados
                degree = Degree(degree_id=int(degree_id), degree_name=degree_name, degree_semesters=int(semester))
                
                # Actualizar el grado en la base de datos
                degree_db = DBdegree()
                degree_db.update(degree)
            except ValueError:
                messagebox.showerror("Error", "Ingrese un número válido para los semestres.")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")

    def drop_degree(self):
        try:
            # Obtener el código del grado desde la entrada
            degree_id = self.entry_id_degree.get()
            
            # Validar que el campo ID no esté vacío
            if degree_id.strip() == "":
                messagebox.showerror("Error", "Primero busque un grado para eliminar.")
                return
            
            # Confirmar la eliminación del grado
            confirmation = messagebox.askyesno("Confirmación", "¿Estás seguro que deseas eliminar este grado?")
            
            if confirmation:
                # Eliminar el grado de la base de datos
                degree_db = DBdegree()
                degree_db.delete(degree_id)
                
                # Limpiar los campos después de la eliminación exitosa
                self.cancel_degree()
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")

        




