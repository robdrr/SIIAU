from TheClass import *
from tkinter import ttk, messagebox


class DBroom(DB):
    
    def create(self, room):   
        try:
            super().open()  

            # Verificar si ya existe una habitación con el mismo nombre y edificio y status = 1
            self.sql_check = "SELECT COUNT(*) FROM room WHERE room_name = %s AND room_building = %s AND status = 1"
            self.data_check = (room.room_name, room.room_building)
            self.cursor1.execute(self.sql_check, self.data_check)
            count = self.cursor1.fetchone()[0]

            # Si ya existe una habitación con el mismo nombre y edificio y status = 1, no permitir la inserción
            if count > 0:
                messagebox.showwarning("Advertencia", "Ya existe una habitación activa con el mismo nombre y edificio.")
            else:
                # Si no existe una habitación con el mismo nombre y edificio y status = 1, proceder con la inserción
                self.sql_insert = "INSERT INTO room (room_name, room_building) VALUES (%s, %s)"
                self.data_insert = (room.room_name, room.room_building)
                self.cursor1.execute(self.sql_insert, self.data_insert)
                self.conexion.commit()
                messagebox.showinfo("Éxito", "La habitación se ha creado correctamente.")

        except Exception as e:
            print("Error al insertar en la base de datos:", str(e))
            messagebox.showerror("Error", f"Se produjo un error al crear la habitación: {str(e)}")
        finally:
            super().close()


    def read(self, room_id):
        try:
            super().open()  
            self.sql = "SELECT * FROM room WHERE room_id = %s"
            self.cursor1.execute(self.sql, (room_id,))
            result = self.cursor1.fetchone()
            super().close()  
            return result
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al leer la habitación: {str(e)}")
            return None 

    def update(self, room):
        try:
            super().open()  

            # Verificar si ya existe una habitación con el mismo nombre y edificio y status = 1
            self.sql_check = "SELECT COUNT(*) FROM room WHERE room_name = %s AND room_building = %s AND status = 1 AND room_id != %s"
            self.data_check = (room.room_name, room.room_building, room.room_id)
            self.cursor1.execute(self.sql_check, self.data_check)
            count = self.cursor1.fetchone()[0]

            # Si ya existe una habitación con el mismo nombre y edificio y status = 1, no permitir la actualización
            if count > 0:
                messagebox.showwarning("Advertencia", "Ya existe una habitación activa con el mismo nombre y edificio.")
            else:
                # Si no existe una habitación con el mismo nombre y edificio y status = 1, proceder con la actualización
                self.sql_update = "UPDATE room SET room_name=%s, room_building=%s WHERE room_id = %s"
                data_update = (room.room_name, room.room_building, room.room_id)
                self.cursor1.execute(self.sql_update, data_update)
                self.conexion.commit()
                messagebox.showinfo("Éxito", "La habitación se ha actualizado correctamente.")

        except Exception as e:
            print("Error al actualizar la habitación:", str(e))
            messagebox.showerror("Error", f"Se produjo un error al actualizar la habitación: {str(e)}")
        finally:
            super().close()

    def delete(self, room_id):
        try:
            super().open()  
            self.sql = "UPDATE room SET status=FALSE WHERE room_id = %s AND room_id NOT IN (SELECT DISTINCT room_id FROM subjects);"
            self.cursor1.execute(self.sql, (room_id,))
            rows_affected = self.cursor1.rowcount
            self.conexion.commit()
            super().close()  

            if rows_affected > 0:
                messagebox.showinfo("Éxito", "El aula se ha eliminado correctamente.")
            else:
                messagebox.showwarning("Advertencia", "El aula está siendo ocupada.")
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al eliminar el aula: {str(e)}")

class Room:
    def __init__(self, room_id=None, room_name="", room_building=""):
        self._room_id = room_id
        self._room_name = room_name
        self._room_building = room_building

    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value

    @property
    def room_name(self):
        return self._room_name

    @room_name.setter
    def room_name(self, value):
        self._room_name = value

    @property
    def room_building(self):
        return self._room_building

    @room_building.setter
    def room_building(self, value):
        self._room_building = value

