# This Python file uses the following encoding: utf-8
import sys
import requests
import json

from PySide6.QtWidgets import QApplication, QMainWindow, QCompleter, QGraphicsBlurEffect
from PySide6.QtGui import  QPixmap, QMovie
from PySide6.QtCore import Qt, QTimer
from datetime import datetime, timezone, timedelta
import threading
import re
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.movie = QMovie("weather_icons/6.gif")
        blur_effect = QGraphicsBlurEffect(self)
        blur_effect.setBlurRadius(10)
        self.ui.animated_bg.setGraphicsEffect(blur_effect)
        self.movie.setScaledSize(self.ui.animated_bg.size())
        self.ui.animated_bg.setMovie(self.movie)
        self.movie.start()
#------------------------------------------------------------------------------------------------------------------------#
#                                                General  setup                                                          #
#------------------------------------------------------------------------------------------------------------------------#
        #Api key
        self.api_key = "0431196d6053b7ab1d5b34e45da76d05"

        #Some variables initialization.
        self.lat = None
        self.icon = None
        self.lon = None
        self.local_time = None  

        #City list initialization. We'll need this for the auto-completer.
        self.city_list = []

        #On search button click, connect to self.get_weather method.
        self.ui.searchButton.clicked.connect(self.load_ui_with_delay)
        self.clock = QTimer()
        self.clock.timeout.connect(self.local_time_bg)
        self.clock.start(200)
   

        #Function Call
        self.suggestions()

    def load_ui_with_delay(self):
        '''Method to introduce a delay without blocking the UI'''
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)  # Timer should trigger only once
        self.timer.timeout.connect(self.load_ui)  # Call load_ui() after delay
        self.timer.start(1000)  # 1000 ms = 1 second delay

    def load_ui(self):
        self.start_background_task()
        self.local_time_bg()

#------------------------------------------------------------------------------------------------------------------------#
#                                               Suggestion function                                                      #
#------------------------------------------------------------------------------------------------------------------------#


    def suggestions(self):
        ''' Function that will fill the previously created list with City and country name.
            That list will be used for the auto-completer that will pop when something is being typed inside the search field'''
        
        #Open json file and load data inside the list.
        with open('city.list.json', 'r') as file:
            self.data = json.load(file)

        #For loop to extrapolate each city name and country from the list.
        # We've to use a string cause append can't take 2 arguments and it expect a string. So tuples were not an option. 
        for cities in self.data:
                city_entry = f"{cities['name']} ({cities['country']})"
                self.city_list.append(city_entry)


        #Previously mentioned completer initialization and setup.
        completer = QCompleter(self.city_list)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setMaxVisibleItems(5)
        self.ui.lineEdit.setCompleter(completer)
#------------------------------------------------------------------------------------------------------------------------#
#                        Function to get weather infos, such as temperature, etc                                         #
#------------------------------------------------------------------------------------------------------------------------#
        
        
    def start_background_task(self):
        '''Function to start the get_weather function in a background thread.'''
        threading.Thread(target=self.get_weather).start()

    def local_time_bg(self):
        threading.Thread(target=self.set_local_time).start()

    def get_weather(self):
        '''Function
            Gets the real-time weather condition of a city. From this function we'll also call 2 other functions
            self.get_weather_icon() = Function that will return a different icon based con the weather ID returned by the API.
            self.weather_forecast() = Function that will return weather the next 5 days.'''
        self.city_name = self.ui.lineEdit.text()

        if self.ui.lineEdit.text() == "":
            self.ui.lineEdit.setPlaceholderText("Please search for a valid city")
            return

        #Truncates the city complete name. Example: From Terni (IT) to Terni. Else it won't work for the API Call.
        self.city_name = re.sub(r"\s*\(.*\)","",self.city_name)
         #Open json file and load data inside the list.

        #Loop the json file to find the city name and its coordinates.  
        for cities in self.data:
            if cities['name'] == self.city_name:
                self.lat = cities['coord']['lat']
                self.lon = cities['coord']['lon']

        #Base url for the API request.
        base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.api_key}&units=metric&lang=it"
        response = requests.get(base_url)
        if response.status_code == 200:

            self.weather_info = response.json()
            #Temp = Current temperature in celsius
            temp = self.weather_info['main']['temp'] 

            #Name = city_name
            self.name = self.weather_info['name']

            #Weather description
            description = self.weather_info['weather'][0]['description']

            self.ui.temp.setText(f"{str(temp)}°, {description}")

            self.get_weather_icon()
            self.weather_forecast()
            
