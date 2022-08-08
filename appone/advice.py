#import necessary packages
from appone import appone
from .views import *
import linecache
import pandas as pd

#advice to survive city's weather

def advices():

    #read the array from the external API
    dataArray = weather()

    
    #read the variables from the array
    temperatureAdvice = float(dataArray[1])
    humidity = int(dataArray[4])
    windSpeed = float(dataArray[5])
 

    #new variables for second web service
    #placeholder for weather advice string variable
    advice = ""

    #placeholder for temperature integer variable
    tempID = 0

    #placeholder for humidity integer variable
    humidityID = 0
    
    #give advice based off of weather data; namely temperature, wind and humidity
    print("\n\n-----------------------------------------------------------------------------------------------------------------------------\n\n")
    print("All advice is based off of scales from Thinkmetric(temperature), the Beaufort Wind Scale(wind speed) and AirThings(humidity) ")
    #temperature advice
    if temperatureAdvice >= 15.00:
        advice += "Your destination will have high to very high temperatures. Put on SPF 40+ sunscreen, dress lightly, go see the city and, where possible, go to the beach.\n"
        tempID = 1
    elif 10.00 <= temperatureAdvice < 15.00:
        advice += "Your destination will have average to high temperatures. Put on SPF 30+ sunscreen, dress normally (but do carry a light jacket just incase) and go see the city.\n"
        tempID = 2
    elif 5.00 <= temperatureAdvice < 10.00:
        advice += "Your destination will have cold to average temperatures. You should have a jacket and some warm clothes. You can go touring if you enjoy the cold but carry the warm clothes with you.\n"
        tempID = 3
    elif 0.00 <= temperatureAdvice < 5.00:
        advice += "Your destination will have cold to very cold temperatures. We recommend that you stay indoors, cover up, have a warm meal and enjoy a lazy day.\n"
        tempID = 4
    elif temperatureAdvice < 0.00:
        advice += "Your destination will have below freezing temperatures. Winter is coming! We recommend you stay indoors. Nevertheless, have some winter clothes handy if you must leave your accomodation.\n"
        tempID = 4

    #wind advice
    if windSpeed >= 27.50:
        advice += "There will also be storms and possibly hurricanes. Do not leave your accomodation until it is safe to do so.\n"
    elif 16.50 <= windSpeed <27.50:
        advice += "There will also be gale winds. Bring a coat, preferrably a windbreaker if you have or can buy one.\n"
    elif 8.00 <= windSpeed <16.50:
        advice += "There will also be breeze winds. Not much to be concerned about, but bring a coat just incase.\n"
    elif 0.00 <= windSpeed <8.00:
        advice += "There will also be gentle winds-a little bit windy, but nothing alarming.\n"
    
    #humidity advice
    if humidity >= 50:
        advice += "Your destination also has high humidity. Buy a portable A/C and/or a dehumidifier and enjoy some cold drinks.\n"
        humidityID = 1
    elif 30 <= humidity < 50:
        advice += "Your destination also has moderate humidity. Buy a portable A/C or a dehumidifier if you find this too uncomfortable for you and enjoy some cold drinks.\n"
        humidityID = 2
    elif 30 <= humidity < 50:
        advice += "Your destination also has low humidity. Buy a humidifier if you find this too uncomfortable for you.\n"
        humidityID = 3
    

    #append the array for the second internal web service
    dataArray.append(tempID)
    dataArray.append(humidityID)
    dataArray.append(advice)

    #print advice
    print(advice)
    print("\n\n-----------------------------------------------------------------------------------------------------------------------------\n\n")

    #return the array
    return dataArray