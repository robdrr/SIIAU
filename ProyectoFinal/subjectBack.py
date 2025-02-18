from TheClass import *
from tkinter import messagebox



#agragar la logica al update o no actualizar esas cosas

class DBsubject(DB):

    
    def check_teacher_schedule_conflict(self, teacher_id, new_schedule):
        super().open()
        # Query to check for schedule conflicts
        # self.cursor1.execute("SELECT * FROM teachers t JOIN teachers_subjects ts ON t.teacher_id = ts.teacher_id JOIN subjects s ON ts.subject_id = s.subject_id WHERE t.teacher_schedule = s.subject_schedule AND t.teacher_id = %s")
        self.cursor1.execute("SELECT teacher_schedule FROM teachers WHERE teacher_id = %s ", teacher_id)
        current_schedules = self.cursor1.fetchall()
        # Itera sobre los horarios actuales y compara con el nuevo horario
        for schedule in current_schedules:
            if schedule[0] == new_schedule:
                self.conexion.rollback()
                return
            
        

        
# cola =  "SELECT * FROM subjects s JOIN teachers_subjects ts ON s.subject_id = ts.subject_id  JOIN teachers t ON ts.teacher_id = t.teacher_id WHERE t.teacher_schedule = s.subject_schedule"
    
    
    
    def create(self, subject):
        
        try:
            super().open()
            self.sql1 = "SELECT teacher_id FROM teachers T JOIN users U ON U.user_id = T.user_id WHERE U.user_name = %s"
            self.cursor2.execute(self.sql1, (subject.teacher_id,))
            teacher_id = self.cursor2.fetchone()[0]
            print("1")

            self.sql2 = "SELECT room_id FROM room WHERE room_name = %s"
            self.cursor2.execute(self.sql2, (subject.subject_room,))
            room_id = self.cursor2.fetchone()[0]
            print("2")

            
            # Insert into subjects table
            self.mysql = "INSERT INTO subjects (subject_name, subject_credit, subject_semester, subject_degree, subject_schedule,  room_id) VALUES (%s, %s, %s, %s, %s, %s)"
            self.data =subject.subject_name, subject.subject_credits, subject.subject_semester, subject.subject_degree, subject.subject_schedule, room_id
            self.cursor1.execute(self.mysql, self.data)
            print("3")
            #self.conexion.commit()

            #self.check_teacher_schedule_conflict(teacher_id)

            # Get the last inserted subject_id
            subject_id = self.cursor1.lastrowid
            print("4")
            # Insert into teachers_subjects table
            self.cursor3.execute("INSERT INTO teachers_subjects (teacher_id, subject_id) VALUES (%s, %s)", (teacher_id, subject_id))
            self.conexion.commit()
            print("5")

        except Exception as e:
            print("create subject")
            print(e)

    def read(self, subject_id):
        try:
            super().open()
            self.sql = "SELECT * FROM subjects WHERE subject_id = %s"
            self.cursor1.execute(self.sql, (subject_id,))
            result = self.cursor1.fetchone()

            self.sql1 = "SELECT u.user_name FROM users u INNER JOIN teachers t ON u.user_id = t.user_id INNER JOIN teachers_subjects ts ON t.teacher_id = ts.teacher_id WHERE ts.subject_id = %s"
            self.cursor2.execute(self.sql1, (subject_id,))
            teacher = self.cursor2.fetchone()[0]

            self.sql2 = "SELECT room_name FROM room r INNER JOIN subjects s ON r.room_id = s.room_id WHERE s.subject_id = %s"
            self.cursor2.execute(self.sql2, (subject_id,))
            room = self.cursor2.fetchone()[0]
            return result, teacher, room
        except Exception as e:
            print(e)
        finally:
            super().close()

    def update(self, subject_id, subject_name, subject_credits, subject_semester, subject_degree):
        try:
            super().open()
            self.sql = "UPDATE subjects SET subject_name=%s, subject_credit=%s, subject_semester=%s, subject_degree=%s WHERE subject_id = %s"
            data = (subject_name, subject_credits, subject_semester, subject_degree, subject_id)
            self.cursor1.execute(self.sql, data)
            self.conexion.commit()
        except Exception as e:
            print(e)
        finally:
            super().close()


    def delete(self, subject_id):
        try:
            super().open()
            self.sql =  "UPDATE subjects SET status = FALSE WHERE subject_id = %s AND available = TRUE"
            self.cursor1.execute(self.sql, (subject_id,))
            rows_affected = self.cursor1.rowcount
            self.conexion.commit()
            super().close()

            if rows_affected > 0:
                messagebox.showinfo("Éxito", "La materia se ha eliminado correctamente.")
            else:
                messagebox.showwarning("Advertencia", "La materia está en uso")


        except Exception as e:
            print (e)


    def comboboxTeacher(self):
        super().open()
        self.sql = "SELECT user_name FROM users JOIN teachers ON users.user_id = teachers.user_id WHERE users.status is TRUE"
        self.cursor1.execute(self.sql)
        result = self.cursor1.fetchall()
        super().close()
        return result
    
    def comboboxRoom(self):
        super().open()
        self.sql = "SELECT room_name FROM room WHERE status is TRUE"
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


        





