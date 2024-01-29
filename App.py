import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from Page1 import Page1
from Page2 import Page2
from Page3 import Page3
from Page4 import Page4


class App(tk.Tk):

  ################
  # APP SETTINGS #
  ################
  #height and width is done to match size of iPhone screen
  name = "Homestimstor App"                      # Name of the app
  width = 400                               # Width of the app window
  height = 600                              # Height of the app window
  pages = [ Page1, Page2, Page3, Page4 ]           # Pages of the app
  initial_page = 1                          # Initial page to show, from 1 to upwards

  # Custom styles for the app
  styles = {
    "EXTRALARGEFONT": ("Verdana", 35),
    "LARGEFONT": ("Courier", 38),
    "MIDDLEFONT": ("Courier", 25),
    "NORMALFONT": ("Courier", 15),
    "MINIFONT" : ("Courier", 9)
  }

  ###################
  # STATE VARIABLES #
  ###################

  # Global selected option example
  selectedFilePath = ""

  #Global Column names from the selected CSV file
  columnNames = []

  userChoice = ""

  checkboxes = {}
  #############
  # FUNCTIONS #
  #############

  # Show a certain page, from 1 to upwards
  def show_page(self, page_number : int):
    self.frames.get(page_number).tkraise()
    self.frames.get(page_number).on_show()
  
  # Get a certain page, from 1 to upwards
  def get_page(self, page_number : int):
    return self.frames.get(page_number)
  
  


  ######################
  # INITIALIZE THE APP #
  ######################
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    
    # creating a container
    container = tk.Frame(self, bg='#A6BF93') 
    container.pack(side = "top", fill = "both", expand = True)
    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)
    self.geometry(f"{self.width}x{self.height}")
    self.title(self.name)
    self.resizable(False, False)




    # Theme settings for the app
    # https://github.com/TomSchimansky/CustomTkinter/wiki/Themes
    #ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
    #ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    # Create all the pages
    self.frames = {}
    i : int = 1
    for F in self.pages:
      frame = F(container, self)
      self.frames[i] = frame
      frame.grid(row = 0, column = 0, sticky ="nsew")
      i = i + 1
    
    # Initial page to show
    self.show_page(self.initial_page)
