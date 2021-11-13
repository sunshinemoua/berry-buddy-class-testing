import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)

BERRY_NAME = ''

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        self.pages = (StartPage, Berry)

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Berry):
            frame = F(container, self, self.pages)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        # INITIAL PAGE ON APP LOAD
        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # passes text to the window StartPage
    def pass_on_text(self):
        self.frames[self.pages[1]].get_text("HELLO WORLD")


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller, pages):
        tk.Frame.__init__(self, parent)
        self.pages = pages
        self.controller = controller
        # self.pages = pages

        # label of frame Layout 2
        label = ttk.Label(self, text="Home Page", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        # # Update the listbox
        def update(data):
            # Clear the listbox so it can reset each time a new berry is entered
            myList.delete("0", "end")
            # Add berried top listbox
            for i, item in enumerate(data):
                # myList.insert(END, item)
                myList.insert(i, item)

        # Update entry box with listbox clicked
        def fillout(event):
            # Deletes anything in the entry box
            myEntry.delete(0, "end")

            # Add clicked list item to entry box
            myEntry.insert(0, myList.get("anchor"))
            global BERRY_NAME
            BERRY_NAME = myEntry.get()
        #
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
        button3 = ttk.Button(self, text="GO",
                             command=lambda: controller.show_frame(pages[1]))

        # putting the button in its place by
        # using grid
        button3.grid(row=3, column=1, padx=10, pady=10)


# WE ARE WORKING ON THIS PART 1
class Berry(tk.Frame):
    def __init__(self, parent, controller, pages):
        tk.Frame.__init__(self, parent)
        self.pages = pages
        self.controller = controller
        # self.pages = pages


        print("BERRY NAME DATA: ", self.controller)
        label = ttk.Label(self, text=Berries.berries, font=LARGEFONT)
        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Go Home",
                             command=lambda: controller.show_frame(pages[0]))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()