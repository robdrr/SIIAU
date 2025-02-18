import tkinter as tk
from tkinter import ttk, messagebox
from roomBack import *


class fClassroom:
        
    def classrooms_interface(self):
        self.classroom_frame.pack_propagate(0)

        tk.Label(self.classroom_frame, text="Input Classroom Code:").place(x=80, y=20)
        self.entry_search_classroom = tk.Entry(self.classroom_frame)
        self.entry_search_classroom.place(x=215, y=20)
        self.button_search_classroom = tk.Button(self.classroom_frame, text="Search",width=10, command=self.read_classroom)
        self.button_search_classroom.place(x=355, y=18)

        tk.Label(self.classroom_frame, text="ID:").place(x=88, y=80)
        self.entry_id_classroom = tk.Entry(self.classroom_frame, state="readonly")
        self.entry_id_classroom.place(x=120, y=80)

        tk.Label(self.classroom_frame, text="Classroom:").place(x=45, y=160)
        self.entry_classroom_classroom = tk.Entry(self.classroom_frame)
        self.entry_classroom_classroom.place(x=120, y=160)

        tk.Label(self.classroom_frame, text="Building:").place(x=55, y=240)
        self.combobox_building_classroom = ttk.Combobox(self.classroom_frame, values=["A", "B", "C"])
        self.combobox_building_classroom.place(x=120, y=240)

#------------------ Botones ----------------------------------
        
        self.button_new_classroom = tk.Button(self.classroom_frame, text="NEW",width=10, command=self.new_classroom)
        self.button_new_classroom.place(x=30, y=380)

        self.button_save_classroom = tk.Button(self.classroom_frame, text="SAVE",width=10, command=self.create_classroom)
        self.button_save_classroom.place(x=150, y=380)

        self.button_Cancel_classroom = tk.Button(self.classroom_frame, text="CANCEL",width=10, command=self.cancel_classroom)
        self.button_Cancel_classroom.place(x=270, y=380)

        self.button_edit_classroom = tk.Button(self.classroom_frame, text="EDIT",width=10, command=self.update_classroom)
        self.button_edit_classroom.place(x=390, y=380)
        self.button_edit_classroom.config(state="disabled")

        self.button_drop_classroom = tk.Button(self.classroom_frame, text="DROP",width=10, command=self.drop_classroom)
        self.button_drop_classroom.place(x=510, y=380)
        self.button_drop_classroom.config(state="disabled")
        self.classroom_bottons = [self.button_new_classroom, self.button_save_classroom, self.button_Cancel_classroom, self.button_edit_classroom, self.button_drop_classroom]

#----------------------------Subject Functions--------------------------
        
    def create_classroom(self):
        try:
            room_name = self.entry_classroom_classroom.get()
            room_building = self.combobox_building_classroom.get()
            new_room = Room(room_name=room_name, room_building=room_building)
            self.dbR.create(new_room)

            if not all([room_name, room_building]):
                messagebox.showerror("Error", "Fill all the blanks")
                return


            #messagebox.showinfo("Éxito", "La habitación se ha creado correctamente.")
            print("p")
            self.cancel_classroom()
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")

    def read_classroom(self):
        try:

            room_id = self.entry_search_classroom.get()
            room_data = self.dbR.read(room_id)
            if room_data:
                if room_data[3]:

                    self.entry_id_classroom.configure(state="normal")
                    self.entry_id_classroom.delete(0, tk.END)
                    self.entry_id_classroom.insert(0, room_data[0])
                    self.entry_id_classroom.configure(state="readonly")
                    self.entry_classroom_classroom.delete(0, tk.END)
                    self.entry_classroom_classroom.insert(0, room_data[1])
                    self.combobox_building_classroom.set(room_data[2])
                else:
                    messagebox.showerror("Error", "Clasroom no longer exists")
            else:
                messagebox.showerror("Error", "No se encontró ningún aula con ese código.")
            self.button_save_classroom.config(state="disabled")
            self.button_edit_classroom.config(state="normal")
            self.button_drop_classroom.config(state="normal")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")

    def update_classroom(self):
        try:
            room_id = self.entry_id_classroom.get()
            room_name = self.entry_classroom_classroom.get()
            room_building = self.combobox_building_classroom.get()
            room = Room(room_id=room_id, room_name=room_name, room_building=room_building)
            self.dbR.update(room)

            #messagebox.showinfo("Success", "Classroom updated successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")


    def drop_classroom(self):
        try:
            room_id = self.entry_id_classroom.get()
            self.dbR.delete(room_id)
            self.entry_id_classroom.configure(state="normal")
            self.entry_id_classroom.delete(0, tk.END)
            self.entry_id_classroom.configure(state="readonly")
            self.entry_classroom_classroom.delete(0, tk.END)
            self.combobox_building_classroom.set("")
            #messagebox.showinfo("Success", "Room deleted successfully")
            self.button_save_classroom.config(state="normal")
            self.cancel_classroom()
            
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")
   
    def cancel_classroom(self):
        try:
            self.entry_id_classroom.configure(state="normal")
            self.entry_id_classroom.delete(0, tk.END)
            self.entry_id_classroom.configure(state="readonly")
            self.entry_classroom_classroom.delete(0, tk.END)
            self.combobox_building_classroom.set("")
            self.button_save_classroom.config(state="normal")
            self.button_edit_classroom.config(state="disabled")
            self.button_drop_classroom.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")

    
    def new_classroom(self):
        try:
            self.entry_id_classroom.configure(state="normal")
            self.entry_id_classroom.delete(0, tk.END)
            self.entry_id_classroom.configure(state="readonly")
            self.entry_classroom_classroom.delete(0, tk.END)
            self.combobox_building_classroom.set("")
            self.button_save_classroom.config(state="normal")
            self.button_edit_classroom.config(state="disabled")
            self.button_drop_classroom.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")



        
