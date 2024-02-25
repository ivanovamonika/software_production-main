import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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
    df = pd.read_csv(self.app.selectedFilePath)
    userZipCode = self.textfieldZipCode.get()
    
    print(df['zip_code'])
    zipCodeList = df['zip_code'].tolist()
    self.app.checkboxes = {"bed" : self.textfieldNBedrooms.get(),
    "bath" : self.textfieldNBathrooms.get(),
    "house_size" : self.textfieldSquareM.get(),
    "acre_lot" : self.textfieldAcreSize.get(),
    "zip_code" : self.textfieldZipCode.get()
}
    
    print(self.app.checkboxes)
            # Validation for the ZipCode (must be an integer)
    if not userZipCode.isdigit():
        messagebox.showwarning("Error", "The zip code must be a number.")
        return
    else:
        intZipCode = int(userZipCode)
        if intZipCode not in zipCodeList:
            messagebox.showwarning("Error", "The zip code does not exist in the CSV file.")
            return
     
    try:
        float(self.textfieldSquareM.get())
    except ValueError:
        messagebox.showerror("Error", "Square Meters must be a number.")
        return
    try:
        float(self.textfieldAcreSize.get())
    except ValueError:
        messagebox.showerror("Error", "Acre lot must be a number.")
        return
    
    if not self.textfieldNBedrooms.get().isdigit():
        messagebox.showerror("Error", "Number of Bedrooms must be a number.")
        return
    if not self.textfieldNBathrooms.get().isdigit():
      messagebox.showerror("Error", "Number of Bathrooms must be a number.")
      return
    

       
        #trying to not load the model every time i go back and forth to the page but it didn't work
    self.app.show_page(4)



  def on_show(self):
    self.app.model = None
    if self.app.model is None:
      #transforming user choice to format of original dataframe
      self.app.userChoice = self.app.userChoice.replace(' ', '_')
      print("showing page 3")
      #loading the data
      df = pd.read_csv(self.app.selectedFilePath)
      #training on the chosen value
      x = df.drop(self.app.userChoice, axis=1)
      y = df[self.app.userChoice]
      #splitting the data
      x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
      #creating the model
      self.app.model=RandomForestRegressor(n_estimators=100, random_state=42)
      #training the model
      self.app.model.fit(x_train, y_train)
      # Make predictions
      pred = self.app.model.predict(x_test)
      mse = mean_squared_error(y_test, pred)
      r2 = r2_score(y_test, pred)

      print(f"Mean Squared Error: {mse}")
      print(f"R² Score: {r2}")

      return
    else:
       print("Model already exists.")
    print('Showing Page 3')


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
    #tried to do it dynamically but it didn't work this way
    #for i in range(3): #len(self.app.columnNames)
    #  self.textfield = ctk.CTkEntry(master=self.frameForText,
    #                                     width= 220,
    #                                     height= 30,
    #                                     corner_radius=0)
    #  self.textfield.place(relx=0.5, rely=0.20+i*10, anchor=tk.CENTER)
    #  #self.textfield.set(i)
    #  self.app.myEntries.append(self.textfield)

    #zipcode entry field and label
    self.ZipCodeL = ctk.CTkLabel(master=self.frameForText, text= 'zip code:', font = NORMALFONT)
    self.ZipCodeL.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
    self.textfieldZipCode= ctk.CTkEntry(master=self.frameForText,
                                         width= 220,
                                         height= 30,
                                         corner_radius=0)
    self.textfieldZipCode.place(relx=0.5, rely=0.20, anchor=tk.CENTER)
    
    #squaremeter field and label
    self.SML = ctk.CTkLabel(master=self.frameForText, text= 'square m:', font = NORMALFONT)
    self.SML.place(relx=0.5, rely=0.26, anchor=tk.CENTER)
    self.textfieldSquareM = ctk.CTkEntry(master=self.frameForText,
                                         width= 220,
                                         height= 30,
                                         corner_radius=0)
    self.textfieldSquareM.place(relx=0.5, rely=0.31, anchor=tk.CENTER)

    #acre size entry field and label
    self.AcreSize = ctk.CTkLabel(master=self.frameForText, text= 'acre size:', font = NORMALFONT)
    self.AcreSize.place(relx=0.5, rely=0.37, anchor=tk.CENTER)
    self.textfieldAcreSize = ctk.CTkEntry(master=self.frameForText,
                                         width= 220,
                                         height= 30,
                                         corner_radius=0)
    self.textfieldAcreSize.place(relx=0.5, rely=0.42, anchor=tk.CENTER)
 
    #number of bedrooms field and label
    self.NBedrooms = ctk.CTkLabel(master=self.frameForText, text= 'bedrooms:', font = NORMALFONT)
    self.NBedrooms.place(relx=0.5, rely=0.48, anchor=tk.CENTER) 
    self.textfieldNBedrooms = ctk.CTkEntry(master=self.frameForText,
                                         width= 220,
                                         height= 30,
                                         corner_radius=0)
    self.textfieldNBedrooms.place(relx=0.5, rely=0.53, anchor=tk.CENTER)

    #number of bathrooms entryfield and label
    self.NBathrooms = ctk.CTkLabel(master=self.frameForText, text= 'bathrooms:', font = NORMALFONT)
    self.NBathrooms.place(relx=0.5, rely=0.59, anchor=tk.CENTER)
    self.textfieldNBathrooms = ctk.CTkEntry(master=self.frameForText,
                                         width= 220,
                                         height= 30,
                                         corner_radius=0)
    self.textfieldNBathrooms.place(relx=0.5, rely=0.64, anchor=tk.CENTER)

    
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
