# Fast Food Information Management System
from functools import partial
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import custom as cs
import credentials as cr

class Management:
    def __init__(self, root):
        self.window = root
        self.window.title("FAST FOOD INFORMATION MANAGEMENT SYSTEM")
        self.window.geometry("1350x750+0+0")
        self.window.config(bg="white")

        # Customization
        self.color_1 = cs.color_1
        self.color_2 = cs.color_2
        self.color_3 = cs.color_3
        self.color_4 = cs.color_4
        self.font_1 = cs.font_1
        self.font_2 = cs.font_2

        # User Credentials
        self.host = cr.host
        self.user = cr.user
        self.password = cr.password
        self.database = cr.database

        # Left Frame
        self.frame_1 = Frame(self.window, bg=self.color_1)
        self.frame_1.place(x=0, y=0, width=1100, relheight=1)

        # Right Frame
        self.frame_2 = Frame(self.window, bg=self.color_2)
        self.frame_2.place(x=1100, y=0, relwidth=1, relheight=1)

        # Buttons
        self.view_bt = Button(self.frame_2, text='Search Food', font=(self.font_1, 12), bd=2, command=self.get_info_view, cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=68,y=40,width=100)
        self.add_bt = Button(self.frame_2, text='Add New', font=(self.font_1, 12), bd=2, command=self.add_food, cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=68,y=100,width=100)
        self.update_bt = Button(self.frame_2, text='Show All', font=(self.font_1, 12), bd=2, command=self.show_all, cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=68,y=160,width=100)
        self.delete_bt = Button(self.frame_2, text='Update', font=(self.font_1, 12), bd=2, command=self.get_info_update,cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=68,y=220,width=100)
        self.clear_bt = Button(self.frame_2, text='Clear', font=(self.font_1, 12), bd=2, command=self.clear_screen, cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=68,y=280,width=100)
        self.exit_bt = Button(self.frame_2, text='Exit', font=(self.font_1, 12), bd=2, command=self.Exit, cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=68,y=340,width=100)


    def show_all(self):
        self.clear_screen()

        # Create treeview with scrollbar frame
        self.treeScroll = Scrollbar(self.frame_1)
        self.treeScroll.pack(side=RIGHT, fill=Y)

        self.tree = ttk.Treeview(self.frame_1, yscrollcommand=self.treeScroll.set, height=37)
        self.tree.pack()

        self.treeScroll.config(command=self.tree.yview)

        # Define columns and headings
        self.tree['columns'] = ("No", "Brand", "Type", "Name", "Carbs", "Protein", "Fat", "Calo", "Data Source")

        self.tree.column("#0", width=0, stretch=0)
        self.tree.column("No", width=40)
        self.tree.column("Brand", anchor=W, width=120)
        self.tree.column("Type", anchor=W, width=120)
        self.tree.column("Name", anchor=W, width=186)
        self.tree.column("Carbs", anchor=W, width=80)
        self.tree.column("Protein", anchor=W, width=80)
        self.tree.column("Fat", anchor=W, width=80)
        self.tree.column("Calo", anchor=W, width=80)
        self.tree.column("Data Source", anchor=W, width=300)

        self.tree.heading("#0", text="")
        self.tree.heading("No", text="No.", anchor=W)
        self.tree.heading("Brand", text="Brand", anchor=W)
        self.tree.heading("Type", text="Type", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("Carbs", text="Carbs", anchor=W)
        self.tree.heading("Protein", text="Protein", anchor=W)
        self.tree.heading("Fat", text="Fat", anchor=W)
        self.tree.heading("Calo", text="Calo", anchor=W)
        self.tree.heading("Data Source", text="Data Source", anchor=W)

        self.tree.pack(pady=0, padx=0)

        # Import data from mysql to treeview
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        curs = connection.cursor()
        curs.execute("SELECT * FROM fast_food")
        records = curs.fetchall()

        for record in records:
            self.tree.insert(parent="", index="end", iid=record[0], text=record[0], values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]))
        connection.commit()
        connection.close()


    # Widgets for adding fast food information
    def add_food(self):
        self.clear_screen()

        self.No = Label(self.frame_1, text="No", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=40,y=30)
        self.No_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.No_entry.place(x=50,y=65, width=200, height=30)

        self.Brand = Label(self.frame_1, text="Brand", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=40,y=150)
        self.Brand_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.Brand_entry.place(x=50,y=185, width=200, height=30)

        self.Type = Label(self.frame_1, text="Type", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=300,y=150)
        self.Type_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.Type_entry.place(x=310,y=185, width=200, height=30)

        self.Name = Label(self.frame_1, text="Name", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=560,y=150)
        self.Name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.Name_entry.place(x=570,y=185, width=200, height=30)

        self.Carbs = Label(self.frame_1, text="Carbs", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=40,y=270)
        self.Carbs_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.Carbs_entry.place(x=50,y=305, width=200, height=30)

        self.Protein = Label(self.frame_1, text="Protein", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=300,y=270)
        self.Protein_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.Protein_entry.place(x=310,y=305, width=200, height=30)

        self.Fat = Label(self.frame_1, text="Fat", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=560,y=270)
        self.Fat_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.Fat_entry.place(x=570,y=305, width=200, height=30)

        self.Calo = Label(self.frame_1, text="Calo", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=820,y=270)
        self.Calo_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.Calo_entry.place(x=830,y=305, width=200, height=30)

        self.dataSource = Label(self.frame_1, text="Data Source", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=40,y=390)
        self.dataSource_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.dataSource_entry.place(x=50,y=425, width=980, height=30)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(self.font_1, 15), bd=2, command=self.submit, cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=490,y=550,width=100)


    # Show a fast food information
    def get_info_view(self):
        self.clear_screen()

        self.getName = Label(self.frame_1, text="Enter name", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=140,y=70)
        self.getName_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getName_entry.place(x=163, y=110, width=800, height=30)

        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_1, 15), bd=2, command=self.check_info_view, cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=490,y=200,width=80)
            
    # Update a fast food information
    def get_info_update(self):
        self.clear_screen()

        self.getName = Label(self.frame_1, text="Enter name", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=140,y=70)
        self.getName_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getName_entry.place(x=163, y=110, width=800, height=30)

        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_1, 15), bd=2, command=self.check_info_update, cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=490,y=200,width=80)

    # Remove all widgets from the frame 1
    def clear_screen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

    # Exit window
    def Exit(self):
        exit = messagebox.askyesno("EXIT", "Do you want to exit?")
        if exit > 0:
            root.destroy()
            return

    # Checks whether the food name is available or not. If available, the function calls the 'show_info' function to display the result.
    def check_info_view(self):
        if self.getName_entry.get() == '':
            messagebox.showerror("Error!", "All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("SELECT * FROM fast_food WHERE Name=%s", self.getName_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Food doesn't exist",parent=self.window)
                else:
                    self.show_info(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    # Checks whether the food name is available or not. If available, the function calls the 'get_update_details' function to get the new data to perform update operation.
    def check_info_update(self):
        if self.getName_entry.get() == '':
            messagebox.showerror("Error!", "All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("SELECT * FROM fast_food WHERE Name=%s", self.getName_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Food doesn't exists",parent=self.window)
                else:
                    self.get_update_details(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    # Gets the food name that the user wants to update to perform the update operation
    def get_update_details(self, row):
        self.clear_screen()

        self.Carbs = Label(self.frame_1, text="Carbs", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=40,y=150)
        self.Carbs_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.Carbs_entry.place(x=50,y=185, width=200, height=30)

        self.Protein = Label(self.frame_1, text="Protein", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=300,y=150)
        self.Protein_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.Protein_entry.place(x=310,y=185, width=200, height=30)

        self.Fat = Label(self.frame_1, text="Fat", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=560,y=150)
        self.Fat_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.Fat_entry.place(x=570,y=185, width=200, height=30)

        self.Calo = Label(self.frame_1, text="Calo", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=820,y=150)
        self.Calo_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.Calo_entry.place(x=830,y=185, width=200, height=30)

        self.dataSource = Label(self.frame_1, text="Data Source", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=40,y=270)
        self.dataSource_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.dataSource_entry.place(x=50,y=305, width=980, height=30)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(self.font_1, 15), bd=2, command=partial(self.update_info, row), cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=160,y=425,width=100)
        self.cancel_bt = Button(self.frame_1, text='Cancel', font=(self.font_1, 15), bd=2, command=self.clear_screen, cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=280,y=425,width=100)
    
    # Within frame 1, it displays information about fast food information
    def show_info(self, row):
        self.clear_screen()
        No = Label(self.frame_1, text="No", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=40,y=30)
        No_data = Label(self.frame_1, text=row[0], font=(self.font_1, 15)).place(x=50, y=60)

        Brand = Label(self.frame_1, text="Brand", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=40,y=100)
        Brand_data = Label(self.frame_1, text=row[1], font=(self.font_1, 15)).place(x=50, y=130)

        Type = Label(self.frame_1, text="Type", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=300,y=100)
        Type_data = Label(self.frame_1, text=row[2], font=(self.font_1, 15)).place(x=310, y=130)

        Name = Label(self.frame_1, text="Name", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=560,y=100)
        Name_data = Label(self.frame_1, text=row[3], font=(self.font_1, 15)).place(x=570, y=130)

        Carbs = Label(self.frame_1, text="Carbs", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=40,y=170)
        Carbs_data = Label(self.frame_1, text=row[4], font=(self.font_1, 15)).place(x=50, y=200)

        Protein = Label(self.frame_1, text="Protein", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=300,y=170)
        Protein_data = Label(self.frame_1, text=row[5], font=(self.font_1, 15)).place(x=310, y=200)

        Fat = Label(self.frame_1, text="Fat", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=560,y=170)
        Fat_data = Label(self.frame_1, text=row[6], font=(self.font_1, 15)).place(x=570, y=200)

        Calo = Label(self.frame_1, text="Calo", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=820,y=170)
        Calo_data = Label(self.frame_1, text=row[7], font=(self.font_1, 15)).place(x=830, y=200)

        dataSource = Label(self.frame_1, text="Data Source", font=(self.font_2, 18, "bold"), bg=self.color_1, fg=self.color_4).place(x=40,y=240)
        dataSource_data = Label(self.frame_1, text=row[8], font=(self.font_1, 15)).place(x=50, y=270)

    # Updates fast food information
    def update_info(self, row):
        if self.Carbs_entry.get() == '' or self.Protein_entry.get() == '' or self.Fat_entry.get() == '' or self.Calo_entry.get() == '' or self.dataSource_entry.get() == '':
            messagebox.showerror("Error!", "All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("SELECT * FROM fast_food WHERE Name=%s", row[3])
                row=curs.fetchone()

                if row==None:
                    messagebox.showerror("Error!","The food doesn't exists",parent=self.window)
                else:
                    curs.execute("UPDATE fast_food set Carbs=%s, Protein=%s, Fat=%s, Calo=%s, DataSource=%s WHERE Name=%s",
                                        (
                                            self.Carbs_entry.get(),
                                            self.Protein_entry.get(),
                                            self.Fat_entry.get(),
                                            self.Calo_entry.get(),
                                            self.dataSource_entry.get(),
                                            row[3]
                                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been updated")
                    self.clear_screen()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    # Add the information of new food information
    def submit(self):
        if self.Name_entry.get() == '':
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from fast_food where Name=%s", self.Name_entry.get())
                row=curs.fetchone()

                if row!=None:
                    messagebox.showerror("Error!","The food name is already exists, please try again with another name",parent=self.window)
                else:
                    curs.execute("INSERT INTO fast_food (No, Brand, Type, Name, Carbs, Protein, Fat, Calo, DataSource) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                        (
                                            self.No_entry.get(),
                                            self.Brand_entry.get(),
                                            self.Type_entry.get(),
                                            self.Name_entry.get(),
                                            self.Carbs_entry.get(),
                                            self.Protein_entry.get(),
                                            self.Fat_entry.get(),
                                            self.Calo_entry.get(),
                                            self.dataSource_entry.get()
                                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been submitted")
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    # Reset all the entry fields
    def reset_fields(self):
        self.No_entry.delete(0, END)
        self.Brand_entry.delete(0, END)
        self.Type_entry.delete(0, END)
        self.Name_entry.delete(0, END)
        self.Carbs_entry.delete(0, END)
        self.Protein_entry.delete(0, END)
        self.Fat_entry.delete(0, END)
        self.Calo_entry.delete(0, END)
        self.dataSource_entry.delete(0, END)

# The main function
if __name__ == "__main__":
    root = Tk()
    obj = Management(root)
    root.mainloop()