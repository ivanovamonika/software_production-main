import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import pandas as pd
from PIL import ImageTk, Image


class Page1(tk.Frame):

  ##############
  # COMPONENTS #
  ##############

  labelTitle : ctk.CTkLabel = None
  labelSelectedFile : ctk.CTkLabel = None
  buttonSelectFile : ctk.CTkButton = None
  buttonContinue : ctk.CTkButton = None
  frameForButtons : ctk.CTkFrame = None
  subTitle : ctk.CTkLabel = None


  ###################
  # STATE VARIABLES #
  ###################

  #############
  # FUNCTIONS #
  #############

  def selectFile(self):
    #Opening a file dialog and get the selected file path
    self.app.selectedFilePath = ctk.filedialog.askopenfile(title="Open File", filetypes=(("Open a .csv file", "*.csv"), ("All files", "*.*"))).name

    
  def proceed(self):
    # Check if a file has been selected
    if self.app.selectedFilePath == "":
      # Show a warning message
      tk.messagebox.showwarning("No File Selected", "Please select a CSV file before continuing.")
      return
    
    # Read the CSV file using pandas
    df = pd.read_csv(self.app.selectedFilePath)

    # Get and save the column names into a list and save them for future use
    self.app.columnNames = (df.columns).tolist()
    for i in range(len(self.app.columnNames)):
      self.app.columnNames[i] = self.app.columnNames[i].replace("_", " ")
    #check to see if it worked
    print(self.app.columnNames)

    #switching to page 2
    self.app.show_page(2)

  def on_show(self):
    print("Showing page 1")

  
      
  #######################
  # INITIALIZE THE PAGE #
  #######################
  def __init__(self, parent, app):
    tk.Frame.__init__(self, parent, bg='#A6BF93')
    self.app = app

    NORMALFONT = app.styles.get("NORMALFONT")
    LARGEFONT = app.styles.get("LARGEFONT")
    EXTRALARGEFONT = app.styles.get("EXTRALARGEFONT")
    MINIFONT = app.styles.get('MINIFONT')

  
    # Title of app label
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel
    self.labelTitle = ctk.CTkLabel(master=self, font = EXTRALARGEFONT, text="Homestimator")
    self.labelTitle.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    # Label for selected file
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel    
    self.subTitle= ctk.CTkLabel(master=self, 
                  
                                          text = " Upload CSV file\n with house data", 
                                          font = LARGEFONT)
    self.subTitle.place(relx=0.5, rely=0.28, anchor=tk.CENTER)
    

    #button
    
    self.frameForButtons = ctk.CTkFrame(master=self, width=300, height=300, corner_radius=30, bg_color='#A6BF93')
    self.frameForButtons.place(relx=0.5, rely=0.65, anchor = tk.CENTER)

    # Button to select a file, calls the selectFile function inside this class
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkButton
    self.buttonSelectFile = ctk.CTkButton(master=self.frameForButtons, text="Select CSV File", command = lambda : self.selectFile(), fg_color='#90658B', text_color='#FFFFFF', compound='top', font=NORMALFONT, hover_color='#361632')
    self.buttonSelectFile.place(relx=0.5, rely=0.40, anchor=tk.CENTER)

    # Button to continue to the next page, calls the proceed function inside this class
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkButton
    self.buttonContinue = ctk.CTkButton(master=self.frameForButtons, text="Continue", command= lambda : self.proceed(), fg_color='#90658B',text_color='#FFFFFF', font=NORMALFONT, hover_color='#361632')
    self.buttonContinue.place(relx=0.5, rely=0.60, anchor=tk.CENTER)

    #copyright label
    self.copyRightLabel = ctk.CTkLabel(master=self,text = " copy rights SApp Wizz c", 
                                          font = MINIFONT)
    self.copyRightLabel.place(relx=0.5, rely=0.98, anchor=tk.CENTER)
  
      
