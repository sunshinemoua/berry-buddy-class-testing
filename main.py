import tkinter as tk
from tkinter import ttk
import sqlite3 as sl

con = sl.connect("berries.db")

with con:
    con.execute("""
        CREATE TABLE BERRY (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT
        );
    """)

sql = 'INSERT INTO BERRY (id, name, description) values(?, ?, ?)'
data = [
    (1, 'Gooseberry', """Currants and gooseberries are both members of the Ribes genus, and do look very
    similar, though there are some important distinctions. They are both perennial
    bushes with somewhat vining stalks that arise from the roots. When cut back or
    burned back, the plant will send up many very straight stalks.
    The stalks of the gooseberries are covered in spines. The fruits of goose-berry are
    also covered in little spines. Currants, on the other hand, have no spines on the stalk
    or fruit. But both plants have the very same growth patterns, and leaves that look
    like a three-lobed mitten.
    I prefer the currants because they are easier to collect and have no spines. But
    both are useful, and both have their adherents.
    The fruits are small, but you can get a fair amount if you find a good patch and
    carefully pick away. You never seem to be able to gather as much as you want. For
    one thing, the fruits don't usually all ripen at the same time."""),
    (2, 'Coffeeberry', """California coffeeberry is a member of the Buckthorn family
    (Rhamnaceae). There are fifty to fifty-two genera of the
    Buckthorn family worldwide, with about 950 species.
    There are fifty species of the Frangula genus, with three
    species found in California. Aside from the two species listed
    above, there is Frangula rubra, or Sierra coffeeberry.
    Description: F. californica and its six subspecies are most
    common in Southern California; F. purshiana and its three
    subspecies are found more commonly in the northern part of
    California. These are small shrubs to large trees, depending on
    location and species. F. californica is typically no more than
    8 feet tall, whereas F. purshiana is significantly taller, very
    treelike. The leaves are alternately arranged, an inch or two
    in length, typically bright green, narrowly oblong, with tiny
    teeth on the margins."""),
    (3, 'Elderberry', """The elderberry is a member of the Muskroot family(Adoxaceae). This family has five genera and about 200
    species worldwide. Only two of the genera are represented
    in California, one of which is Sambucus. There are twenty
    species of Sambucus worldwide, and according to the
    latest classification, you'll find four types of elderberries in
    California."""),
    (4, 'Wild Grape', """Native wild grapes belong to the Grape family (Vitaceae). The
    Grape family has about fifteen genera and about 800 species
    worldwide. In California, this family is represented by only
    two genera, Parthenocissus (the Virginia creeper) and Vitis
    (grapes). Though there are sixty-five known species of Vitis, it
    is only represented in California by three species, one of which
    is the introduced cultivated grape (V. vinifera). The other two
    are the California wild grape (V. californica) and the desert
    wild grape (V. girdiana)."""),
    (5, 'Cherry', """Wild cherries are members of the Rose family (Rosaceae),
    which contains 110 genera and 3,000 species worldwide.
    Species from forty-five of the genera are found in California.
    Wild cherries are members of the Prunus genus, of which
    there are about 400 species worldwide. There are eleven
    species of Prunus in California, including cherry, almond,
    apricot, and plum, but we're only concerned with the cherries here."""),
    (6, 'Currant', """These are vining or shrublike plants, often with
    many long and arching branches arising from a common root.
    Flower colors vary, depending on species, and can be yellow,
    orange, red, and more. The fruit is a berry, with small bristles
    in the case of the gooseberry. Generally, the petals form a
    tube, and when the fruit matures, the dried flower is often
    persistent on the end of the fruit."""),
    (7, 'Ground Cherry', """Ground cherry is a member of the Nightshade family
    (Solanaceae), which consists of at least seventy-five genera
    and about 3,000 species worldwide. Physalis is one of the
    thirteen genera of the Nightshade family found in California.
    Physalis contains about eighty-five species worldwide, with
    seven species (not including varieties) found in California,
    four of which are native. At least one is regarded as a noxious
    weed, and one nonnative is the widely cultivated tomatillo (P.philadelphica). 
    Thus, in the pre-Spanish days, the only ground
    cherries eaten by the desert indigenous peoples would have
    been P. acutifolia, P. crassifolia, P. hederifolia (and its two
    varieties), and P. lobata. The last one, commonly called the
    lobed ground cherry, is not common in California. The first
    three have yellow flowers, and P. lobata has purple flowers."""),
    (8, 'Huckleberry', """Huckleberry is a member of the Heath family (Ericaceae).
    This family contains about one hundred genera and 3,000
    species worldwide. In California, there are twenty-six genera.
    The Vaccinium genus includes more than 400 species in the
    world, with eight in California. In general, Vaccinium are
    referred to as huckleberries, blueberries, cranberries, and even
    bilberries, depending on the species. All are native, except V.
    macrocarpon, which is the common cranberry."""),
    (9, 'Juniper', """Juniper is a member of the Cypress family (Cupressaceae),
    which has thirty genera and more than 130 species worldwide. Only seven genera 
    are found in California.There are about sixty-seven species of Junipers in the
    Northern Hemisphere. In California, we have just five species of juniper, all
     of which are considered native, including the Utah juniper V. osteosperma)."""),
    (10, 'Nightshade', """The western black nightshade plant is somewhat common
    throughout the chaparral regions, and is not uncommon throughout developed 
    urban areas. I've seen some in the desert, some at the beach, though rarely
     in the high elevations of the mountains. It is sometimes even cultivated."""),
    (11, 'Raspberry', """Raspberries are members of the Rose family
    (Rosacea). The Rose family contains 110 genera and 3,000
    species worldwide. Species from forty-five of the genera are
    found in California. Raspberries belong to the Rubus genus, 
    and there are 400 to 750 species of Rubus worldwide. There are 
    eleven species of Rubus in California (not including varieties)."""),
    (12, 'Serviceberry', """Serviceberry is a large shrub or small tree with
deciduous leaves, often forming in dense thickets. The twigs
of this native are glabrous, and the leaf is elliptical to round,
with obvious serrations, generally serrated above the middle
of the leaf. The flowers are five-petaled, white, fragrant, in
clusters of a few to many. The fruit is a pome of two
to five papery segments, berrylike, generally spherical, and
bluish black in color."""),
    (13, 'Strawberry', """If you've grown strawberries in your yard, you
will recognize these three wild strawberries. The leaves are
all basal, generally three-lobed, with each leaflet having fine
teeth. It looks just the strawberry you grow in your garden,
but smaller.
Technically, the strawberry is an aggregate accessory fruit,
meaning that the fleshy part is derived not from the plant's
ovaries, but from the receptacle that holds the ovaries. In
other words, what we call "the fruit" (because duh!, it looks
like a fruit) is the receptacle, and all the little seeds on the
outside of the "fruit" are technically referred to as achenes,
actually one of the ovaries of the flower with a seed inside it."""),
    (14, 'Toyon', """Toyon can grow to be a medium-size tree, and
is probably most conspicuous in the winter when it's covered
with clusters of orange-red fruits. The tree is found in the
chaparral zones, and often planted on the fringes of the
urban areas. The leaves are leathery and ovate, with toothed
margins. The tree is evergreen and can be a large bush or a
small tree. Each flower, which forms in the summer, is white
and five-petaled, about ¼ inch wide. The clusters of orange-
red fruit ripen from about November into January.""")
]

with con:
    con.executemany(sql, data)

with con:
    data = con.execute("SELECT * FROM BERRY")
    for row in data:
        print(row)

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