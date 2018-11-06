from flask import render_template
from flask import request
import logging, json
from . import main


@main.route("/", methods=['GET', 'POST'])
def index():
    logging.info("index")
    return render_template('index.html')


@main.route("/login", methods=['POST'])
def login():
    try:
        logging.info("login")
        return 1
    except Exception as e:
        logging.error(e)



