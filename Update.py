from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master
        # heading
        self.heading = ttk.Label(master, text = 'Update Appointments', font=('arial 40 bold'))
        self.heading.place(x=370,y=10)

        # label .. name
        self.name = ttk.Label(master, text = "Enter Patient's Name", font=('arial 18 bold'))
        self.name.place(x=210, y=95)

        # entry .. name
        self.namenet = ttk.Entry(master, width='30')
        self.namenet.place(x=550,y=102)

        # button
        self.search = ttk.Button(master, text='Search',width='12', command=self.search_db)
        self.search.place(x=900, y=100)

        # function for the button
    def search_db(self):
        self.input = self.namenet.get()

        #execute
        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.results = c.execute(sql, (self.input,))
        for self.row in self.results:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.location = self.row[3]
            self.phone = self.row[4]
            self.gender = self.row[5]
            self.time = self.row[6]

            # Updating
            self.uname = ttk.Label(self.master, text="Patient's Name", font=('arial 18 bold'))
            self.uname.place(x=225,y=150)

            self.uage = ttk.Label(self.master, text="Age", font=('arial 18 bold'))
            self.uage.place(x=225,y=190)

            self.ugender = ttk.Label(self.master, text="Gender", font=('arial 18 bold'))
            self.ugender.place(x=225,y=230)

            self.ulocation = ttk.Label(self.master, text="Location", font=('arial 18 bold'))
            self.ulocation.place(x=225,y=270)

            self.uphone = ttk.Label(self.master, text="Phone Number", font=('arial 18 bold'))
            self.uphone.place(x=225,y=310)

            self.utime = ttk.Label(self.master, text="Appointment Time", font=('arial 18 bold'))
            self.utime.place(x=225,y=350)

            # Entries + inserting values to it
            self.entname = ttk.Entry(self.master, width=30)
            self.entname.place(x=550, y=157)
            self.entname.insert(END, str(self.name1))

            self.entage = ttk.Entry(self.master, width=30)
            self.entage.place(x=550, y=197)
            self.entage.insert(END, str(self.age))

            self.entgender = ttk.Entry(self.master, width=30)
            self.entgender.place(x=550, y=237)
            self.entgender.insert(END, str(self.gender))

            self.entlocation = ttk.Entry(self.master, width=30)
            self.entlocation.place(x=550, y=277)
            self.entlocation.insert(END, str(self.location))

            self.entphone = ttk.Entry(self.master, width=30)
            self.entphone.place(x=550, y=317)
            self.entphone.insert(END, str(self.phone))

            self.enttime = ttk.Entry(self.master, width=30)
            self.enttime.place(x=550, y=357)
            self.enttime.insert(END, str(self.time))

            # executing updates
            self.update = ttk.Button(self.master, text='Update',width='12', command=self.update_db)
            self.update.place(x=900, y=200)

            # deleting Button
            self.delete = ttk.Button(self.master, text='Delete',width='12', command=self.delete_db)
            self.delete.place(x=900, y=260)


    def update_db(self):
        # declaring variable to update database
        self.var1 = self.entname.get()
        self.var2 = self.entage.get()
        self.var3 = self.entgender.get()
        self.var4 = self.entlocation.get()
        self.var5 = self.entphone.get()
        self.var6 = self.enttime.get()
        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
        c.execute(query,(self.var1, self.var2, self.var3, self.var4, self.var5, self.var6,self.namenet.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success","Successfully Updated !")

    def delete_db(self):
        # deleting an appointment
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2,(self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.entname.destroy()
        self.entage.destroy()
        self.entgender.destroy()
        self.entlocation.destroy()
        self.entphone.destroy()
        self.enttime.destroy()
        self.update.destroy()
        self.delete.destroy()


root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.resizable(False,False)
root.title("Update Appointments")
root.mainloop()
