## Name
Weather application

## Description
This is meant for tourists visiting cities. There is a published webiste but it can also be run on a localhost.
There are two applications(two folders)
The first application-'appone'-is a combination of Mark Muinde's own web service and the OpenWeatherMap API. The client is also in this folder.
The second application-'apptwo'is Ishmam Ahmed's web service

The user inputs a city name via a web interface.

The external API (openweathermap.org) uses an API key for a free account to returns the weather conditions for that city to the client and passes an array representing the current weather conditions of that city to the first internal web service (WS1)

WS1 reads the array to get relevant weather conditions and returns relevant advice as to how to deal with the weather, and relevant integer flags that represent the level of alertness the client should have. It appends the advice and the integer flags to the client.

The client calls in a function from 'apptwo' that takes the appended array as input.

apptwo takes in the appended array and reads the integer flags, translates them into weather conditions and performs a google search as to what to do in the city when it has those weather conditions and returns the first 15 links that have been gotten. apptwo then appends these links to the array and send it back to the client.

The client then opens the array and returns to the user all this information on one comprehensive html page.


## Installation and usage

**For localhost usage:**
Use the Flask framework 
At the root directory is a file-_requirements.txt_ that has all the dependencies.


1. Unzip the zip file code submission
2. Open a terminal and cd into the folder named 'flask'
3. Run this command: 

                . bin/activate 
                
This should activate the virtual environment

4. With the virtual environmet running, cd back to the root directory and run this command:

                pip install -r requirements.txt

This will unpack all the dependencies. 

5. Run these commands next:

                export FLASK_APP=run.py
                export FLASK_ENV=development 
                flask run

6. Open a browser and go to the localhost url: http://127.0.0.1:5000/
You will receive output on both the webpage and your terminal once a city name is entered. 

**For web usage:**
Go to this url : http://markandishmam.pythonanywhere.com/
You will receive web page output once a city name is entered.