class Subject:
    
    def __init__(self, subject_id=None, subject_name="", subject_credits=None, subject_semester="", subject_degree="", subject_schedule="", teacher_id=None, subject_room="", subject_students_max=None): 
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.subject_credits = subject_credits
        self.subject_semester = subject_semester
        self.subject_degree = subject_degree
        self.subject_schedule = subject_schedule
        self.teacher_id = teacher_id
        self.subject_room = subject_room
        
    @property
    def subject_id(self):
        return self._subject_id

    @subject_id.setter
    def subject_id(self, value):
        self._subject_id = value

    @property
    def subject_name(self):
        return self._subject_name

    @subject_name.setter
    def subject_name(self, value):
        self._subject_name = value

    @property
    def subject_credits(self):
        return self._subject_credits

    @subject_credits.setter
    def subject_credits(self, value):
        self._subject_credits = value

    @property
    def subject_semester(self):
        return self._subject_semester

    @subject_semester.setter
    def subject_semester(self, value):
        self._subject_semester = value

    @property
    def subject_degree(self):
        return self._subject_degree

    @subject_degree.setter
    def subject_degree(self, value):
        self._subject_degree = value

    @property
    def subject_schedule(self):
        return self._subject_schedule

    @subject_schedule.setter
    def subject_schedule(self, value):
        self._subject_schedule = value

    @property
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        self._teacher_id = value

    @property
    def subject_room(self):
        return self._subject_room

    @subject_room.setter
    def subject_room(self, value):
        self._subject_room = value

    @property
    def subject_students_max(self):
        return self._subject_students_max

    @subject_students_max.setter
    def subject_students_max(self, value):
        self._subject_students_max = value



# | subjects | CREATE TABLE `subjects` (
#   `subject_id` int NOT NULL AUTO_INCREMENT,
#   `subject_name` varchar(50) DEFAULT NULL,
#   `subject_credit` int DEFAULT NULL,
#   `subject_semester` varchar(50) DEFAULT NULL,
#   `subject_degree` varchar(50) DEFAULT NULL,
#   `subject_schedule` varchar(100) DEFAULT NULL,
#   `teacher_id` int DEFAULT NULL,
#   `room_id` int DEFAULT NULL,
#   `subject_student_max` int DEFAULT NULL,
#   PRIMARY KEY (`subject_id`),
#   KEY `teacher_id` (`teacher_id`),
#   KEY `room_id` (`room_id`),
#   CONSTRAINT `subjects_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`teacher_id`),
#   CONSTRAINT `subjects_ibfk_2` FOREIGN KEY (`room_id`) REFERENCES `room` (`room_id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |