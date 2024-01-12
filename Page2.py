import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import pandas as pd
import Page1

class Page2(tk.Frame):

  ##############
  # COMPONENTS #
  ##############

  labelTitle1 : ctk.CTkLabel = None

  labelCombo : ctk.CTkLabel = None
  combo : ctk.CTkComboBox = None

  textfieldExample : ctk.CTkEntry = None
  frameForPage2 : ctk.CTkFrame = None
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

    self.app.show_page(3)




  #######################
  # INITIALIZE THE PAGE #
  #######################
  def __init__(self, parent, app):
    tk.Frame.__init__(self, parent, bg='#A6BF93')
    self.app = app

    NORMALFONT = app.styles.get("NORMALFONT")
    LARGEFONT = app.styles.get("LARGEFONT")
    EXTRALARGEFONT = app.styles.get("EXTRALARGEFONT")
    MIDDLEFONT = app.styles.get("MIDDLEFONT")
    MINIFONT = app.styles.get('MINIFONT')


    # Label
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel
    self.labelTitle1 = ctk.CTkLabel(master=self, font = EXTRALARGEFONT, text="Homestimator")
    self.labelTitle1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    
    self.frameForPage2 = ctk.CTkFrame(master=self, width=300, height=300, corner_radius=30, bg_color='#A6BF93')
    self.frameForPage2.place(relx=0.5, rely=0.65, anchor = tk.CENTER)

    # Example of a dropdown menu
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkComboBox
    self.labelDropdown = ctk.CTkLabel(master=self, text= 'fields to train', font = LARGEFONT)
    self.labelDropdown.place(relx=0.5, rely=0.28, anchor=tk.CENTER)
    self.combo = ctk.CTkComboBox(master=self.frameForPage2)
    self.combo.place(relx=0.5, rely=0.37, anchor=tk.CENTER)
    # To set the options for the dropdown menu:
    self.combo.configure(values = ['vals', 'bf'])

    # Set the selected value to empty
    self.combo.set('')
    # To get the currently selected value:
    self.combo.get()


    # Button to go back
    #image for back button
    self.backButtonImg = ctk.CTkImage(Image.open('icons8-back-arrow-32.png'), size=(25,25))
    self.buttonBack = ctk.CTkButton(master=self, image=self.backButtonImg, text='',command= lambda : app.show_page(1), width=25, height=25, fg_color='transparent',hover_color='#90658B')
    self.buttonBack.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

    # Button to continue
    self.buttonContinue = ctk.CTkButton(master=self.frameForPage2, text="Continue", command= lambda : self.proceed(), fg_color='#90658B',text_color='#FFFFFF', font=NORMALFONT, hover_color='#361632')
    self.buttonContinue.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    
    #copyright label
    self.copyRightLabel = ctk.CTkLabel(master=self,text = " copy rights SApp Wizz c", 
                                          font = MINIFONT)
    self.copyRightLabel.place(relx=0.5, rely=0.98, anchor=tk.CENTER)