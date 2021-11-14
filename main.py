import tkinter as tk
from tkinter import ttk
import sqlite3 as sl

con = sl.connect("berries.db")

# sql = 'INSERT INTO BERRY (id, name, description) values(?, ?, ?)'
# data = [
#     (11, 'Raspberry', """Raspberries are members of the Rose family
# (Rosacea). The Rose family contains 110 genera and 3,000
# species worldwide. Species from forty-five of the genera are
# found in California. Raspberries belong to
# the Rubus genus, and there are 400 to 750 species of Rubus
# worldwide. There are eleven species of Rubus in California (not
# including varieties)."""),
#     (12, 'Serviceberry', """Serviceberry is a large shrub or small tree with
# deciduous leaves, often forming in dense thickets. The twigs
# of this native are glabrous, and the leaf is elliptical to round,
# with obvious serrations, generally serrated above the middle
# of the leaf. The flowers are five-petaled, white, fragrant, in
# clusters of a few to many. The fruit is a pome of two
# to five papery segments, berrylike, generally spherical, and
# bluish black in color."""),
#     (13, 'Strawberry', """If you've grown strawberries in your yard, you
# will recognize these three wild strawberries. The leaves are
# all basal, generally three-lobed, with each leaflet having fine
# teeth. It looks just the strawberry you grow in your garden,
# but smaller.
# Technically, the strawberry is an aggregate accessory fruit,
# meaning that the fleshy part is derived not from the plant's
# ovaries, but from the receptacle that holds the ovaries. In
# other words, what we call "the fruit" (because duh!, it looks
# like a fruit) is the receptacle, and all the little seeds on the
# outside of the "fruit" are technically referred to as achenes,
# actually one of the ovaries of the flower with a seed inside it."""),
#     (14, 'Toyon', """Toyon can grow to be a medium-size tree, and
# is probably most conspicuous in the winter when it's covered
# with clusters of orange-red fruits. The tree is found in the
# chaparral zones, and often planted on the fringes of the
# urban areas. The leaves are leathery and ovate, with toothed
# margins. The tree is evergreen and can be a large bush or a
# small tree. Each flower, which forms in the summer, is white
# and five-petaled, about ¼ inch wide. The clusters of orange-
# red fruit ripen from about November into January.""")
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
    # cont is the name of the frame we want to show
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller, pages):
        tk.Frame.__init__(self, parent)
        self.pages = pages
        self.controller = controller
        # self.pages = pages

        # label of frame Layout 2
        label = ttk.Label(self, text="Berry Buddy Catalog", font=LARGEFONT)
        label2 = ttk.Label(self, text="")
        label3 = ttk.Label(self, text="")

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        # # Update the listbox
        def update(data):
            # Clear the listbox so it can reset each time a new berry is entered
            myList.delete("0", "end")
            # Add berries top listbox
            # enumerate allows us to get the index
            # loop goes through the list of berries in the box
            for i, item in enumerate(data):
                # i is the index and item is the berry itself
                myList.insert(i, item)

        def resetLabelText():
            label2.config(text='')
            label3.config(text='')


        # Update entry box with listbox clicked
        def fillout(event):
            # Deletes anything in the entry box
            myEntry.delete(0, "end")

            # Add clicked list item to entry box
            myEntry.insert(0, myList.get("anchor"))
            global BERRY_NAME
            BERRY_NAME = myEntry.get()
            if BERRY_NAME in berryNames:
                with con:
                    data = con.execute(f"SELECT * FROM BERRY WHERE name == '{myEntry.get()}'")
                    result = data.fetchone()
                    if result:
                        label2.grid(row=1, column=5, padx=10, pady=10)
                        label2.config(text=result[1])
                        label3.config(text=result[2])
                        label3.grid(row=1, column=6, padx=5, pady=5)
                        # breaking... come back to fix because it is not destroying the labels, instead it is overlapping
                        button2 = ttk.Button(self, text="Quit", command=lambda: resetLabelText())
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
        berryNames = ['Gooseberry', 'Coffeeberry', 'Elderberry', 'Wild Grape', 'Cherry', 'Currant', 'Ground Cherry', 'Huckleberry',
                      'Juniper', 'Nightshade', 'Raspberry', 'Serviceberry', 'Strawberry', 'Toyon']
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
    def __init__(self, parent, controller, pages):
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