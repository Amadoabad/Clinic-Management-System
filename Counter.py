from tkinter import*
from tkinter import ttk
import sqlite3
import pyttsx3

# connect to db
conn = sqlite3.connect("database.db")
c = conn.cursor()

# empty lists to append later
number = []
patients = []

sql = "SELECT * FROM appointments"
result = c.execute(sql)
for r in result:
    ids = r[0]
    name = r[1]
    number.append(ids)
    patients.append(name)

class Application:
    def __init__(self,master):
        self.master = master

        self.x = 0

        # heading
        self.heading = ttk.Label(master, text="Appointments", font="arial 60 bold")
        self.heading.pack()

        # button to change patients
        self.change = ttk.Button(master, text="Next Patient", width='25',command=self.change_db )
        self.change.place(x=510, y=600)

        #=============
        self.num = ttk.Label(master, text='', font="arial 150 bold")
        self.num.pack()

        Label(master, text="").pack()
        Label(master, text="").pack()
        self.patient_name = ttk.Label(master, text='', font="arial 80 bold")
        self.patient_name.pack()

    def change_db(self):
        self.num.config(text=str(number[self.x]))
        self.patient_name.config(text=str(patients[self.x]))
        #voices
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-30)
        engine.say('patient number ' + str(number[self.x]) +'  '+ str(patients[self.x]))
        engine.runAndWait()
        self.x +=1


root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.resizable(False,False)
root.title("Appointments' counter")
root.mainloop()
