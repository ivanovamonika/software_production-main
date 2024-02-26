## Home estimator

Software that takes a CSV file from a user and user input of what kind of home they are looking for (acre size, house size, number of bedrooms, number of bathrooms and zip code). User choses on what to train the predictive model. Software prints the estimated price based on the criteria given by the user.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


## Prerequisites
Coding language is Python3.
Ensure Python 3.8 or higher is installed

### Libraries used: 
tkinter, customtkinter, pandas and PIL

### Installing: 
in Windows PowerShell:

```
pip install tk
pip install ctk
pip install pandas
pip install pillow

```

There is only one unit test for the CSV file. Run it with 

```
python -m unittest discover tests
```
The app has tests to show to user's interface. If the user doesn't put the correct format for square meters, acre lot size, bedrooms and bathrooms. The user get's a warning message to correct the error. There's a test that checks if user's chosen zip code exists in the CSV file they have submitted.

## Deployment

* for Windows .exe deployment - https://towardsdatascience.com/how-to-easily-convert-a-python-script-to-an-executable-file-exe-4966e253c7e9
* for Apple .app deployment - https://py2app.readthedocs.io/en/latest/

## Built With
* tkinter, customtkinter - The web framework used
* Python3 - Coding language

## Images
* icons -  icons8.com
* images - undraw.co

## Versioning


## Author

* **Monika Ivanova** - *Initial work* - [ivanovamonika](https://github.com/ivanovamonika)

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
Project template from: 
[kulttuuri](https://github.com/kulttuuri/python_customtkinter_multipage_app_example)

## Inspiration
School
