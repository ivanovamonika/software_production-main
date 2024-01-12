import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import pandas as pd
from PIL import Image, ImageTk
class Page3(tk.Frame):

  ##############
  # COMPONENTS #
  ##############

  labelTitle1 : ctk.CTkLabel = None

  labelCombo : ctk.CTkLabel = None
  combo : ctk.CTkComboBox = None

  textfieldExample : ctk.CTkEntry = None

  buttonBack : ctk.CTkButton = None
  buttonContinue : ctk.CTkButton = None

  ###################
  # STATE VARIABLES #
  ###################

  #############
  # FUNCTIONS #
  #############

  def proceed(self):
    print(f"In dropdown menu, user has selected value: {self.combo.get()}")

    self.app.show_page(4)
  
  def parameters(self):
    #we need to get the input from thr user here


    return

  #######################
  # INITIALIZE THE PAGE #
  #######################
  def __init__(self, parent, app):
    tk.Frame.__init__(self, parent, bg='#A6BF93')
    self.app = app

    EXTRALARGEFONT = app.styles.get('EXTRALARGEFONT')
    NORMALFONT = app.styles.get("NORMALFONT")
    LARGEFONT = app.styles.get("LARGEFONT")
    MIDDLEFONT = app.styles.get('MIDDLEFONT')
    MINIFONT = app.styles.get('MINIFONT')

    # Label
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel
    self.labelTitle1 = ctk.CTkLabel(master=self, font = EXTRALARGEFONT, text="Homestimator")
    self.labelTitle1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    
    self.frameForText = ctk.CTkFrame(master=self, width=400, height=500, corner_radius=50, bg_color='#A6BF93') #change to pink
    self.frameForText.place(relx=0.5, rely=0.65, anchor = tk.CENTER)

    #self.frameBubble = ctk.CTkFrame(master=self.frameForText, width=280, height=100, corner_radius = 30, fg_color='#DABDD6') #change to gray
    #self.frameBubble.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    # Example of a textfield
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkEntry
    self.labelText = ctk.CTkLabel(master=self, text="Type in your\ndesired parameters", font = MIDDLEFONT, bg_color='#DABDD6', fg_color='transparent')
    self.labelText.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    #text fields for parameters
    self.textfieldExample = ctk.CTkEntry(master=self.frameForText,
                                         width= 220,
                                         height= 30,
                                         corner_radius=0)
    self.textfieldExample.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

    
    self.textfieldExample = ctk.CTkEntry(master=self.frameForText,
                                         width= 220,
                                         height= 30,
                                         corner_radius=0)
    self.textfieldExample.place(relx=0.5, rely=0.30, anchor=tk.CENTER)

    
    self.textfieldExample = ctk.CTkEntry(master=self.frameForText,
                                         width= 220,
                                         height= 30,
                                         corner_radius=0)
    self.textfieldExample.place(relx=0.5, rely=0.40, anchor=tk.CENTER)

    
    self.textfieldExample = ctk.CTkEntry(master=self.frameForText,
                                         width= 220,
                                         height= 30,
                                         corner_radius=0)
    self.textfieldExample.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

    
    self.textfieldExample = ctk.CTkEntry(master=self.frameForText,
                                         width= 220,
                                         height= 30,
                                         corner_radius=0)
    self.textfieldExample.place(relx=0.5, rely=0.60, anchor=tk.CENTER)
    # To get the value of the textfield:
    #need to dynamically get the choice and
    #create the text fields
    self.textfieldExample.get()

    # Button to go back
    self.backButtonImg = ctk.CTkImage(Image.open('icons8-back-arrow-32.png'), size=(25,25))
    self.buttonBack = ctk.CTkButton(master=self, image=self.backButtonImg, text='',command= lambda : app.show_page(2), width=25, height=25, fg_color='transparent',hover_color='#90658B')
    self.buttonBack.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

    # Button to continue
    self.buttonContinue = ctk.CTkButton(master=self, text="Submit", command= lambda : self.proceed())
    self.buttonContinue.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    
    #copyright label
    self.copyRightLabel = ctk.CTkLabel(master=self.frameForText, text = " copy rights SApp Wizz c", 
                                          font = MINIFONT)
    self.copyRightLabel.place(relx=0.5, rely=0.896, anchor=tk.CENTER)