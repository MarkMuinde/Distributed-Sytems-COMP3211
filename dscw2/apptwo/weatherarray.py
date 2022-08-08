#import necessary packages
from flask import render_template
from apptwo import apptwo
import requests
from googlesearch import search

#second web service
#get array from client as argument and perform google search
def secondWebService(array):

    #read the variables from the array
    cityname = array[0]
    temperatureCurrent = float(array[1])
    temperatureMaximum = array[2]
    temperatureMinimum = array[3]
    humidity = int(array[4])
    windSpeed = float(array[5])
    windDirection = array[6]
    clouds = array[7]
    temperatureAlertLevel = int(array[8])
    humidityAlertLevel = int(array [9])
    advice = array [10]

    #placeholder for search query string variable
    query = ""

    #use the integer flags from the client to develop a query
    #that will perform a google search based on what they represent
    if temperatureAlertLevel == 1 and humidityAlertLevel == 1:
        query = ("https://www.google.com?q=Activities-in-" +
                 str(cityname) + "-when-very-hot-and-humidity-is-high")
    elif temperatureAlertLevel == 1 and humidityAlertLevel == 2:
        query = ("https://www.google.com?q=Activities-in-" +
                 str(cityname) + "-when-very-hot-and-humid")
    elif temperatureAlertLevel == 1 and humidityAlertLevel == 3:
        query = ("https://www.google.com?q=Activities-in-" +
                 str(cityname) + "-when-very-hot-and-humidity-is-low")
    elif temperatureAlertLevel == 2 and humidityAlertLevel == 1:
        query = ("https://www.google.com?q=Activities-in-" +
                 str(cityname) + "-when-hot-and-humidity-is-high")
    elif temperatureAlertLevel == 2 and humidityAlertLevel == 2:
        query = ("https://www.google.com?q=Activities-in-" +
                 str(cityname) + "-when-hot-and-humid")
    elif temperatureAlertLevel == 2 and humidityAlertLevel == 3:
        query = ("https://www.google.com?q=Activities-in-" +
                 str(cityname) + "when-hot-and-humidity-is-low")
    elif temperatureAlertLevel == 3 and humidityAlertLevel == 1:
        query = ("https://www.google.com?q=Activities-in-" +
                 str(cityname) + "-when-chilly-and-humidity-is-high")
    elif temperatureAlertLevel == 3 and humidityAlertLevel == 2:
        query = ("https://www.google.com?q=Activities-in-" +
                 str(cityname) + "-when-chilly-and-humid")
    elif temperatureAlertLevel == 3 and humidityAlertLevel == 3:
        query = ("https://www.google.com?q=Activities-in-" +
                 str(cityname) + "-when-chilly-and-humidity-is-low")
    elif temperatureAlertLevel == 4 and humidityAlertLevel == 1:
        query = ("https://www.google.com?q=Activities-in-" +
                 str(cityname) + "-when-cold-and-humidity-is-high")
    elif temperatureAlertLevel == 4 and humidityAlertLevel == 2:
        query = ("https://www.google.com?q=Activities-in-" +
                 str(cityname) + "-when-cold-and-humid")
    elif temperatureAlertLevel == 4 and humidityAlertLevel == 3:
        query = ("https://www.google.com?q=Activities-in-" +
                 str(cityname) + "-when-cold-and-humidity-is-low")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    requests.get(query, headers=headers)

    links = []
    print("\n\n-----------------------------------------------------------------------------------------------------------------------------\n\n")
    print("Here are some links to help you enjoy your trip to %s based on the current weather conditions.\n Copy and paste any of the links below onto a different web page:\n" % cityname)
    for result in search(query, tld="co.in", num=15, stop=15, pause=2):
        print(result)
        links.append(result)

    #append to array
    array.append(links)

    #return the complete array for the weather data to client
    return array








