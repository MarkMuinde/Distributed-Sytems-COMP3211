#import necessary packages
from flask import render_template
from appone import appone
from .forms import CityForm
from .views import *
from .advice import *
from apptwo import *
import time


#weather function to get weather details after failure
@appone.route('/', methods=['GET', 'POST'])
def client():

    #import world cities csv file
    columnNames = ['city']
    data = pd.read_csv('worldcities.csv', names=columnNames)
    names = data.city.tolist()

    #import the city form
    form = CityForm()
    if form.validate_on_submit():
        city = form.city.data
        if city not in names:
            return render_template('redirect.html', title='Weather of City')
        else:
            # API key from openweathermap.org as short variable
            API_key = '839c2939c15a0df36b7a061166502e26'
            # using pyowm function to create owm object
            openWeatherMap = pyowm.OWM(API_key)
            weatherAtPlace = openWeatherMap.weather_at_place(
                city)  # where you need to see the weather
            weatherData = weatherAtPlace.get_weather()  # get the weather data

            #Basic data
            print("\-----------------------------------------------------------------------------------------------------------------------------\n")
            print("\u0332".join("CURRENTLY:"))
            print("All times are in Greenwich Mean Time(GMT)")
            print("\n")

            #Temperature data
            # temperature in degrees celsiustemperature['temp']
            temperature = weatherData.get_temperature(unit='celsius')
            temp = temperature['temp']  # actual temperature
            tempMax = temperature['temp_max']  # maximum temperature
            tempMin = temperature['temp_min']  # minimum temperature

            print("The current temperature is ", temperature['temp'], "\N{DEGREE SIGN}C with highs of ",
                  tempMax, "\N{DEGREE SIGN}C and lows of ", tempMin, "\N{DEGREE SIGN}C.")
            print("\n")

            #Wind data
            wind = weatherData.get_wind()  # get wind speed & direction
            windSpeed = wind['speed']  # wind speed
            windDirection = wind['deg']  # wind direction
            print("The current wind speed is ",
                  windSpeed, "m/s and the current wind direction is ", windDirection, "\N{DEGREE SIGN}")
            print("\n")

            #Humidity data
            humidity = weatherData.get_humidity()  # get humidity
            # was not able to find negative superscripting for python but available in html
            print("The current humidity is ", humidity, "kg^-1")
            print("\n")

            #Cloud coverage
            cloudCoverage = weatherData.get_clouds()  # get cloud coverage
            print("The cloud coverage percentage is ", cloudCoverage, "%")
            print("\n")

            #save necessary details into array
            dataArray = [city, temp, tempMax, tempMin, humidity,
                         windSpeed, windDirection, cloudCoverage]

            #return the array for the weather data for the first internal web service
            return main_function()

    return render_template('city.html', title='Weather of City', form=form)


def main_function():

    #call functions from the external API and first web service
    start1 = time.time()
    weather()
    timetaken1 = time.time() - start1
    start = time.time()
    advices()
    timetaken = time.time() - start
    start2 = time.time()
    dataArray = advices()

    #call function from second web service in client
    dataArrayFinal = weatherarray.secondWebService(dataArray)
    timetaken2 = time.time() - start2

    print('Internal WS1 time :', timetaken)
    print('Internal WS2 time :', timetaken2)
    print('External WS time :', timetaken1)
    print("\n\n-----------------------------------------------------------------------------------------------------------------------------\n\n")

    #return the complete template for the weather data
    return render_template('main.html', title = 'Weather of City', city = dataArrayFinal[0] ,
                            temperature = dataArrayFinal[1], tempMax = dataArrayFinal[2],
                            tempMin = dataArrayFinal[3], humidity = dataArrayFinal[4], 
                            windSpeed = dataArrayFinal[5], windDirection = dataArrayFinal[6], 
                            cloudCoverage = dataArrayFinal[7], tempID = dataArrayFinal [8], 
                            humidityID = dataArrayFinal [9], advice = dataArrayFinal [10],
                            links = dataArrayFinal [11]) 

                            