#------------------------------------------------------------------------------------------------------------------------#
#                            Function to remove hour from date. Needed for weather forecast                              #
#------------------------------------------------------------------------------------------------------------------------#

    def remove_hour(self, date):
        '''Function to extrapolate date only from a DATE/HOUR string format.
           Returns:
            date string without the hour.'''
        date = date[0:10]
        return date
    
#------------------------------------------------------------------------------------------------------------------------#
#                            Function to set local-time hour                                                             #
#------------------------------------------------------------------------------------------------------------------------# 

    def set_local_time(self):
        base_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={self.lat}&lon={self.lon}&appid={self.api_key}&units=metric&lang=it"
        response = requests.get(base_url)
        data = response.json()
        if response.status_code == 200:
            self.local_time_offset = data['city']['timezone'] // 3600
            local_time = str(datetime.now(timezone.utc) + timedelta(hours= self.local_time_offset))
            self.local_time = local_time[0:19]
            self.ui.city_label.setText(f"{str(self.name)}, {self.local_time}")
    

#------------------------------------------------------------------------------------------------------------------------#
#                            Function to get weather forecast from today to the next 5 days                              #
#------------------------------------------------------------------------------------------------------------------------#

    def weather_forecast(self):
        ''' Function used to get all the weather data for the next 5 days. Data will be placed inside a grid with day and hours.
            Inside the function i've set every label with its own scaled pixmap that will displays respective weather icon for a certain day/hour.
            This function will also show the local time for selected city.
            '''
        base_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={self.lat}&lon={self.lon}&appid={self.api_key}&units=metric&lang=it"
        response = requests.get(base_url)
        data = response.json()
        if response.status_code == 200:

            #Setting ui label for each day. From current to the next 5 days.
            self.ui.Day_1.setText(self.remove_hour(data['list'][2]['dt_txt']))
            self.ui.Day_2.setText(self.remove_hour(data['list'][10]['dt_txt']))
            self.ui.Day_3.setText(self.remove_hour(data['list'][18]['dt_txt']))
            self.ui.Day_4.setText(self.remove_hour(data['list'][26]['dt_txt']))
            self.ui.Day_5.setText(self.remove_hour(data['list'][34]['dt_txt']))

            #Setting ui label for each hour. Will be set every 3 hour because that's what the API gave me back.
            self.ui.midnight.setText("00:00:00")
            self.ui.three.setText("00:03:00")
            self.ui.six.setText("00:06:00")
            self.ui.nine.setText("00:09:00")
            self.ui.twelve.setText("00:12:00")
            self.ui.fifteen.setText("00:15:00")
            self.ui.eighteen.setText("00:18:00")
            self.ui.twentyone.setText("00:21:00")

            #Retrieve and store each ID of a certain day/hour inside a variable.
            id_day1_midnight = data['list'][2]['weather'][0]['id']
            id_day1_three = data['list'][3]['weather'][0]['id']
            id_day1_six = data['list'][4]['weather'][0]['id']
            id_day1_nine = data['list'][5]['weather'][0]['id']
            id_day1_twelve = data['list'][6]['weather'][0]['id']
            id_day1_fifteen = data['list'][7]['weather'][0]['id']
            id_day1_eighteen = data['list'][8]['weather'][0]['id']
            id_day1_twentyone =data['list'][9]['weather'][0]['id']
            id_day2_midnight = data['list'][10]['weather'][0]['id']
            id_day2_three = data['list'][11]['weather'][0]['id']
            id_day2_six = data['list'][12]['weather'][0]['id']
            id_day2_nine = data['list'][13]['weather'][0]['id']
            id_day2_twelve = data['list'][14]['weather'][0]['id']
            id_day2_fifteen = data['list'][15]['weather'][0]['id']
            id_day2_eighteen = data['list'][16]['weather'][0]['id']
            id_day2_twentyone =data['list'][17]['weather'][0]['id']
            id_day3_midnight =data['list'][18]['weather'][0]['id']
            id_day3_three = data['list'][19]['weather'][0]['id']
            id_day3_six =data['list'][20]['weather'][0]['id']
            id_day3_nine = data['list'][21]['weather'][0]['id']
            id_day3_twelve = data['list'][22]['weather'][0]['id']
            id_day3_fifteen = data['list'][23]['weather'][0]['id']
            id_day3_eighteen = data['list'][24]['weather'][0]['id']
            id_day3_twentyone =data['list'][25]['weather'][0]['id']
            id_day4_midnight =data['list'][26]['weather'][0]['id']
            id_day4_three = data['list'][27]['weather'][0]['id']
            id_day4_six =data['list'][28]['weather'][0]['id']
            id_day4_nine = data['list'][29]['weather'][0]['id']
            id_day4_twelve = data['list'][30]['weather'][0]['id']
            id_day4_fifteen = data['list'][31]['weather'][0]['id']
            id_day4_eighteen = data['list'][32]['weather'][0]['id']
            id_day4_twentyone =data['list'][33]['weather'][0]['id']
            id_day5_midnight =data['list'][34]['weather'][0]['id']
            id_day5_three = data['list'][35]['weather'][0]['id']
            id_day5_six =data['list'][36]['weather'][0]['id']
            id_day5_nine = data['list'][37]['weather'][0]['id']
            id_day5_twelve = data['list'][38]['weather'][0]['id']
            id_day5_fifteen = data['list'][39]['weather'][0]['id']

        

        #Set every label with a scaled pixmap, done by using a function called self.id_to_icon() that will convert each id to its respective icon.
        self.pixmap_day1_midnight = QPixmap(self.id_to_icon(id_day1_midnight))
        self.scaled_pixmap_day1_midnight = self.pixmap_day1_midnight.scaled(self.ui.day1_midnight.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day1_midnight.setPixmap(self.scaled_pixmap_day1_midnight)

        self.pixmap_day1_three = QPixmap(self.id_to_icon(id_day1_three))
        self.scaled_pixmap_day1_three = self.pixmap_day1_three.scaled(self.ui.day1_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day1_three.setPixmap(self.scaled_pixmap_day1_three)

        self.pixmap_day1_six = QPixmap(self.id_to_icon(id_day1_six))
        self.scaled_pixmap_day1_six = self.pixmap_day1_six.scaled(self.ui.day1_six.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day1_six.setPixmap(self.scaled_pixmap_day1_six)


        self.pixmap_day1_nine = QPixmap(self.id_to_icon(id_day1_nine))
        self.scaled_pixmap_day1_nine = self.pixmap_day1_nine.scaled(self.ui.day1_nine.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day1_nine.setPixmap(self.scaled_pixmap_day1_nine)


        self.pixmap_day1_twelve = QPixmap(self.id_to_icon(id_day1_twelve))
        self.scaled_pixmap_day1_twelve = self.pixmap_day1_twelve.scaled(self.ui.day1_twelve.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day1_twelve.setPixmap(self.scaled_pixmap_day1_twelve)


        self.pixmap_day1_fifteen = QPixmap(self.id_to_icon(id_day1_fifteen))
        self.scaled_pixmap_day1_fifteen = self.pixmap_day1_fifteen.scaled(self.ui.day1_fifteen.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day1_fifteen.setPixmap(self.scaled_pixmap_day1_fifteen)


        self.pixmap_day1_eighteen = QPixmap(self.id_to_icon(id_day1_eighteen))
        self.scaled_pixmap_day1_eighteen = self.pixmap_day1_eighteen.scaled(self.ui.day1_eighteen.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day1_eighteen.setPixmap(self.scaled_pixmap_day1_eighteen)


        self.pixmap_day1_twentyone = QPixmap(self.id_to_icon(id_day1_twentyone))
        self.scaled_pixmap_day1_twentyone = self.pixmap_day1_twentyone.scaled(self.ui.day1_twentyone.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day1_twentyone.setPixmap(self.scaled_pixmap_day1_twentyone)

        self.pixmap_day2_midnight = QPixmap(self.id_to_icon(id_day2_midnight))
        self.scaled_pixmap_day2_midnight = self.pixmap_day2_midnight.scaled(self.ui.day2_midnight.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day2_midnight.setPixmap(self.scaled_pixmap_day2_midnight)

        self.pixmap_day2_three = QPixmap(self.id_to_icon(id_day2_three))
        self.scaled_pixmap_day2_three = self.pixmap_day2_three.scaled(self.ui.day2_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day2_three.setPixmap(self.scaled_pixmap_day2_three)

        self.pixmap_day2_six = QPixmap(self.id_to_icon(id_day2_six))
        self.scaled_pixmap_day2_six = self.pixmap_day2_six.scaled(self.ui.day2_six.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day2_six.setPixmap(self.scaled_pixmap_day2_six)

        self.pixmap_day2_nine = QPixmap(self.id_to_icon(id_day2_nine))
        self.scaled_pixmap_day2_nine = self.pixmap_day2_nine.scaled(self.ui.day2_nine.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day2_nine.setPixmap(self.scaled_pixmap_day2_nine)

        self.pixmap_day2_twelve = QPixmap(self.id_to_icon(id_day2_twelve))
        self.scaled_pixmap_day2_twelve = self.pixmap_day2_twelve.scaled(self.ui.day2_twelve.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day2_twelve.setPixmap(self.scaled_pixmap_day2_twelve)

        self.pixmap_day2_fifteen = QPixmap(self.id_to_icon(id_day2_fifteen))
        self.scaled_pixmap_day2_fifteen = self.pixmap_day2_fifteen.scaled(self.ui.day2_fifteen.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day2_fifteen.setPixmap(self.scaled_pixmap_day2_fifteen)

        self.pixmap_day2_eighteen = QPixmap(self.id_to_icon(id_day2_eighteen))
        self.scaled_pixmap_day2_eighteen = self.pixmap_day2_eighteen.scaled(self.ui.day2_eighteen.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day2_eighteen.setPixmap(self.scaled_pixmap_day2_eighteen)

        self.pixmap_day2_twentyone = QPixmap(self.id_to_icon(id_day2_twentyone))
        self.scaled_pixmap_day2_twentyone = self.pixmap_day2_twentyone.scaled(self.ui.day2_twentyone.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day2_twentyone.setPixmap(self.scaled_pixmap_day2_twentyone)

        
        self.pixmap_day3_midnight = QPixmap(self.id_to_icon(id_day3_midnight))
        self.scaled_pixmap_day3_midnight = self.pixmap_day3_midnight.scaled(self.ui.day3_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day3_midnight.setPixmap(self.scaled_pixmap_day3_midnight)

        self.pixmap_day3_three = QPixmap(self.id_to_icon(id_day3_three))
        self.scaled_pixmap_day3_three = self.pixmap_day3_three.scaled(self.ui.day3_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day3_three.setPixmap(self.scaled_pixmap_day3_three)

        self.pixmap_day3_six = QPixmap(self.id_to_icon(id_day3_six))
        self.scaled_pixmap_day3_six = self.pixmap_day3_six.scaled(self.ui.day3_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day3_six.setPixmap(self.scaled_pixmap_day3_six)

        self.pixmap_day3_nine = QPixmap(self.id_to_icon(id_day3_nine))
        self.scaled_pixmap_day3_nine = self.pixmap_day3_nine.scaled(self.ui.day3_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day3_nine.setPixmap(self.scaled_pixmap_day3_nine)

        self.pixmap_day3_twelve = QPixmap(self.id_to_icon(id_day3_twelve))
        self.scaled_pixmap_day3_twelve = self.pixmap_day3_twelve.scaled(self.ui.day3_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day3_twelve.setPixmap(self.scaled_pixmap_day3_twelve)

        self.pixmap_day3_fifteen = QPixmap(self.id_to_icon(id_day3_fifteen))
        self.scaled_pixmap_day3_fifteen = self.pixmap_day3_fifteen.scaled(self.ui.day3_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day3_fifteen.setPixmap(self.scaled_pixmap_day3_fifteen)

        self.pixmap_day3_eighteen = QPixmap(self.id_to_icon(id_day3_eighteen))
        self.scaled_pixmap_day3_eighteen = self.pixmap_day3_eighteen.scaled(self.ui.day3_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day3_eighteen.setPixmap(self.scaled_pixmap_day3_eighteen)

        self.pixmap_day3_twentyone = QPixmap(self.id_to_icon(id_day3_twentyone))
        self.scaled_pixmap_day3_twentyone = self.pixmap_day3_twentyone.scaled(self.ui.day3_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day3_twentyone.setPixmap(self.scaled_pixmap_day3_twentyone)

        self.pixmap_day4_midnight = QPixmap(self.id_to_icon(id_day4_midnight))
        self.scaled_pixmap_day4_midnight = self.pixmap_day4_midnight.scaled(self.ui.day4_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day4_midnight.setPixmap(self.scaled_pixmap_day4_midnight)

        self.pixmap_day4_three = QPixmap(self.id_to_icon(id_day4_three))
        self.scaled_pixmap_day4_three = self.pixmap_day4_three.scaled(self.ui.day4_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day4_three.setPixmap(self.scaled_pixmap_day4_three)

        self.pixmap_day4_six = QPixmap(self.id_to_icon(id_day4_six))
        self.scaled_pixmap_day4_six = self.pixmap_day4_six.scaled(self.ui.day4_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day4_six.setPixmap(self.scaled_pixmap_day4_six)

        self.pixmap_day4_nine = QPixmap(self.id_to_icon(id_day4_nine))
        self.scaled_pixmap_day4_nine = self.pixmap_day4_nine.scaled(self.ui.day4_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day4_nine.setPixmap(self.scaled_pixmap_day4_nine)

        self.pixmap_day4_twelve = QPixmap(self.id_to_icon(id_day4_twelve))
        self.scaled_pixmap_day4_twelve = self.pixmap_day4_twelve.scaled(self.ui.day4_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day4_twelve.setPixmap(self.scaled_pixmap_day4_twelve)

        self.pixmap_day4_fifteen = QPixmap(self.id_to_icon(id_day4_fifteen))
        self.scaled_pixmap_day4_fifteen = self.pixmap_day4_fifteen.scaled(self.ui.day4_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day4_fifteen.setPixmap(self.scaled_pixmap_day4_fifteen)

        self.pixmap_day4_eighteen = QPixmap(self.id_to_icon(id_day4_eighteen))
        self.scaled_pixmap_day4_eighteen = self.pixmap_day4_eighteen.scaled(self.ui.day4_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day4_eighteen.setPixmap(self.scaled_pixmap_day4_eighteen)

        self.pixmap_day4_twentyone = QPixmap(self.id_to_icon(id_day4_twentyone))
        self.scaled_pixmap_day4_twentyone = self.pixmap_day4_twentyone.scaled(self.ui.day4_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day4_twentyone.setPixmap(self.scaled_pixmap_day4_twentyone)
        

        self.pixmap_day5_midnight = QPixmap(self.id_to_icon(id_day5_midnight))
        self.scaled_pixmap_day5_midnight = self.pixmap_day5_midnight.scaled(self.ui.day5_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day5_midnight.setPixmap(self.scaled_pixmap_day5_midnight)

        self.pixmap_day5_three = QPixmap(self.id_to_icon(id_day5_three))
        self.scaled_pixmap_day5_three = self.pixmap_day5_three.scaled(self.ui.day5_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day5_three.setPixmap(self.scaled_pixmap_day5_three)

        self.pixmap_day5_six = QPixmap(self.id_to_icon(id_day5_six))
        self.scaled_pixmap_day5_six = self.pixmap_day5_six.scaled(self.ui.day5_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day5_six.setPixmap(self.scaled_pixmap_day5_six)

        self.pixmap_day5_nine = QPixmap(self.id_to_icon(id_day5_nine))
        self.scaled_pixmap_day5_nine = self.pixmap_day5_nine.scaled(self.ui.day5_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day5_nine.setPixmap(self.scaled_pixmap_day5_nine)

        self.pixmap_day5_twelve = QPixmap(self.id_to_icon(id_day5_twelve))
        self.scaled_pixmap_day5_twelve = self.pixmap_day5_twelve.scaled(self.ui.day5_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day5_twelve.setPixmap(self.scaled_pixmap_day5_twelve)

        self.pixmap_day5_fifteen = QPixmap(self.id_to_icon(id_day5_fifteen))
        self.scaled_pixmap_day5_fifteen = self.pixmap_day5_fifteen.scaled(self.ui.day5_three.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.day5_fifteen.setPixmap(self.scaled_pixmap_day5_fifteen)


#------------------------------------------------------------------------------------------------------------------------#
#                                         Function to get weather icons                                                  #
#------------------------------------------------------------------------------------------------------------------------#

    def id_to_icon(self,id):
        ''' Function that will check weather ids and retrieve corresponding png icon.

        Returns:
            Path of the icon itself as string'''
        
        if id >= 801 and id <= 804:
            icon = "weather_icons/blue-cloud.png"
        elif id >= 200 and id <= 232:
            icon = "weather_icons/lightning-and-blue-rain-cloud.png"
        elif id >= 300 and id <= 321:
            icon = "weather_icons/downpour-rainy-day.png" 
        elif id >= 500 and id <= 531:
            icon = "weather_icons/rain-and-blue-cloud.png"
        elif id >= 600 and id <= 622:
            icon = "weather_icons/snow-and-blue-cloud.png"
        elif id >= 701 and id <= 781:
            icon = "weather_icons/sand-256.png"
        elif id == 800:
            icon = "weather_icons/yellow-sun.png"
        return icon


    def get_weather_icon(self):
        ''' Very similar function to id_to_icon() but this is used for the real-time weather.
            It also sets the label with respective icon.'''
        
        #This will retrieve current weather id from the API json.
        weather_id = self.weather_info['weather'][0]['id']

        #Check for id and assign/set respective weather icon.
        if weather_id >= 801 and weather_id <= 804:
            self.icon = "weather_icons/blue-cloud.png"
            pixmap = QPixmap(self.icon)
            scaled_pixmap = pixmap.scaled(self.ui.w_icon.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.w_icon.setPixmap(scaled_pixmap)
        elif weather_id >= 200 and weather_id <= 232:
            self.icon = "weather_icons/lightning-and-blue-rain-cloud.png"
            pixmap = QPixmap(self.icon)
            scaled_pixmap = pixmap.scaled(self.ui.w_icon.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.w_icon.setPixmap(scaled_pixmap)
        elif weather_id >= 300 and weather_id <= 321:
            self.icon = "weather_icons/downpour-rainy-day.png"
            pixmap = QPixmap(self.icon)
            scaled_pixmap = pixmap.scaled(self.ui.w_icon.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.w_icon.setPixmap(scaled_pixmap)
        elif weather_id >= 500 and weather_id <= 531:
            self.icon = "weather_icons/rain-and-blue-cloud.png"
            pixmap = QPixmap(self.icon)
            scaled_pixmap = pixmap.scaled(self.ui.w_icon.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.w_icon.setPixmap(scaled_pixmap)
        elif weather_id >= 600 and weather_id <= 622:
            self.icon = "weather_icons/snow-and-blue-cloud.png"
            pixmap = QPixmap(self.icon)
            scaled_pixmap = pixmap.scaled(self.ui.w_icon.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.w_icon.setPixmap(scaled_pixmap)
        elif weather_id >=701  and weather_id <= 781:
            self.icon = "weather_icons/sand-256.png"
            pixmap = QPixmap(self.icon)
            scaled_pixmap = pixmap.scaled(self.ui.w_icon.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.w_icon.setPixmap(scaled_pixmap)
        elif weather_id == 800:
            self.icon = "weather_icons/yellow-sun.png"
            pixmap = QPixmap(self.icon)
            scaled_pixmap = pixmap.scaled(self.ui.w_icon.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.w_icon.setPixmap(scaled_pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
