from flask import Flask

appone = Flask(__name__)
appone.config.from_object('config')

from appone import views, advice, main