# Import statements
import tkinter as tk
from tkinter import ttk


class Window(tk.Toplevel):
    def __init__(self, parent, title, type):
        super().__init__(parent)

        self.geometry("300x100")
        self.title(title)

        if type != "exit" and type != "invalid":
            self.protocol("WM_DELETE_WINDOW", root.close_confirm)

        if type == "menu":
            ttk.Button(self,
                       text="Play Game",
                       command=lambda: [root.open_window("Board", "board"), self.withdraw()]).pack(side=tk.TOP)
            ttk.Button(self,
                       text="Exit",
                       command=root.close_confirm).pack(side=tk.BOTTOM)
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
                       text="Exit",
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
        if type == "exit":  # If exit confirmation window, forces user interaction
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
