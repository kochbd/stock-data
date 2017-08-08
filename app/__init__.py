from flask import Flask, render_template

import datetime
app = Flask(__name__)
app.config.from_object('config')
from app import views
