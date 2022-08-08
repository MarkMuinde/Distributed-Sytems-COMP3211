#import necessary packages
from flask import render_template, redirect
from appone import appone
from .forms import CityForm
import pyowm #Python OpenWeatherMap (owm) API version 2.10.0
import pandas as pd


#weather function to get weather details
def weather():

    #import world cities csv file
    columnNames = ['city']
    data = pd.read_csv('worldcities.csv', names=columnNames)
    names = data.city.tolist()
    
    #import the city form
    form = CityForm()
    if form.validate_on_submit():
        city = form.city.data
        if city not in names:
            return render_template ('redirect.html', title = 'Weather of City')
        else:
            API_key = '839c2939c15a0df36b7a061166502e26'                                    #API key from openweathermap.org as short variable
            openWeatherMap = pyowm.OWM(API_key)                                             #using pyowm function to create owm object
            weatherAtPlace = openWeatherMap.weather_at_place(city)                          #where you need to see the weather
            weatherData = weatherAtPlace.get_weather()                                      #get the weather data


            #Basic data
            print("\-----------------------------------------------------------------------------------------------------------------------------\n")
            print("\u0332".join("CURRENTLY:"))
            print("All times are in Greenwich Mean Time(GMT)")
            print("\n")
            

            #Temperature data
            temperature = weatherData.get_temperature(unit='celsius')                       #temperature in degrees celsiustemperature['temp']
            temp = temperature['temp']                                                      #actual temperature
            tempMax = temperature['temp_max']                                               #maximum temperature
            tempMin = temperature['temp_min']                                               #minimum temperature

            print("The current temperature is ", temperature['temp'], "\N{DEGREE SIGN}C with highs of ",
                tempMax, "\N{DEGREE SIGN}C and lows of ", tempMin, "\N{DEGREE SIGN}C.")
            print("\n")

            #Wind data
            wind = weatherData.get_wind()                                                   #get wind speed & direction
            windSpeed = wind['speed']                                                       #wind speed
            windDirection = wind['deg']                                                     #wind direction
            print("The current wind speed is ",
                windSpeed, "m/s and the current wind direction is ", windDirection, "\N{DEGREE SIGN}")
            print("\n")

            #Humidity data
            humidity = weatherData.get_humidity()                                           #get humidity
            print("The current humidity is ", humidity, "kg^-1")                            #was not able to find negative superscripting for python but available in html
            print("\n")

            #Cloud coverage
            cloudCoverage = weatherData.get_clouds()                                        #get cloud coverage
            print("The cloud coverage percentage is ", cloudCoverage, "%")
            print("\n")

            #save necessary details into array
            dataArray = [city, temp, tempMax, tempMin, humidity, windSpeed, windDirection, cloudCoverage]

            #return the array for the weather data for the first internal web service
            return dataArray

    return render_template('city.html', title = 'Weather of City', form = form)


#redirect if city input is invalid
@appone.route('/redirect', methods=['GET', 'POST'])
def redirect():
    return render_template('redirect.html', title='Weather of City')



