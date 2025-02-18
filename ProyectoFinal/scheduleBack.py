from TheClass import *

class DBschedule(DB):

    # def check_cohort_schedule_conflict(self):
    #     mysql = "SELECT * FROM COHORTS  c JOIN subject_cohorts  sc ON c.cohort_id = sc.cohort_id  JOIN subjects s ON s.subject_id = sc.subject_id"

    #     cola = "SELECT * FROM subjects where subject ="

    

    def create(self, cohort_id, subject_name):

        try:
            super().open()



            print("1.1")
            self.mysql = "UPDATE subjects SET cohort_id = %s, available = FALSE WHERE subject_name = %s"
            self.data = (cohort_id, subject_name)
            self.cursor1.execute(self.mysql, self.data)            # COLA = "SELECT * FROM COHORTS  c JOIN subject_cohorts  sc ON c.cohort_id = sc.cohort_id  JOIN subjects s ON s.subject_id = sc.subject_id"
            self.conexion.commit()
            print("1.2")
            # self.cursor1.execute("INSERT INTO subject_cohorts (subject_id, cohort_id) VALUES (%s, %s),", schedule.subjec_id, schedule.cohort_id)

            # self.cursor2.execute("UPDATE subjects SET available = False WHERE subject_name = %s ", (subject_name,))

        except Exception as e:
            print (e)
        finally:
            super().close()

    def read(self, cohort_id):
        try:
            super().open()
            self.mysql = "SELECT cohort_id, cohort_degree, cohort_semester, status FROM cohorts WHERE cohort_id = %s"
            self.cursor1.execute(self.mysql, (cohort_id,))
            result = self.cursor1.fetchone()
            print(result)
            return result
        except Exception as e:
            print(e)
        finally:
            super().close()


    def delete(self, subject_name):
        try:
            super().open()
            self.mysql = "UPDATE subjects SET cohort_id = NULL, available = TRUE WHERE subject_name = %s"
            self.data = (subject_name,)
            self.cursor1.execute(self.mysql, self.data)            # COLA = "SELECT * FROM COHORTS  c JOIN subject_cohorts  sc ON c.cohort_id = sc.cohort_id  JOIN subjects s ON s.subject_id = sc.subject_id"
            self.conexion.commit()
            print("1.2")
            # self.cursor1.execute("INSERT INTO subject_cohorts (subject_id, cohort_id) VALUES (%s, %s),", schedule.subjec_id, schedule.cohort_id)

            # self.cursor2.execute("UPDATE subjects SET available = False WHERE subject_name = %s ", (subject_name,))

        except Exception as e:
            print (e)
        finally:
            super().close()
#no se como hacer el update confio en vosotros
    def update(self, ):
        pass


#el delete tiene que borrar las cosas que se hiceron antes 

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


    def comboboxSubject(self, degree):
        super().open()
        self.mysql = "SELECT subject _name, sucject_schedule FROM subject WHERE subject_degree = %s"
        self.cursor1.execute(self.mysql, (degree,))
        result = self.cursor1.fetchall()
        super().close()
        return result



class Schedule:
    def __init__(self, schedule_id, schedule_degree ,schedule_semester, schedule_subject):
        self.shcedule_id = schedule_id
        #self.cohort_id = cohort_id
        self.shcedule_degree = schedule_degree
        self.shcedule_semester = schedule_semester
        self.schedule_subject = schedule_subject
