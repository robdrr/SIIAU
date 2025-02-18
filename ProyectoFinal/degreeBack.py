from tkinter import messagebox
from TheClass import DB

class DBdegree(DB):
    def create(self, degree):   
        try:
            super().open()  
            self.sql = "INSERT INTO degree (degree_name, degree_semesters) VALUES (%s, %s)"
            self.data = (degree.degree_name, degree.degree_semesters)
            self.cursor1.execute(self.sql, self.data)
            self.conexion.commit()
            super().close()  
            messagebox.showinfo("Éxito", "El grado se ha creado correctamente.")
        except Exception as e:
            print("Error al insertar en la base de datos:", str(e))
            messagebox.showerror("Error", f"Se produjo un error al crear el grado: {str(e)}")

    def read(self, degree_id):
        try:
            super().open()  
            self.sql = "SELECT * FROM degree WHERE degree_id = %s"
            self.cursor1.execute(self.sql, (degree_id,))
            result = self.cursor1.fetchone()
            super().close()  
            return result
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al leer el grado: {str(e)}")
            return None 

    def update(self, degree):
        try:
            super().open()  
            self.sql = "UPDATE degree SET degree_name=%s, degree_semesters=%s WHERE degree_id = %s"
            data = (degree.degree_name, degree.degree_semesters, degree.degree_id)
            self.cursor1.execute(self.sql, data)
            self.conexion.commit()
            super().close()  
            messagebox.showinfo("Éxito", "El grado se ha actualizado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al actualizar el grado: {str(e)}")

    def delete(self, degree_id):
        try:
            super().open()  
            self.sql = "UPDATE degree SET status=FALSE WHERE degree_id = %s"
            self.cursor1.execute(self.sql, (degree_id,))
            self.conexion.commit()
            super().close()  
            messagebox.showinfo("Éxito", "El grado se ha eliminado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al eliminar el grado: {str(e)}")


    def degree_list(self):
        try:
            super().open()
            self.sql = "SELECT degree_name FROM degree WHERE status is TRUE"
            self.cursor1.execute(self.sql)
            degrees = self.cursor1.fetchall()
            return degrees
        except Exception as e:
            print("Error trying to execute the query:", e)
            return None
        finally:
            super().close()

class Degree:
    def __init__(self, degree_id=None, degree_name="", degree_semesters=0):
        self._degree_id = degree_id
        self._degree_name = degree_name
        self._degree_semesters = degree_semesters

    @property
    def degree_id(self):
        return self._degree_id

    @degree_id.setter
    def degree_id(self, value):
        self._degree_id = value

    @property
    def degree_name(self):
        return self._degree_name

    @degree_name.setter
    def degree_name(self, value):
        self._degree_name = value

    @property
    def degree_semesters(self):
        return self._degree_semesters

    @degree_semesters.setter
    def degree_semesters(self, value):
        self._degree_semesters = value
