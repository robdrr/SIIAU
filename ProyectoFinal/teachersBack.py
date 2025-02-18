from TheClass import *
from tkinter import ttk, messagebox

class DBteacher(DB):
    def create(self, teacher):
        try:
            super().open()
            self.sql = "INSERT INTO teachers (teacher_id, user_id, teacher_degree,  teacher_level) VALUES (%s, %s, %s, %s)"
            self.data = (teacher.teacher_id, teacher.user_id, teacher.teacher_degree, teacher.teacher_level)
            self.cursor1.execute(self.sql, self.data)
            self.conexion.commit()
            super().close()
        except Exception as e:
            print(e)

    def read (self, teacher):
        try:
            super().open()
            self.sql = "SELECT * FROM teachers WHERE teacher_id = %s"
            self.cursor1.execute(self.sql, (teacher,))
            result = self.cursor1.fetchone()

            self.sql1 = "SELECT * FROM users AS u JOIN teacher as t ON users.user_id = t.teachers.user_id WHERE t.teachers.teacher_id = %s"
            self.cursor2.execute(self.sql1, (teacher,))
            result1 = self.cursor2.fetchone()
            super().close()
            return result, result1
        except Exception as e:
            print(e)

    def update(self, user_id, teacher_degree,  teacher_level):
        try:
            super().open()
            self.sql = "UPDATE teachers SET teacher_degree =%s, teacher_level=%s WHERE user_id = %s"
            self.data = (teacher_degree,  teacher_level, user_id)
            self.cursor1.execute(self.sql, self.data)
            self.conexion.commit()
            super().close()
        except Exception as e:
            print (e)

    def delete(self, teacher_id):
        try:
            super().open()
            self.sql ="UPDATE teachers SET status = FALSE WHERE student_id = %s"
            self.cursor1.execute(self.sql, (teacher_id,))
            self.conexion.commit()
            super().close()
        except Exception as e:
            print (e)

class Teachers:
    def __init__(self, teacher_id=None, user_id=None, teacher_degree="",  teacher_level=""):
        self._teacher_id = teacher_id
        self._user_id = user_id
        self._teacher_degree = teacher_degree
    
        self._teacher_level = teacher_level

    @property
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        self._teacher_id = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def teacher_degree(self):
        return self._teacher_degree

    @teacher_degree.setter
    def teacher_degree(self, value):
        self._teacher_degree = value

    @property
    def teacher_level(self):
        return self._teacher_level

    @teacher_level.setter
    def teacher_level(self, value):
        self._teacher_level = value



#HAY QUE BORRAR EL UNIQUE, tengo problemas con esa logica
#cuando creo una materia tomo un horario y un salon
#tengo que revisar que el salon este vacio a esa hora
#tengo que revisar el maestro este libre a esa hora

#el maestro guarda un horario y y 


# | TEACHERS | CREATE TABLE `teachers` (
#   `teacher_id` int NOT NULL AUTO_INCREMENT,
#   `user_id` int DEFAULT NULL,
#   `teacher_degree` varchar(50) DEFAULT NULL,
#   `teacher_level` varchar(50) DEFAULT NULL,
#   `status` tinyint(1) DEFAULT '1',
#   `teacher_schedule` varchar(100) DEFAULT NULL,
#   PRIMARY KEY (`teacher_id`),
#   UNIQUE KEY `user_id` (`user_id`),
#   UNIQUE KEY `UnicoHorario` (`teacher_schedule`),
#   CONSTRAINT `teachers_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)

#         mysql> CREATE TABLE teachers_subjects(
#     -> relation_id INT AUTO_INCREMENT PRIMARY KEY,
#     -> teacher_id INT,
#     -> subject_id INT,
#     -> FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
#     -> FOREIGN KEY (subject_id) REFERENCES subjects(subject_id));
# Query OK, 0 rows affected (0.10 sec)
