from flask import Flask

apptwo = Flask(__name__)
apptwo.config.from_object('config')

from apptwo import weatherarray