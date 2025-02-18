from TheClass import *
from tkinter import ttk, messagebox

class DBuser(DB):

    def logindb(self, user):
        try:
            super().open()
            self.sql = "INSERT INTO login (username) VALUES (%s)"
            self.cursor1.execute(self.sql, (user,))
            self.conexion.commit()
            super().close()
        except Exception as e:
            print(e)

    def get_login1(self):
        try:
            super().open()
            self.sql = "SELECT * FROM USERS JOIN LOGIN  ON users.user_username = login.username ORDER BY login_id DESC LIMIT 1;"
            self.cursor1.execute(self.sql)
            result = self.cursor1.fetchone()
            super().close()
            return result
        except Exception as e:
            print(e)


    def get_teacher(self):
        try:
            super().open()
            self.sql = "SELECT t.teacher_degree, t.teacher_level FROM teachers t INNER JOIN users u ON t.user_id = u.user_id INNER JOIN (SELECT * FROM login ORDER BY login_id DESC LIMIT 1) l ON u.user_username = l.username;"
            self.cursor1.execute(self.sql)
            result = self.cursor1.fetchone()
            super().close()
            return result
        except Exception as e:
            print(e)

    def create(self, user):   
        try:
            super().open()  
            self.sql = "INSERT INTO users (user_id, user_name, user_paternalSurname, user_maternalSurname, user_email, user_password, user_username, user_role) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            self.data = (user.user_id, user.user_name, user.user_paternalSurname, user.user_maternalSurname, user.user_email, user.user_password, user.user_username, user.user_role)
            self.cursor1.execute(self.sql, self.data)
            self.conexion.commit()
            super().close()  
            messagebox.showinfo("Éxito", "El usuario se ha creado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al crear el usuario: {str(e)}")

    def read(self, user_id):
        try:
            super().open()  
            self.sql = "SELECT * FROM users WHERE user_id = %s"
            self.cursor1.execute(self.sql, (user_id,))
            result = self.cursor1.fetchone()
            super().close()  
            return result
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al leer el usuario: {str(e)}")
            return None 


        
    def update(self, user):
        try:
            super().open()  
            self.sql = "UPDATE users SET user_name=%s, user_paternalSurname=%s, user_maternalSurname=%s, user_email=%s, user_password=%s, user_username=%s, user_role=%s  WHERE user_id = %s "
            data = (user.user_name, user.user_paternalSurname, user.user_maternalSurname, user.user_email, user.user_password, user.user_username, user.user_role, user.user_id)
            self.cursor1.execute(self.sql, data)
            self.conexion.commit()
            super().close()  
            messagebox.showinfo("Éxito", "El usuario se ha actualizado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al actualizar el usuario: {str(e)}")


    def delete(self, user_id):
        try:
            super().open()  
            self.sql = "UPDATE users SET status = FALSE WHERE user_id = %s"
            self.cursor1.execute(self.sql, (user_id,))
            self.conexion.commit()
            super().close()  
        except Exception as e:
            raise e



    def login(self, name, password):
        try:
            super().open()  
            self.sql = "SELECT * FROM users WHERE BINARY user_username = %s AND BINARY user_password = %s"
            self.data = (name, password)
            self.cursor1.execute(self.sql, self.data)
            result = self.cursor1.fetchone()
            super().close()  
            return result
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al iniciar sesión: {str(e)}")
            return None

        
    def get_user_by_name(self, username):
        # Función que se encarga de verificar si hay otro usuario con el mismo nombre de usuario
        try:
            super().open()  
            self.sql = "SELECT * FROM users WHERE BINARY user_username = %s"
            self.cursor1.execute(self.sql, (username,))
            result = self.cursor1.fetchone()
            super().close()  
            return result
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al obtener el usuario por nombre de usuario: {str(e)}")
            return None

class User:
    def __init__(self, user_id=None, user_name="",
                 user_paternalSurname="", user_maternalSurname="",
                 user_email="", user_password="",
                 user_username="", user_role=""):
        self._user_id = user_id
        self._user_name = user_name
        self._user_paternalSurname = user_paternalSurname
        self._user_maternalSurname = user_maternalSurname
        self._user_email = user_email
        self._user_password = user_password
        self._user_username = user_username
        self._user_role = user_role

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    @property
    def user_paternalSurname(self):
        return self._user_paternalSurname

    @user_paternalSurname.setter
    def user_paternalSurname(self, value):
        self._user_paternalSurname = value

    @property
    def user_maternalSurname(self):
        return self._user_maternalSurname

    @user_maternalSurname.setter
    def user_maternalSurname(self, value):
        self._user_maternalSurname = value

    @property
    def user_email(self):
        return self._user_email

    @user_email.setter
    def user_email(self, value):
        self._user_email = value

    @property
    def user_password(self):
        return self._user_password

    @user_password.setter
    def user_password(self, value):
        self._user_password = value

    @property
    def user_username(self):
        return self._user_username

    @user_username.setter
    def user_username(self, value):
        self._user_username = value

    @property
    def user_role(self):
        return self._user_role

    @user_role.setter
    def user_role(self, value):
        self._user_role = value


        