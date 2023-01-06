#Bring in pyautogui
import pyautogui as pg
#Brings in Flask & render templates from flask
from flask import Flask, render_template

#Create the Flask app
app = Flask(__name__)

#This function will take a screen shot and save it as desktop.png
def ScreenMonitor():
    image = pg.screenshot('static/desktop.png')
    print('Screenshot Taken!')

ScreenMonitor()

#Makes a basic route for Flask server
@app.route('/')
#Makes a function witch should display Dekstop.html on the flask server
def Desktop():
    return render_template('Desktop.html')

#This will run the flask server
if __name__ == "__main__":
    app.run()
    print('Flask server now closed ):')

