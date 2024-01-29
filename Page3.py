import tkinter as tk
from tkinter import ttk
import threading
import customtkinter as ctk
import pandas as pd
from PIL import Image, ImageTk
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


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
    
  
  def on_show(self):
    #we need to get the input from the user here
    print("showing page 3")
    #loading the data
    df = pd.read_csv(self.app.selectedFilePath)
    #training on the chosen value
    x = df.drop(self.app.userChoice, axis=1)
    y = df[self.app.userChoice]
    #splitting the data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    #creating the model
    model=RandomForestRegressor(n_estimators=100, random_state=42)
    #training the model
    model.fit(x_train, y_train)
    # Make predictions
    pred = model.predict(x_test)
    mse = mean_squared_error(y_test, pred)
    r2 = r2_score(y_test, pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R² Score: {r2}")

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
    self.textfieldZipCode = ctk.CTkEntry(master=self.frameForText,
                                         width= 220,
                                         height= 30,
                                         corner_radius=0)
    self.textfieldZipCode.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

    
    self.textfieldSquareM = ctk.CTkEntry(master=self.frameForText,
                                         width= 220,
                                         height= 30,
                                         corner_radius=0)
    self.textfieldSquareM.place(relx=0.5, rely=0.30, anchor=tk.CENTER)

    
    self.textfieldAcreSize = ctk.CTkEntry(master=self.frameForText,
                                         width= 220,
                                         height= 30,
                                         corner_radius=0)
    self.textfieldAcreSize.place(relx=0.5, rely=0.40, anchor=tk.CENTER)

    
    self.textfieldNBedrooms = ctk.CTkEntry(master=self.frameForText,
                                         width= 220,
                                         height= 30,
                                         corner_radius=0)
    self.textfieldNBedrooms.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

    
    self.textfieldNBathrooms = ctk.CTkEntry(master=self.frameForText,
                                         width= 220,
                                         height= 30,
                                         corner_radius=0)
    self.textfieldNBathrooms.place(relx=0.5, rely=0.60, anchor=tk.CENTER)
    # To get the value of the textfield:
    #need to dynamically get the choice and
    #create the text fields
    self.textfieldZipCode.get()
    self.textfieldSquareM.get()
    self.textfieldAcreSize.get()
    self.textfieldNBedrooms.get()
    self.textfieldNBathrooms.get()

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
