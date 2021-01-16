from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

# Task list :
app = Flask(__name__)
db = SQLAlchemy()



if __name__ == '__main__':
    app.run()
