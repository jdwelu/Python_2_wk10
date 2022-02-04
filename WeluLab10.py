#! /usr/bin/env python3


import tkinter as tk
from tkinter import ttk
import re
import xml.etree.ElementTree as et
import xml.dom.minidom as xdm
import sqlite3
import csv


class EmployeesFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)

        # Define string variable for the entry field
        self.Employee_ID = tk.StringVar()
        self.First_Name = tk.StringVar()
        self.Last_Name = tk.StringVar()
        self.Pay_Rate = tk.StringVar()

        self.labelValue = tk.StringVar()
        self.labelValue.set("+program started+")

        # Create a label, an entry field, and a button
        ttk.Labelspace0 = ttk.Label(self, text="***   Employee Information   ***").grid(column=0, row=0, columnspan=2)
        
        ttk.Label0 = ttk.Label(self, text="Employee ID: ").grid(column=0, row=1, sticky=tk.W)
        ttk.Entry0 = ttk.Entry(self, textvariable=self.Employee_ID).grid(column=1, row=1)

        ttk.Label1 = ttk.Label(self, text="First Name: ").grid(column=0, row=2, sticky=tk.W)
        ttk.Entry1 = ttk.Entry(self, textvariable=self.First_Name).grid(column=1, row=2)

        ttk.Label2 = ttk.Label(self, text="Last Name: ").grid(column=0, row=3, sticky=tk.W)
        ttk.Entry2 = ttk.Entry(self, textvariable=self.Last_Name).grid(column=1, row=3)

        ttk.Label3 = ttk.Label(self, text="Pay Rate: ").grid(column=0, row=4, sticky=tk.W)
        ttk.Entry3 = ttk.Entry(self, textvariable=self.Pay_Rate).grid(column=1, row=4)

        ttk.Labelspace1 = ttk.Label(self, text="").grid(column=0, row=5, columnspan=2)

        ttk.Labelspace2 = ttk.Label(self, text="***   Storage Selection   ***").grid(column=0, row=6, columnspan=2)

        ttk.Button0 = tk.Button(self, text="SQL DB", width=10, bg="pink", fg="black", command=self.sqlDB).grid(column=0, row=7, sticky=tk.W)
        ttk.Label4 = ttk.Label(self, text=" add to .db file ").grid(column=1, row=7)

        ttk.Button1 = tk.Button(self,text="XML", width=10, bg="lightblue", fg="black", command=self.modifyXML).grid(column=0, row=8, sticky=tk.W)
        ttk.Label5 = ttk.Label(self, text=" add to .xml file ").grid(column=1, row=8)

        ttk.Button2 = tk.Button(self, text="CSV", width=10, bg="lightgreen", fg="black", command=self.modifyCSV).grid(column=0, row=9, sticky=tk.W)
        ttk.Label6 = ttk.Label(self, text=" add to .csv file ").grid(column=1, row=9)

        ttk.Button3 = tk.Button(self, text="RESET", width=10, bg="lightyellow", fg="black", command=self.clear).grid(column=0, row=10, sticky=tk.W)
        ttk.Label7 = ttk.Label(self, text=" clear all entries ").grid(column=1, row=10)

        ttk.Labelspace3 = ttk.Label(self, text="").grid(column=0, row=11, columnspan=2)

        ttk.Label8 = ttk.Label(self, text="***   Status   ***").grid(column=0, row=12, columnspan=2)

        ttk.Label9 = ttk.Label(self, textvariable=self.labelValue).grid(column=0, row=13, columnspan=2)

        ttk.Labelspace4 = ttk.Label(self, text="").grid(column=0, row=14, columnspan=2)

        

        # ttk.Button0 = ttk.Button(self, text="Clear", command=self.clear).grid(column=2, row=0)

        # Add padding to all the child components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)


    def modifyCSV(self):
##        print("Employee ID: ", self.Employee_ID.get())
##        print("First Name: ", self.First_Name.get())
##        print("Last Name: ", self.Last_Name.get())
##        print("Pay Rate: ", self.Pay_Rate.get())

        try:
            entry0 = int(self.Employee_ID.get())
            entry1 = str(self.First_Name.get())
            entry2 = str(self.Last_Name.get())
            entry3 = float(self.Pay_Rate.get())
            entry4 = str(format(entry3, ',.2f'))

            if entry0 == "":
                raise TypeError
            if entry1 == "":
                raise TypeError
            if entry2 == "":
                raise TypeError
            if entry3 == "":
                raise TypeError
            if entry3 < 9.00:
                raise TypeError

            # Reading the csv file.
            datafile = open('employees.csv', 'r')
            datareader = csv.reader(datafile, delimiter=',')

            # Initializing an array to store the data read.
            data = []

            # Populating and checking the data array.
            for line in datareader:
                data.append(line)
            ##print()
            ##print(data)
            ##print()

            # Closing the file now that the data array has been populated.
            datafile.close()

            # Displaying the element arrays vertically.
            print()
            for element in data:
                print(element, end="\n")
            print()

            # Simply adding another element to the csv file.
            print()
            print("Adding another element to the list of employees.")
            print()
            data.append([entry0, entry1, entry2, entry4])
            for row in data:
                for column in row:
                    print(column, end=" | ")
                print()
            print()

            # Creating a new .csv file with the manipulated data.
