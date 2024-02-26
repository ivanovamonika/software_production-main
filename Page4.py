import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import pandas as pd

class Page4(tk.Frame):
  
  ##############
  # COMPONENTS #
  ##############

  labelTitle1 : ctk.CTkLabel = None
  labelTitle2 : ctk.CTkLabel = None
  buttonContinue : ctk.CTkButton = None
  sliderLabel : ctk.CTkLabel = None
  slider : ctk.CTkSlider = None
  switch : ctk.CTkSwitch = None

  ###################
  # STATE VARIABLES #
  ###################

  #############
  # FUNCTIONS #
  #############

  def proceed():
    return
  

  def on_show(self):
    #converting the user inputs
    inputsList = [float(self.app.checkboxes.get('house_size', 0)),
                  float(self.app.checkboxes.get('acre_lot', 0)),
                 int(self.app.checkboxes.get('bed', 0)),
                 int(self.app.checkboxes.get('bath', 0)),
                 int(self.app.checkboxes.get('zip_code', 0))]
    #predicting with real user inputs
    if self.app.model:
      userInputs=inputsList
      predictedPrice=self.app.model.predict([userInputs])
      self.predictionLabel.configure(text=f"${predictedPrice[0]:,.2f}")

    #if model wasn't created
    else:
      self.predictionLabel.configure(text="Model not available.")
      #we need to get the input from the user here
      print("showing page 4")
      return
  

  
  


  #######################
  # INITIALIZE THE PAGE #
  #######################
  def __init__(self, parent, app):
    tk.Frame.__init__(self, parent, bg='#A6BF93')
    self.app = app

    EXTRALARGEFONT = app.styles.get('EXTRALARGEFONT')
    LARGEFONT = app.styles.get('LARGEFONT')
    MINIFONT = app.styles.get('MINIFONT')
    MIDDLEFONT = app.styles.get('MIDDLEFONT')

    
    self.congratsImg = ctk.CTkImage(Image.open('congratsImg.png'), size=(360,520))

    self.imgLabel= ctk.CTkLabel(master=self, image=self.congratsImg, text='', fg_color='transparent')
    self.imgLabel.place(relx=0.3, rely=0.6, anchor=tk.CENTER)

    self.circleImg=ctk.CTkImage(Image.open('icons8-circle-50.png'), size =(150,150))
    self.predictionLabel=ctk.CTkLabel(master=self, text='Price: $0', image=self.circleImg, font=MIDDLEFONT)
    self.predictionLabel.place(relx=0.7, rely=0.45, anchor=tk.CENTER)

    self.labelTitle1 = ctk.CTkLabel(master=self, font = LARGEFONT, text="Congratulations!")
    self.labelTitle1.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    self.labelTitle2 = ctk.CTkLabel(master=self, font = MIDDLEFONT, text="Your home’s \n estimated price is!")
    self.labelTitle2.place(relx=0.5, rely=0.27, anchor=tk.CENTER)

    #back button with arrow image
    self.backButtonImg = ctk.CTkImage(Image.open('icons8-back-arrow-32.png'), size=(25,25))
    self.buttonBack = ctk.CTkButton(master=self, image=self.backButtonImg, text='',command= lambda : app.show_page(3), width=25, height=25, fg_color='transparent',hover_color='#90658B')
    self.buttonBack.place(relx=0.1, rely=0.1, anchor=tk.CENTER)


    #copyright label
    self.copyRightLabel = ctk.CTkLabel(master=self, text = " copy rights SApp Wizz c", 
                                          font = MINIFONT)
    self.copyRightLabel.place(relx=0.5, rely=0.98, anchor=tk.CENTER)
