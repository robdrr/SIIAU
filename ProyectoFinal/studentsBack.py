from TheClass import *
from tkinter import ttk, messagebox

class DBstudents(DB):
    # def check_cohort(self, cohort_id):
    #     try:
    #         super().open()
    #         query = f"SELECT cohort_max FROM cohorts WHERE cohort_id = {cohort_id}"
    #         self.cursor1.execute(query)
    #         result = self.cursor1.fetchone()
    #         super().close()
    #         return result[0] > 0 if result else False
    #     except Exception as e:
    #         messagebox.showerror("Error", f"Error al verificar la disponibilidad del cohort: {str(e)}")
    #         return False
        

    
    def create(self, student):
        try:
            super().open()
            self.sql = "INSERT INTO students (user_id, student_state, student_birthday, student_degree, cohort_id) VALUES (%s, %s, %s, %s, %s)"
            self.data = (student.user_id, student.student_state, student.student_birthday, student.student_degree, student.cohort_id)
            self.cursor1.execute(self.sql, self.data)
            self.conexion.commit()

            # Update cohort_max - 1
            query = f"UPDATE cohorts SET cohort_max = cohort_max - 1 WHERE cohort_id = {student.cohort_id}"
            self.cursor1.execute(query)
            self.conexion.commit()

            super().close()
            messagebox.showinfo("Éxito", "El estudiante se ha creado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al crear al estudiante: {str(e)}")


    def read(self, student_id):
        try:
            super().open() 

            # Consulta para obtener los datos del estudiante
            self.sql = "SELECT * FROM students WHERE student_id = %s"
            self.cursor1.execute(self.sql, (student_id,))
            result = self.cursor1.fetchone()

            # Consulta para obtener los datos del usuario asociado al estudiante
            self.sql1 = "SELECT * FROM users AS u JOIN students AS s ON u.user_id = s.user_id WHERE s.student_id = %s"
            self.cursor2.execute(self.sql1, (student_id,))
            result1 = self.cursor2.fetchone()

            super().close()  
            return result, result1
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al leer el estudiante: {str(e)}")
            return None, None
        
    
    def update(self, student_id, student_degree, student_subject, student_state, student_birthday, cohort_id):
        try:
            super().open() 
            # Obtener el cohort_id anterior del estudiante
            self.sql_prev_cohort = "SELECT cohort_id FROM students WHERE student_id = %s"
            self.cursor1.execute(self.sql_prev_cohort, (student_id,))
            prev_cohort_id = self.cursor1.fetchone()[0]

            # Actualizar el estudiante con el nuevo cohort_id
            self.sql_update_student = "UPDATE students SET student_degree=%s, student_subject=%s, student_state=%s, student_birthday=%s, cohort_id=%s WHERE student_id=%s"
            self.data_update_student = (student_degree, student_subject, student_state, student_birthday, cohort_id, student_id)
            self.cursor1.execute(self.sql_update_student, self.data_update_student)

            # Incrementar el cohort_max del cohort_id anterior
            self.sql_inc_prev_cohort_max = "UPDATE cohorts SET cohort_max = cohort_max + 1 WHERE cohort_id = %s"
            self.cursor1.execute(self.sql_inc_prev_cohort_max, (prev_cohort_id,))

            # Decrementar el cohort_max del nuevo cohort_id
            self.sql_dec_new_cohort_max = "UPDATE cohorts SET cohort_max = cohort_max - 1 WHERE cohort_id = %s"
            self.cursor1.execute(self.sql_dec_new_cohort_max, (cohort_id,))

            self.conexion.commit()
            super().close()  
            messagebox.showinfo("Éxito", "Los datos del estudiante se han actualizado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al actualizar los datos del estudiante: {str(e)}")


    def delete(self, student_id):
        try:
            super().open() 
            #Its necessary to add that the space of the person who deleted themselves be returned to their group"
            self.sql = "UPDATE students SET status = FALSE WHERE student_id = %s"
            self.cursor1.execute(self.sql, (student_id,))
            self.conexion.commit()
            super().close()  
            messagebox.showinfo("Éxito", "El estudiante se ha eliminado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al eliminar al estudiante: {str(e)}")


    def comboboxCohorts(self):
        super().open()
        self.sql = "select cohort_id FROM cohorts WHERE status = TRUE AND cohort_max >0"
        self.cursor1.execute(self.sql)
        result = self.cursor1.fetchall()
        super().close()
        return result
    
    def comboboxDegree(self):
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
    
 
class Students:
    def __init__(self, student_id=None, user_id=None, student_degree="", student_subject="", student_state="", student_birthday=None, cohort_id=""):
        self.student_id = student_id
        self.user_id = user_id
        self.student_degree = student_degree
        self.student_subject = student_subject
        self.student_state = student_state
        self.student_birthday = student_birthday
        self._cohort_id = cohort_id

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def student_degree(self):
        return self._student_degree

    @student_degree.setter
    def student_degree(self, value):
        self._student_degree = value

    @property
    def student_subject(self):
        return self._student_subject

    @student_subject.setter
    def student_subject(self, value):
        self._student_subject = value

    @property
    def student_state(self):
        return self._student_state

    @student_state.setter
    def student_state(self, value):
        self._student_state = value

    @property
    def student_birthday(self):
        return self._student_birthday

    @student_birthday.setter
    def student_birthday(self, value):
        self._student_birthday = value

    @property
    def cohort_id(self):
        return self._cohort_id

    @cohort_id.setter
    def cohort_id(self, value):
        self._cohort_id = value
    




# | students | CREATE TABLE `students` (
#   `student_id` int NOT NULL AUTO_INCREMENT,
#   `user_id` int DEFAULT NULL,
#   `student_state` varchar(50) DEFAULT NULL,
#   `student_birthday` date DEFAULT NULL,
#   `student_degree` varchar(50) DEFAULT NULL,
#   `status` tinyint(1) DEFAULT '1',
#   `cohort_id` int DEFAULT NULL,
#   PRIMARY KEY (`student_id`),
#   UNIQUE KEY `unique_user_id` (`user_id`),
#   KEY `cohort_id_index` (`cohort_id`),
#   CONSTRAINT `fk_cohort_id` FOREIGN KEY (`cohort_id`) REFERENCES `cohorts` (`cohort_id`),
#   CONSTRAINT `students_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)