# This Python file uses the following encoding: utf-8
import sys
import requests
import json

from PySide6.QtWidgets import QApplication, QMainWindow, QCompleter
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
#------------------------------------------------------------------------------------------------------------------------#
#                                                General  setup                                                          #
#------------------------------------------------------------------------------------------------------------------------#

        #Api key
        self.api_key = "0431196d6053b7ab1d5b34e45da76d05"
        self.lat_lon = None
        self.lat = None
        self.icon = None
        self.lon = None
        #Pixmaps to hold weather's icon forecast
        self.pixmap_day1_midnight = QPixmap()
        self.pixmap_day1_three = QPixmap()
        self.pixmap_day1_six = QPixmap()
        self.pixmap_day1_nine = QPixmap()
        self.pixmap_day1_twelve = QPixmap()
        self.pixmap_day1_fifteen = QPixmap()
        self.pixmap_day1_eighteen = QPixmap()
        self.pixmap_day1_twentyone = QPixmap()
        self.pixmap_day1_midnight = QPixmap()
        self.pixmap_day2_three = QPixmap()
        self.pixmap_day2_six = QPixmap()
        self.pixmap_day2_nine = QPixmap()
        self.pixmap_day2_twelve = QPixmap()
        self.pixmap_day2_fifteen = QPixmap()
        self.pixmap_day2_eighteen = QPixmap()
        self.pixmap_day2_twentyone = QPixmap()
        self.pixmap_day3_midnight = QPixmap()
        self.pixmap_day3_three = QPixmap()
        self.pixmap_day3_six = QPixmap()
        self.pixmap_day3_nine = QPixmap()
        self.pixmap_day3_twelve = QPixmap()
        self.pixmap_day3_fifteen = QPixmap()
        self.pixmap_day3_eighteen = QPixmap()
        self.pixmap_day3_twentyone = QPixmap()
        self.pixmap_day4_midnight = QPixmap()
        self.pixmap_day4_three = QPixmap()
        self.pixmap_day4_six = QPixmap()
        self.pixmap_day4_nine = QPixmap()
        self.pixmap_day4_twelve = QPixmap()
        self.pixmap_day4_fifteen = QPixmap()
        self.pixmap_day4_eighteen = QPixmap()
        self.pixmap_day4_twentyone = QPixmap()
        self.pixmap_day5_midnight = QPixmap()
        self.pixmap_day5_three = QPixmap()
        self.pixmap_day5_six = QPixmap()
        self.pixmap_day5_nine = QPixmap()
        self.pixmap_day5_twelve = QPixmap()
        self.pixmap_day5_fifteen = QPixmap()
        self.pixmap_day5_eighteen = QPixmap()
        self.pixmap_day5_twentyone = QPixmap()


        self.city_list = []

        #On search button click, connect to self.get_weather method.
        self.ui.searchButton.clicked.connect(self.get_weather)
        self.suggestions()

#------------------------------------------------------------------------------------------------------------------------#
#                                               Suggestion function                                                      #
#------------------------------------------------------------------------------------------------------------------------#

    def suggestions(self):
        self.city_name = self.ui.lineEdit.text()
        with open('city.list.json', 'r') as file:
            data = json.load(file)
        
        for città in data:
            self.city_list.append(città['name'])

        completer = QCompleter(self.city_list)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.lineEdit.setCompleter(completer)

        



#------------------------------------------------------------------------------------------------------------------------#
#                  Function to get latitude and longitude. We'll need this to get weather infos                          #
#------------------------------------------------------------------------------------------------------------------------#

    #Function to get lat and lon of city. It will later be useful to get weather.
    def get_lat_lon(self):
        self.city_name = self.ui.lineEdit.text()
        base_url = f"http://api.openweathermap.org/geo/1.0/direct?q={self.city_name}&limit=5&appid={self.api_key}"
        response = requests.get(base_url)
        self.city_info = response.json()
        if response.status_code == 200:
            if self.city_info:       
                self.lat_lon = {"lat": f"{self.city_info[0]['lat']}", "lon": f"{self.city_info[0]['lon']}"}
                return self.lat_lon
            else:
                print("Couldn't find city")
        
#------------------------------------------------------------------------------------------------------------------------#
#                        Function to get weather infos, such as temperature, etc                                         #
#------------------------------------------------------------------------------------------------------------------------#

    def get_weather(self):
        lat_lon = self.get_lat_lon()
        if self.city_info:
            self.lat = lat_lon['lat']
            self.lon = lat_lon['lon']
        else:
            print("No city with this name")
        base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.api_key}&units=metric&lang=it"
        print(base_url)
        response = requests.get(base_url)
        if response.status_code == 200:
            self.weather_info = response.json()
            temp = self.weather_info['main']['temp']
            name = self.weather_info['name']
            description = self.weather_info['weather'][0]['description']
            self.get_weather_icon()
            self.weather_forecast()
            self.ui.w_desc.setText(f"{description}")
            self.ui.city_label.setText(str(name))
            self.ui.temp.setText(f"{str(temp)}°")

#------------------------------------------------------------------------------------------------------------------------#
#                            Function to remove hour from date. Needed for weather forecast                              #
#------------------------------------------------------------------------------------------------------------------------#

    def remove_hour(self, date):
        date = date[0:10]
        return date
    
    def remove_date(self, hour):
        hour = hour[12:19]
        return hour


#------------------------------------------------------------------------------------------------------------------------#
#                            Function to get weather forecast from today to the next 5 days                              #
#------------------------------------------------------------------------------------------------------------------------#

    def weather_forecast(self):
        base_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={self.lat}&lon={self.lon}&appid={self.api_key}&units=metric&lang=it"
        print(base_url)
        response = requests.get(base_url)
        data = response.json()
        if response.status_code == 200:
            #Dates
            self.ui.Day_1.setText(self.remove_hour(data['list'][2]['dt_txt']))
            self.ui.Day_2.setText(self.remove_hour(data['list'][10]['dt_txt']))
            self.ui.Day_3.setText(self.remove_hour(data['list'][18]['dt_txt']))
            self.ui.Day_4.setText(self.remove_hour(data['list'][26]['dt_txt']))
            self.ui.Day_5.setText(self.remove_hour(data['list'][34]['dt_txt']))
            #Hours
            self.ui.midnight.setText("00:00:00")
            self.ui.three.setText("00:03:00")
            self.ui.six.setText("00:06:00")
            self.ui.nine.setText("00:09:00")
            self.ui.twelve.setText("00:12:00")
            self.ui.fifteen.setText("00:15:00")
            self.ui.eighteen.setText("00:18:00")
            self.ui.twentyone.setText("00:21:00")
            #Weather id for each date
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
            # id_day5_eighteen = data['list'][40]['weather'][0]['id']
            # id_day5_twentyone =data['list'][41]['weather'][0]['id']
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
        weather_id = self.weather_info['weather'][0]['id']
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

#------------------------------------------------------------------------------------------------------------------------#
#                                         Setting app-background image                                                   #
#------------------------------------------------------------------------------------------------------------------------#

stylesheet =  """MainWindow {
    background-image: url("weather_icons/sky-background-video-conferencing/4205986.jpg"); 
    background-repeat: no-repeat; 
    background-position: center; 
    }
    """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
