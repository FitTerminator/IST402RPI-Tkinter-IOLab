#Code utilizes references from PSU lectures, online, and LinkedIn learning.

from cgitb import text
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from turtle import title, width 
class Feedback: 
    def __init__(self, master): 
        master.title('Pennsylvania Neighboring State Visitor Feedback Form') 
        master.resizable(False, False) 
        master.configure(background = '#7d7d7d') 
        self.style = ttk.Style() 
        self.style.configure('TFrame', background = '#7d7d7d')
        self.style.configure('TButton', backaround = '#000000') 
        self.style.configure('TLabel', background = '#7d7d7d', font = ('Arial', 11)) 
        self.style.configure('header.TLabel', font = ('Arial', 18,'bold')) 

        
        self.frame_header=ttk.Frame(master)
        self.frame_header.pack()

        ttk.Label(self.frame_header,text='Thank You So Much for Your Visit!', style='Header.TLabel').grid(row=0,column=0, columnspan=3)
        ttk.Label(self.frame_header,wraplength=300,text="Do you have any comments or feedback about your experience? We would love to hear it below! Please be sure to leave your name and email so we can get back to you!").grid(row=1,column=1)
        self.frame_content=ttk.Frame(master)#content frame
        self.frame_content.pack()

        ttk.Label(self.frame_content,text='Name:').grid(row=0,column=0,padx=12,sticky='sw')
        ttk.Label(self.frame_content,text='Email:').grid(row=0,column=1,padx=12,sticky='sw')
        ttk.Label(self.frame_content,text='Comments:').grid(row=9,column=0,padx=5,sticky='sw')

        self.entry_name=ttk.Entry(self.frame_content,width=24)
        self.entry_email=ttk.Entry(self.frame_content,width=24)
        self.entry_comments=Text(self.frame_content,width=50,height=10,font=('Arial',10))

        self.entry_name.grid(row=1,column=0,padx=5)
        self.entry_email.grid(row=1,column=1,padx=5)
        self.entry_comments.grid(row=8,column=0,columnspan=2,padx=5)
        options=[
            "Ohio",
            "New York",
            "Virginia",
            "New Jersey",
            "Delaware"
        ]

        self.clicked=StringVar()
        self.clicked.set("(No State Selected)")

        ttk.Label(self.frame_content,text="Which Neighboring State Are You Visiting From?").grid(row=3,column=0,padx=5,sticky='sw')
        drop=OptionMenu(self.frame_content,self.clicked,*options).grid(row=3,column=1,padx=5, pady=3)

        self.radio=StringVar()
        ttk.Label(self.frame_content,text="Did You Enjoy Your Experience Visiting Us?").grid(row=4,column=0,padx=5,sticky='sw')

        radioBtn1=Radiobutton(self.frame_content,text="Yes",variable=self.radio,value='Yes').grid(row=4,column=1)
        radioBtn2=Radiobutton(self.frame_content,text="No",variable=self.radio,value='No').grid(row=4,column=3)

        self.check1=StringVar()
        self.check2=StringVar()
        ttk.Label(self.frame_content,text="During Your Trip, You Could Easily Find:").grid(row=5,column=0,padx=5,sticky='sw')

        checkBtn1 = Checkbutton(self.frame_content,text="Food",variable = self.check1,onvalue = 'Yes', offvalue = 'No', height = 2, width = 10).grid(row=5,column=1)
        checkBtn2 = Checkbutton(self.frame_content,text="Drinks",variable = self.check2,onvalue = 'Yes', offvalue = 'No', height = 2, width = 10).grid(row=5,column=3)

        ttk.Label(self.frame_content,text="Dump Options:").grid(row=6,column=0,padx=5,sticky='sw')
        ttk.Button(self.frame_content,text="JSON",command=self.JSON).grid(row=6,column=1,padx=5,pady=5,sticky='e')
        ttk.Button(self.frame_content,text="SQLite",command=self.SQLite).grid(row=6,column=2,padx=5,pady=5,sticky='e')
        ttk.Button(self.frame_content,text="flat",command=self.flat).grid(row=6,column=3,padx=5,pady=5,sticky='e')
        
        ttk.Button(self.frame_content,text="Submit",command=self.submit).grid(row=10,column=0,padx=5,pady=5,sticky='e')
        ttk.Button(self.frame_content,text="Clear",command=self.clear).grid(row=10,column=1,padx=5,pady=5,sticky='w')

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Visiting From: {}'.format(self.clicked.get()))
        print('Enjoyed Trip: {}'.format(self.radio.get()))
        print('Could Food Be Found: {}'.format(self.check1.get()))
        print('Could Drinks Be Found: {}'.format(self.check2.get()))
        print('Comments: {}'.format(self.entry_comments.get('1.0', END)))
        messagebox.showinfo(title='Pennsylvania Neighboring State Visitor Feedback Form',message='Thanks For Your Feedback!')
        self.clear()

    def JSON(self):
        import json
        
        class User:
            name = ' '
            email = ' '
            visitedfrom = ' '
            enjoyedtrip = ' '
            foundfood = ' '
            founddrink = ' '
            comments = ' ' 

        userinput = User()
        userinput.name = ('{}'.format(self.entry_name.get()))
        userinput.email = ('{}'.format(self.entry_email.get()))
        userinput.visitfrom = ('{}'.format(self.clicked.get()))
        userinput.enjoyedtrip = ('{}'.format(self.radio.get()))
        userinput.foundfood = ('{}'.format(self.check1.get()))
        userinput.founddrink = ('{}'.format(self.check2.get()))
        userinput.comments = ('{}'.format(self.entry_comments.get('1.0', END)))
        print(json.dumps(userinput.__dict__))
        out_file = open("L06.json", "w")
        json.dump(json.dumps(userinput.__dict__), out_file, indent = 6)
        

    def SQLite(self):

        import sqlite3

        db = sqlite3.connect('myDB.db') 
        cur = db.cursor() 
        cur.execute("drop table if exists test") 
        cur.execute("""
            create table test(
            string TEXT, 
            number INT
            )""") 
        cur.execute('insert into test(string, number) values ("one", 1)') 
        cur.execute('insert into test(string, number) values ("two", 2)') 
        cur.execute('insert into test(string, number) values ("three", 3)')
        for row in cur.execute('select * from test'):
            print(row) 
        db.close()

    def flat(self):
        output = open('L06.txt', 'w')
        output.write('Name: {}'.format(self.entry_name.get()))
        output.write('\nEmail: {}'.format(self.entry_email.get()))
        output.write('\nVisiting From: {}'.format(self.clicked.get()))
        output.write('\nEnjoyed Trip: {}'.format(self.radio.get()))
        output.write('\nCould Food Be Found: {}'.format(self.check1.get()))
        output.write('\nCould Drinks Be Found: {}'.format(self.check2.get()))
        output.write('\nComments: {}'.format(self.entry_comments.get('1.0', END)))
        output.close()

        
        
    def clear(self):
        self.entry_name.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_comments.delete("1.0", "end")

root = Tk()
feedback=Feedback(root)
root.mainloop()
