# Import statements
import tkinter as tk
from tkinter import ttk

#import PIL
#from PIL import ImageTk, Image

import random

#--------------------------------------------------------
# POSSIBLE TO-DO (non-obvious/undocumented features):   |
#--------------------------------------------------------
# - Player order tracker and/or turn tracker.           |
# - Options menu with save/cancel function              |
#       (documented but highly unfinished).             |
# - Manual saving/autosave function after               |
#       player activation (possibly save board          |
#       arrays/player info data in text files).         |
# - Savegame loading of ongoing games.                  |
#--------------------------------------------------------
# STRETCH GOALS:                                        |
#--------------------------------------------------------
# - Expansion pack content (5-6 player variant, cities  |
#       and knights, etc).                              |
#--------------------------------------------------------
# PERSONAL TO-DO (QoL stuff or "dev infrastructure"):   |
#--------------------------------------------------------
# - Change tile relationship doc to be self-updating.   |
#--------------------------------------------------------


# UNIVERSAL CONSTANTS
MIN_PLAYERS = 2
MAX_PLAYERS = 4


class BoardGeneration():
    def __init__(self, parent):
        super().__init__(parent)

        global boardTileArray
        boardTileArray = []


class Window(tk.Toplevel):
    def __init__(self, parent, title, type):
        super().__init__(parent)

        self.geometry("300x100")
        self.title(title)

        if type != "exit" and type != "invalid" and type != "options":
            self.protocol("WM_DELETE_WINDOW", root.close_confirm)

        if type == "menu":
            self.geometry("300x200")
            tk.Button(self,
                       text="Play Game",
                       command=lambda: [root.open_window("Game Setup", "setup"), self.withdraw()]).pack(side=tk.TOP, pady=10)
            tk.Button(self,
                       text="Options",
                       command=lambda: [root.open_window("Options", "options"), self.withdraw()]).pack()
            tk.Button(self,
                       text="Exit",
                       command=root.close_confirm).pack(side=tk.BOTTOM)

        elif type == "options":  # UNFINISHED
            tk.Button(self,
                       text="Save options",
                       command=lambda: [menu.deiconify(), self.destroy()]).pack(side=tk.LEFT)  # UNFINISHED
            tk.Button(self,
                       text="Cancel",
                       command=lambda: [menu.deiconify(), self.destroy()]).pack(side=tk.RIGHT)

        elif type == "setup":
            numPlayersStr = tk.StringVar()
            numPlayersEntry = tk.Entry(self, textvariable=numPlayersStr)
            numPlayersEntry.insert(0, "Enter the number of players, "+str(MIN_PLAYERS)+"-"+str(MAX_PLAYERS))
            numPlayersEntry.pack(expand=True, side=tk.TOP)

            def addPlayers():
                global numPlayers
                numPlayers = int(numPlayersEntry.get())
                if numPlayers <= MAX_PLAYERS and numPlayers >= MIN_PLAYERS:
                    root.open_window("Board", "board")
                    TEMPcreatePlayerWindows(numPlayers)
                    self.destroy()
                    #print(numPlayers)
                else:
                    root.open_window("Error", "playerCountError")
            
            def playerColorGen(window, color):
                window.configure(background=color)
                tk.Label(window,
                        text="Player Number "+str(currPlayerNum),
                        background=color).pack()
                # HIDES ALL OTHER PLAYERS + BOARD IF NO OTHER ACTION TAKEN FIRST -> Locks up if no other windows available/open
                tk.Button(window,
                        text="Close this window",
                        command=window.destroy).pack(side=tk.RIGHT)
            
            def TEMPcreatePlayerWindows(numPlayers):
                global currPlayerNum
                currPlayerNum = 1
                while currPlayerNum <= numPlayers:
                    newPlayerSheet = root.open_window("Player "+str(currPlayerNum), "playerSheet")
                    newPlayerSheet.geometry("200x400")

                    if currPlayerNum == 1:
                        playerColorGen(newPlayerSheet, "red")
                    elif currPlayerNum == 2:
                        playerColorGen(newPlayerSheet, "blue")
                    elif currPlayerNum == 3:
                        playerColorGen(newPlayerSheet, "orange")
                    elif currPlayerNum == 4:
                        playerColorGen(newPlayerSheet, "yellow")

                    # Extra player setup for if expansions are included
                    elif currPlayerNum == 5:
                        playerColorGen(newPlayerSheet, "green")
                    else:
                        playerColorGen(newPlayerSheet, "white")

                    currPlayerNum += 1

            tk.Button(self,
                       text="Continue",
                       command=lambda: addPlayers()).pack(side=tk.LEFT)  # UNFINISHED
            tk.Button(self,
                       text="Back",
                       command=lambda: [menu.deiconify(), self.destroy()]).pack(side=tk.RIGHT) # Hide menu and destroy setup page

        elif type == "board":
            self.geometry("600x600")
            tk.Button(self,
                       text="Open new window",
                       command=lambda: root.open_window("Board", "board")).pack(side=tk.LEFT)
            # HIDES ALL PLAYERS IF NO OTHER ACTION TAKEN FIRST -> Locks up if no other windows available/open
            tk.Button(self,
                       text="Close this window",
                       command=self.destroy).pack(side=tk.RIGHT)
        
            '''elif type == "playerSheet":
            self.geometry("200x400")
            ttk.Label(self,text="Player Number "+str(playerNum)).pack()
            # HIDES ALL OTHER PLAYERS + BOARD IF NO OTHER ACTION TAKEN FIRST -> Locks up if no other windows available/open
            ttk.Button(self,
                       text="Close this window",
                       command=self.destroy).pack(side=tk.RIGHT)'''
        
        elif type == "playerCountError": # Make a subclass of an error type?
            self.geometry("250x100")
            self.resizable(False,False)
            tk.Label(self,text=("Please enter a number of players between "+str(MIN_PLAYERS)+"-"+str(MAX_PLAYERS)+".")).pack()
            tk.Button(self,
                       text="OK",
                       command=self.destroy).pack(side=tk.BOTTOM)

        elif type == "exit":
            # If close is confirmed, calls close_all function
            tk.Label(self,text="Are you sure you want to close?").pack()
            tk.Button(self,
                       text="Close all windows",
                       command=root.close_all).pack(side=tk.LEFT)
            # If close is not confirmed, closes confirmation window
            tk.Button(self,
                       text="Back",
                       command=self.destroy).pack(side=tk.RIGHT)

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.withdraw()

    def close_all(self):  # Closes all windows, including hidden
        for child in self.winfo_children():
            child.destroy()
        self.destroy()

    def open_window(self, title, type):
        window = Window(self, title, type)
        if type == "exit" or type == "options" or type == "playerCountError":  # If exit confirmation window, forces user interaction
            window.grab_set()

        return window

    def close_confirm(self):  # Creates confirmation window
        self.open_window("Confirm exit?", "exit")
    
    # def hideNonActivePlayer(self, playerTurn):
    #    for child in self.winfo_children():
    #        if child.

    # def create_bg(window):  # Function to create banner on each window
    #     backing = Frame(window, padx=10, pady=10)
    #     backing.grid(column=0, row=0, sticky="N W E S")
    #     return backing


# Creates and hides the initial Tk() entity
if __name__ == "__main__":
    root = Root()

    menu = root.open_window("Main Menu", "menu")

    root.mainloop()
