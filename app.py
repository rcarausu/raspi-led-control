import logging
from json import dumps

from flask import Flask
import RPi.GPIO as GPIO

import time

from logger import configure_logging

app = Flask(__name__)


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/pin_on/<pin_number>')
def pin_on(pin_number):
    try:
        pin = int(pin_number)
        logging.info("Turning on pin {}".format(pin))
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        return dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except Exception as e:
        logging.exception("Error while trying to activate pin")
        return dumps({'success': False}), 500, {'ContentType': 'application/json'}


@app.route('/pin_off/<pin_number>')
def pin_off(pin_number):
    try:
        pin = int(pin_number)
        logging.info("Turning off pin {}".format(pin))
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        return dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except Exception as e:
        logging.exception("Error while trying to deactivate pin")
        return dumps({'success': False}), 500, {'ContentType': 'application/json'}


if __name__ == '__main__':
    configure_logging("/home/rcarausu/", "led_control")

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    app.run()
