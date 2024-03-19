# Import statements
import tkinter as tk
from tkinter import ttk
import random


numPlayers = 2


# class BoardGeneration():
#     def __init__(self, parent):
#         super().__init__(parent)


class Window(tk.Toplevel):
    def __init__(self, parent, title, type):
        super().__init__(parent)

        self.geometry("300x100")
        self.title(title)

        if type != "exit" and type != "invalid" and type != "options":
            self.protocol("WM_DELETE_WINDOW", root.close_confirm)

        if type == "menu":
            self.geometry("300x200")
            ttk.Button(self,
                       text="Play Game",
                       command=lambda: [root.open_window("Game Setup", "setup"), self.withdraw()]).pack(side=tk.TOP, pady=10)
            ttk.Button(self,
                       text="Options",
                       command=lambda: [root.open_window("Options", "options"), self.withdraw()]).pack()
            ttk.Button(self,
                       text="Exit",
                       command=root.close_confirm).pack(side=tk.BOTTOM)

        elif type == "options":  # UNFINISHED
            ttk.Button(self,
                       text="Save options",
                       command=lambda: [menu.deiconify(), self.destroy()]).pack(side=tk.LEFT)  # UNFINISHED
            ttk.Button(self,
                       text="Cancel",
                       command=lambda: [menu.deiconify(), self.destroy()]).pack(side=tk.RIGHT)

        elif type == "setup":
            numPlayersStr = tk.StringVar()
            numPlayersEntry = tk.Entry(self, textvariable=numPlayersStr)
            numPlayersEntry.insert(0, "Enter the number of players, 2-6")
            numPlayersEntry.pack(expand=True, side=tk.TOP)

            def addPlayers():
                global numPlayers
                numPlayers = int(numPlayersEntry.get())
                TEMPcreatePlayerWindows(numPlayers)
                #print(numPlayers)
            
            def TEMPcreatePlayerWindows(numPlayers):
                global playerNum
                playerNum = 1
                while playerNum <= numPlayers:
                    root.open_window("Player "+str(playerNum), "playerSheet")
                    playerNum += 1

            ttk.Button(self,
                       text="Continue",
                       command=lambda: [root.open_window("Board", "board"), addPlayers(), self.destroy()]).pack(side=tk.LEFT)  # UNFINISHED
            ttk.Button(self,
                       text="Back",
                       command=lambda: [menu.deiconify(), self.destroy()]).pack(side=tk.RIGHT)

        elif type == "board":
            self.geometry("600x600")
            ttk.Button(self,
                       text="Open new window",
                       command=lambda: root.open_window("Board", "board")).pack(side=tk.LEFT)
            # HIDES ALL PLAYERS IF NO OTHER ACTION TAKEN FIRST -> Locks up if no other windows available/open
            ttk.Button(self,
                       text="Close this window",
                       command=self.destroy).pack(side=tk.RIGHT)
        
        elif type == "playerSheet":
            self.geometry("200x400")
            ttk.Label(self, text="Player Number "+str(playerNum))
            # HIDES ALL OTHER PLAYERS + BOARD IF NO OTHER ACTION TAKEN FIRST -> Locks up if no other windows available/open
            ttk.Button(self,
                       text="Close this window",
                       command=self.destroy).pack(side=tk.RIGHT)

        elif type == "exit":
            # If close is confirmed, calls close_all function
            ttk.Button(self,
                       text="Close all windows",
                       command=root.close_all).pack(side=tk.LEFT)
            # If close is not confirmed, closes confirmation window
            ttk.Button(self,
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
        if type == "exit" or type == "options":  # If exit confirmation window, forces user interaction
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
