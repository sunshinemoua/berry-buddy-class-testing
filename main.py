import tkinter as tk
from tkinter import ttk
import sqlite3 as sl

con = sl.connect("berries.db")

# sql = 'INSERT INTO BERRY (id, name, description) values(?, ?, ?)'
# data = [
#     (2, 'Coffeeberry', """California coffeeberry is a member of the Buckthorn family
# (Rhamnaceae). There are fifty to fifty-two genera of the
# Buckthorn family worldwide, with about 950 species.
# There are fifty species of the Frangula genus, with three
# species found in California. Aside from the two species listed
# above, there is Frangula rubra, or Sierra coffeeberry.
# Description: F. californica and its six subspecies are most
# common in Southern California; F. purshiana and its three
# subspecies are found more commonly in the northern part of
# California. These are small shrubs to large trees, depending on
# location and species. F. californica is typically no more than
# 8 feet tall, whereas F. purshiana is significantly taller, very
# treelike. The leaves are alternately arranged, an inch or two
# in length, typically bright green, narrowly oblong, with tiny
# teeth on the margins."""),
#     (3, 'Elderberry', """The elderberry is a member of the Muskroot family(Adoxaceae). This family has five genera and about 200
# species worldwide. Only two of the genera are represented
# in California, one of which is Sambucus. There are twenty
# species of Sambucus worldwide, and according to the
# latest classification, you'll find four types of elderberries in
# California."""),
# ]
#
# with con:
#     con.executemany(sql, data)
#
# with con:
#     data = con.execute("SELECT * FROM BERRY")
#     for row in data:
#         print(row)

LARGEFONT = ("Verdana", 28)

BERRY_NAME = ''

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # tk.Tk
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        self.pages = (StartPage, Berry)

        # iterating through a tuple consisting of the different page layouts
        for F in (StartPage, Berry):
            frame = F(container, self, self.pages)
            frame['bg'] = 'pink'

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        # INITIAL PAGE ON APP LOAD
        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont, n=None):
        frame = self.frames[cont]
        self.argumentName = n
        frame.tkraise()
        if n:
            frame.arg = n


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller, pages):
        tk.Frame.__init__(self, parent)
        self.pages = pages
        self.controller = controller
        # self.pages = pages

        # label of frame Layout 2
        label = ttk.Label(self, text="Berry Buddy Catalog", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        # # Update the listbox
        def update(data):
            # Clear the listbox so it can reset each time a new berry is entered
            myList.delete("0", "end")
            # Add berried top listbox
            for i, item in enumerate(data):
                myList.insert(i, item)

        def destroyAll(label2, label3):
            label2.destroy()
            label3.destroy()

        # Update entry box with listbox clicked
        def fillout(event):
            # Deletes anything in the entry box
            myEntry.delete(0, "end")

            # Add clicked list item to entry box
            myEntry.insert(0, myList.get("anchor"))
            global BERRY_NAME
            BERRY_NAME = myEntry.get()
            if BERRY_NAME in berryNames:
                label2 = ttk.Label(self, text=myEntry.get(), font=LARGEFONT)
                label2.grid(row=1, column=5, padx=10, pady=10)
                with con:
                    data = con.execute(f"SELECT * FROM BERRY WHERE name == '{myEntry.get()}'")
                    result = data.fetchone()
                    if result:
                        label3 = ttk.Label(self, text=result[2])
                        label3.grid(row=1, column=6, padx=5, pady=5)
                button2 = ttk.Button(self, text="Quit", command=lambda: destroyAll(label2, label3))
                button2.grid(row=1, column=7, padx=10, pady=10)

        # # Create function to check entry vs listbox
        def check(event):
            # Grab what was typed
            typed = myEntry.get()
            if typed == '':
                # The berryNames list will show up if there is nothing in the search bar
                data = berryNames
            else:
                data = []
                for item in berryNames:
                    if typed.lower() in item.lower():
                        data.append(item)

            # Updates our listbox with selected items
            update(data)

        # # Created entry box
        myEntry = tk.Entry(self, font=('Helvetica', 20))
        myEntry.grid(row=1, column=4, padx=10, pady=10)
        #
        # # Create a list box
        myList = tk.Listbox(self, width=50)
        myList.grid(row=2, column=4, padx=10, pady=40)
        #
        # Create a list of berries
        berryNames = ['Coffeeberry', 'Gooseberry', 'Elderberry', 'Wild Grape', 'Ground Cherry',
                      'Huckleberry']
        #
        # # Add berryNames to list
        update(berryNames)
        #
        # # Create a binding on the listbox onclick... predicts entry based on what is in the listbox
        myList.bind('<<ListboxSelect>>', fillout)
        #
        # # Create a binding on the entry box
        myEntry.bind('<KeyRelease>', check)


        ## button to show frame 2 with text layout2
        # button3 = ttk.Button(self, text="GO",
        #                      command=lambda: controller.show_frame(Berry, myEntry.get()))

        # putting the button in its place by
        # using grid
        # button3.grid(row=3, column=1, padx=10, pady=10)


# WE ARE WORKING ON THIS PART 1
class Berry(tk.Frame):
    def __init__(self, parent, controller, pages, attr=None):
        tk.Frame.__init__(self, parent)
        self.pages = pages
        self.controller = controller

        label = ttk.Label(self, text="SHOWING TEXT", font=LARGEFONT)
        # putting the grid in its place by using grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Go Home", command=lambda: controller.show_frame(pages[0]))

        # putting the button in its place by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()