from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from app import views, models