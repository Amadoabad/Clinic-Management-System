from tkinter import*
import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox




conn = sqlite3.connect("database.db")
c = conn.cursor()
# empty list to append from database later
ids=[]
class Application:
    def __init__(self, master):
        self.master = master

        self.left = Frame(master,width=800, height=720)
        self.left.pack(side = LEFT)

        self.right = Frame(master,width=400 ,height=720 )
        self.right.pack(side = RIGHT)
        
        # labels
        self.heading = ttk.Label(self.left, text='Clinic Appointments',font=('arial 40 bold'))
        self.heading.place(x=10, y=10)
        # Patient
        self.name = ttk.Label(self.left, text="Patient's Name",font=('arial 18 bold'))
        self.name.place(x=10, y=100)
        # age
        self.age = ttk.Label(self.left, text="Age",font=('arial 18 bold'))
        self.age.place(x=10, y=140)
        # gender
        self.gender = ttk.Label(self.left, text="Gender",font=('arial 18 bold'))
        self.gender.place(x=10, y=180)
        # location
        self.location = ttk.Label(self.left, text="Location",font=('arial 18 bold'))
        self.location.place(x=10, y=220)
        # appointment time
        self.appointment_time = ttk.Label(self.left, text="Appointment Time",font=('arial 18 bold'))
        self.appointment_time.place(x=10, y=260)
        # phone
        self.phone = ttk.Label(self.left, text="Phone Number", font=('arial 18 bold'))
        self.phone.place(x=10, y=300)
        # entries =========for labels
        self.name_ent= ttk.Entry(self.left, width=30)
        self.name_ent.place(x=250, y=108)
        # age
        self.age_ent= ttk.Entry(self.left, width=30)
        self.age_ent.place(x=250, y=148)
        # gender
        self.gender_ent= ttk.Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=188)
        # location
        self.location_ent= ttk.Entry(self.left, width=30)
        self.location_ent.place(x=250, y=228)
        # time
        self.time_ent= ttk.Entry(self.left, width=30)
        self.time_ent.place(x=250, y=268)
        # phone
        self.phone_ent= ttk.Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=308)
        # button
        self.submit = ttk.Button(self.left, text="Add Appointment", width=20,command= self.add_appointment)
        self.submit.place(x=268,y=370)
        # getting the number of appointments
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids) - 1]
        # logs in right frame
        self.logs = Label(self.right, text='Logs', font=('arial 28 bold'))
        self.logs.place(x=0,y=0)
        self.box = Text(self.right, width=45, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Total Appointments till now : " + str(self.final_id)+'\n')
    # Function for submit button
    def add_appointment(self):
        # getting values
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '':
            tkinter.messagebox.showwarning("Warning","Please Fill Up All Boxes ")
        else:
            # add to database
            sql = '''INSERT INTO 'appointments'(name,age,gender,location,scheduled_time,phone) VALUES(?, ?, ?, ?, ?, ?)'''
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Appointment for " +str(self.val1)+ " has been arranged")

            self.box.insert(END,'Appointment Arrenged for '+ str(self.val1)+' at '+str(self.val5) + "\n")

root =Tk()


b = Application(root)
root.geometry("1200x720+0+0")
root.resizable(False,False)
root.title("Appointment")


root.mainloop()
