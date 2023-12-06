import pygame
from pygame.locals import *
import Constants
import Button
import tkinter as tk
from tkinter import ttk

# the settings pop up window
class SettingsPopUp:
    def __init__(self, win):
        self.win = win
        self.root = tk.Tk()        
        self.root.title("Settings")
        self.root.geometry("300x400")
        self.root.protocol("WM_DELETE_WINDOW", self.hide_settings_popup)
        self.root.withdraw()
        self.pop_up_shown = False

        # settings icon
        self.root.iconbitmap("gear_retro.ico")

        # colors the background
        self.root.configure(bg="DarkOliveGreen3")

        # we will implement more buttons with different functionalities
        # created a button
        self.ok_button = tk.Button(
            self.root, 
            text="OK",
            #command=,
            font=("Franklin Gothic Book", 12, "bold"), 
            fg="green", 
            bg="white",
            width=14,
            borderwidth=3,
            )
        self.ok_button.pack(side=tk.BOTTOM, pady=10)

    # the pop up window appears on the screen
    def show_settings_popup(self):
        self.pop_up_shown = True
        self.root.deiconify()

    # the pop up window is hidden
    def hide_settings_popup(self):
        self.root.withdraw()
        self.pop_up_shown = False