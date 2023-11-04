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
            ttk.Button(self,
                       text="Play Game",
                       command=lambda: [root.open_window("Game Setup", "setup"), self.withdraw()]).pack(side=tk.TOP)
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
                #print(numPlayers)

            ttk.Button(self,
                       text="Continue",
                       command=lambda: [root.open_window("Board", "board"), addPlayers(), self.destroy()]).pack(side=tk.LEFT)  # UNFINISHED
            ttk.Button(self,
                       text="Back",
                       command=lambda: [menu.deiconify(), self.destroy()]).pack(side=tk.RIGHT)

        elif type == "board":
            ttk.Button(self,
                       text="Open new window",
                       command=lambda: root.open_window("Board", "board")).pack(side=tk.LEFT)
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

    # def get_num_players(self):

    # def create_bg(window):  # Function to create banner on each window
    #     backing = Frame(window, padx=10, pady=10)
    #     backing.grid(column=0, row=0, sticky="N W E S")
    #     return backing


# Creates and hides the initial Tk() entity
if __name__ == "__main__":
    root = Root()

    menu = root.open_window("Main Menu", "menu")

    root.mainloop()
