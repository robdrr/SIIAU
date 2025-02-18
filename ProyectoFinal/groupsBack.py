from TheClass import *
from tkinter import ttk, messagebox


class DBgroups(DB):
    def create(self, group):
        self.mysql = "INSERT INTO cohorts (cohort_id, cohort_name, cohort_date, cohort_degree, cohort_semester, cohort_max) VALUES (%s, %s, %s, %s, %s, %s)"
        self.data = group.cohort_id, group.cohort_name, group.cohort_date, group.cohort_degree, group.cohort_semester, group.cohort_max
        try:
            super().open()
            self.cursor1.execute(self.mysql, self.data)
            self.conexion.commit()
            print("Grupo creado exitosamente.")
        except Exception as error:
            print(error)
        finally:
            super().close()


    def read(self, cohort_id):
        self.mysql = "SELECT * FROM cohorts WHERE cohort_id = %s AND status = TRUE"
        try:
            self.open()
            self.cursor1.execute(self.mysql, (cohort_id,))  # Ensure this is a tuple
            result = self.cursor1.fetchone()
        except Exception as error:
            print(f"Database error: {error}")
            return None
        finally:
            self.close()
        return result

    
    def update (self, cohort_id, cohort_name, cohort_date, cohort_degree, cohort_semester, cohort_max):
        
        super().open()
        self.mysql = "UPDATE cohorts SET cohort_name =%s, cohort_date = %s, cohort_degree = %s, cohort_semester = %s, cohort_max = %s WHERE cohort_id = %s"
        self.cursor1.execute(self.mysql, (cohort_name, cohort_date, cohort_degree, cohort_semester, cohort_max, cohort_id))
        self.conexion.commit()
        super().close()

    def delete(self, cohort_id):
        try:
            super().open()  
            self.sql = "UPDATE cohorts SET status = FALSE WHERE cohort_id = %d" % cohort_id
            self.cursor1.execute(self.sql)
            self.conexion.commit()
            super().close()  
            messagebox.showinfo("Éxito", "El grupo se ha eliminado correctamente.")
        except Exception as error:
            messagebox.showerror("Error", f"Se produjo un error al eliminar el grupo: {str(error)}")
    
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
    


    def read_all(self):
        self.mysql = "SELECT * FROM cohorts WHERE status = TRUE"  # Assuming there is a 'status' column to filter active cohorts
        try:
            super().open()
            self.cursor1.execute(self.mysql)
            result = self.cursor1.fetchall()
            return result
        except Exception as error:
            print(f"Error fetching all cohorts: {error}")
            return []
        finally:
            super().close()


class Groups:
    def __init__(self, cohort_id = None, cohort_name='', cohort_date='', cohort_degree='',
                cohort_semester='', cohort_max=''):
        self.cohort_id = cohort_id
        self.cohort_name = cohort_name
        self.cohort_date = cohort_date
        self.cohort_degree = cohort_degree

        self.cohort_semester = cohort_semester
        self.cohort_max = cohort_max

    @property
    def cohort_id(self):
        return self._cohort_id

    @cohort_id.setter
    def cohort_id(self, value):
        self._cohort_id = value

    @property
    def cohort_name(self):
        return self._cohort_name

    @cohort_name.setter
    def cohort_name(self, value):
        self._cohort_name = value

    @property
    def cohort_date(self):
        return self._cohort_date

    @cohort_date.setter
    def cohort_date(self, value):
        self._cohort_date = value

    @property
    def cohort_degree(self):
        return self._cohort_degree

    @cohort_degree.setter
    def cohort_degree(self, value):
        self._cohort_degree = value


    @property
    def cohort_semester(self):
        return self._cohort_semester

    @cohort_semester.setter
    def cohort_semester(self, value):
        self._cohort_semester = value

    @property
    def cohort_max(self):
        return self._cohort_max

    @cohort_max.setter
    def cohort_max(self, value):
        self._cohort_max = value



# | cohorts | CREATE TABLE `cohorts` (
#   `cohort_id` int NOT NULL AUTO_INCREMENT,
#   `cohort_name` varchar(50) DEFAULT NULL,
#   `cohort_date` date DEFAULT NULL,
#   `cohort_degree` varchar(50) DEFAULT NULL,
#   `cohort_semester` varchar(50) DEFAULT NULL,
#   `cohort_max` int DEFAULT NULL,
#   PRIMARY KEY (`cohort_id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |

# mysql> CREATE TABLE subject_cohorts (
#     ->     relation_id INT AUTO_INCREMENT PRIMARY KEY,
#     ->     cohort_id INT,
#     ->     subject_id INT,
#     ->     FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
#     ->     FOREIGN KEY (cohort_id) REFERENCES COHORTS(cohort_id)
#     -> );
# Query OK, 0 rows affected (0.10 sec)