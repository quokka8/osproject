from flask import Flask, render_template
import serial
import time

app = Flask(__name__)

arduino_port = 'COM3'  
ser = serial.Serial(arduino_port, 9600)


@app.route('/')
def index():
    data = get_sensor_data()
    temperature, noise_level = data.split(',')

    return render_template('index.html', temperature=temperature, noise_level=noise_level)

def get_sensor_data():
    data = ser.readline().decode().strip()
    return data

if __name__ == '__main__':
    app.run(debug=True)