##            print()
##            print("***New CSV file updated_products.csv created!***")
##            print()
            employees_csv = open('employees.csv', "w", newline="")
            cvsWriter = csv.writer(employees_csv, delimiter=',')
            cvsWriter.writerows(data)
            employees_csv.close()


            self.labelValue.set("CSV successfully modified!")

        except:
            self.labelValue.set("Error or Invalid Data Entry!")
        
            
    def sqlDB(self):
        # Using the print functions to test the get.
##        print("Employee ID: ", self.Employee_ID.get())
##        print("First Name: ", self.First_Name.get())
##        print("Last Name: ", self.Last_Name.get())
##        print("Pay Rate: ", self.Pay_Rate.get())
##        print()
##        print()

        try:
            entry0 = int(self.Employee_ID.get())
            entry1 = str(self.First_Name.get())
            entry2 = str(self.Last_Name.get())
            entry3 = float(self.Pay_Rate.get())

            if entry0 == "":
                raise TypeError
            if entry1 == "":
                raise TypeError
            if entry2 == "":
                raise TypeError
            if entry3 == "":
                raise TypeError
            if entry3 < 9.00:
                raise TypeError


##            conn = sqlite3.connect('employees.db')  # Create connection object
##
##            c = conn.cursor() # Get a cursor object -- which works with tables
##
##            ## This is string I will used to create the original table
##            tableString = """CREATE TABLE employee (
##               employee_id INTEGER not null primary key,
##               first_name VARCHAR(30), last_name VARCHAR(30),
##               pay_rate VARCHAR(30))"""
##
##            c.execute(tableString) # Create a table
##
##            ## Insert original rows of data into the table
##            c.execute("INSERT INTO employee VALUES (123,'John','Doe','9.15')")
##            c.execute("INSERT INTO employee VALUES (456,'Jane','Doe','10.25')")
##            c.execute("INSERT INTO employee VALUES (789,'Jim','Doe','12.35')")
##            c.execute("INSERT INTO employee VALUES (12,'Jax','Doe','9.20')")
##
##
##            conn.commit() # Save (commit) the changes
##
##            ## We can also close the connection if we are done with it.
##            ## Just be sure any changes have been committed or they will be lost.
##            conn.close()


            # Creating a query to see the table
            print("QUERY: DISPLAY CURRENT TABLE: employee")
            conn = sqlite3.connect('employees.db')
            c = conn.cursor()
            c.execute("SELECT * FROM employee")
            records = c.fetchall()
            for rec in records:
                print(rec)

            print()
            print()
            conn.close()


            # Adding a new record to the table
            print("QUERY: ADDING A NEW RECORD AND DISPLAYING THE NEW TABLE: employee")
            conn = sqlite3.connect('employees.db')
            c = conn.cursor()
            c.execute("INSERT INTO employee (employee_id, first_name, last_name, pay_rate) VALUES (?, ?, ?, ?)", (entry0, entry1, entry2, entry3))
            conn.commit()
            c.execute("SELECT * FROM employee")
            records = c.fetchall()
            for rec in records:
                print(rec)

            print()
            print()
            conn.close()
            

            self.labelValue.set("SQL successfully modified!")

        except:
            self.labelValue.set("Error or Invalid Data Entry!")

            
    # Creating the XML Button function.
    def modifyXML(self):
        # Using the print functions to test the get.
##        print("Employee ID: ", self.Employee_ID.get())
##        print("First Name: ", self.First_Name.get())
##        print("Last Name: ", self.Last_Name.get())
##        print("Pay Rate: ", self.Pay_Rate.get())

        try:
            entry0 = int(self.Employee_ID.get())
            entry1 = str(self.First_Name.get())
            entry2 = str(self.Last_Name.get())
            entry3 = float(self.Pay_Rate.get())

            if entry0 == "":
                raise TypeError
            if entry1 == "":
                raise TypeError
            if entry2 == "":
                raise TypeError
            if entry3 == "":
                raise TypeError
            if entry3 < 9.00:
                raise TypeError
            

            # Parse the selected XML file
            print()
            tree = et.parse('employees.xml')
            root = tree.getroot() # get the company element
            print(root)


            # Detail the XML file tree.
            company0 = et.SubElement(root, 'employee')

            employee_id0 = et.SubElement(company0, 'employee_id')
            employee_id0.text = str(entry0)

            first_name0 = et.SubElement(company0, 'first_name')
            first_name0.text = str(entry1)

            last_name0 = et.SubElement(company0, 'last_name')
            last_name0.text = str(entry2)

            pay_rate0 = et.SubElement(company0, 'pay_rate')
            pay_rate0.text = str(format(entry3, ',.2f'))


            # Testing in IDLE to see my data
            et.dump(root)

            # Writing to file
            tree.write('employees.xml')


            self.labelValue.set("XML successfully modified!")

        except:
            self.labelValue.set("Error or Invalid Data Entry!")
        

    # Define the callback method for the Clear Button.
    def clear(self):
        # Using the print functions to test the get.
##        print("Employee ID: ", self.Employee_ID.get())
##        print("First Name: ", self.First_Name.get())
##        print("Last Name: ", self.Last_Name.get())
##        print("Pay Rate: ", self.Pay_Rate.get())
        self.Employee_ID.set("")
        self.First_Name.set("")
        self.Last_Name.set("")
        self.Pay_Rate.set("")
        self.labelValue.set("+program running+")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Update Employees")
    EmployeesFrame(root)
    root.mainloop()

        
