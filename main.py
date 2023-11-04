# Import statements
import tkinter as tk
from tkinter import ttk


class Window(tk.Toplevel):
    def __init__(self, parent, title, type):
        super().__init__(parent)

        self.geometry("300x100")
        self.title(title)

        if type == "menu":
            ttk.Button(self,
                       text="Open a window",
                       command=lambda: root.open_window("Board", "board")).pack(expand=True)
        elif type == "board":
            ttk.Button(self,
                       text="Close this window",
                       command=self.destroy).pack(expand=True)
        elif type == "exit":
            ttk.Button(self,
                       text="Exit",
                       command=root.close_all).pack(side=tk.LEFT)
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

        # exitConfirmation = input("Are you sure you want to exit? Y/N")
        # if exitConfirmation == "Y" or exitConfirmation == "y":
        #     boardWindow.destroy()
        #     exchangeWindow.destroy()
        #     player1Window.destroy()
        #     player2Window.destroy()
        #     root.destroy()

    def open_window(self, title, type):
        window = Window(self, title, type)
        # window.grab_set()

        for child in self.winfo_children():
            if child.winfo_class() == "Toplevel":
                child.protocol("WM_DELETE_WINDOW", self.close_confirm)

        return window

    def close_confirm(self):
        self.open_window("Confirm exit?", "exit")


    # def create_bg(window):  # Function to create banner on each window
    #     backing = Frame(window, padx=10, pady=10)
    #     backing.grid(column=0, row=0, sticky="N W E S")
    #     return backing


# Calls close_all function when any window is closed manually
# boardWindow.protocol("WM_DELETE_WINDOW", close_all)
# exchangeWindow.protocol("WM_DELETE_WINDOW", close_all)
# player1Window.protocol("WM_DELETE_WINDOW", close_all)
# player2Window.protocol("WM_DELETE_WINDOW", close_all)

# Creates and hides the initial Tk() entity
if __name__ == "__main__":
    root = Root()
    # board.mainloop()

    menu = root.open_window("Main Menu", "menu")

    root.mainloop()
