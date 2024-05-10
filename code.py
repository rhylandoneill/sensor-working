# SPDX-FileCopyrightText: 2024 Eric Z. Ayers
#
# SPDX-License-Identifier: Creative Commons Zero 1.0

"""Collect training data from a color sensor and publish it to Adafruit IO """

import board
import busio
import time

import adafruit_tcs34725


##################
# *EDIT*
# Set configurable values below
# Feed name for Adafruit IO

# milliseconds to gather color data
sensor_integration_time = 150

# manually override the color sensor gain
sensor_gain = 4

# Collect this many samples each time we prompt the user
num_samples = 5

#
# End of editable config values
##################

# Create sensor object, communicating over the board's default I2C bus
i2c = busio.I2C(board.GP5, board.GP4)  # uses first I2C SCA/SCL pair on pico
sensor = adafruit_tcs34725.TCS34725(i2c)

# Change sensor gain to 1, 4, 16, or 60
sensor.gain = sensor_gain
# Change sensor integration time to values between 2.4 and 614.4 milliseconds
sensor.integration_time = sensor_integration_time


while True:
    print(sensor.color_rgb_bytes)
    red = sensor.color_rgb_bytes[0]
    green = sensor.color_rgb_bytes[1]
    blue = sensor.color_rgb_bytes[2]
    lux = sensor.lux
    temp = sensor.color_temperature
    print(red,green,blue,lux,temp)
    print("Temperature: %d" % sensor.color_temperature)
    print(
        "r: %d, g: %d, b: %d"
        % (
            sensor.color_rgb_bytes[0],
            sensor.color_rgb_bytes[1],
            sensor.color_rgb_bytes[2],
        )
    )
    print("Lux: %d" % sensor.lux)
    if red < 39 and red > 35 and green < 16 and green > 12 and lux < 150 and lux > 105 and temp > 3000 and temp < 3200:
        print ("red detected")
    if red > 40 and red < 50 and green < 15 and green > 10 and lux > 130 and lux < 160 and temp > 2700 and temp < 3000:
        print ("orange detected")
    if red > 37 and red < 41 and green < 17 and green > 13 and lux > 165 and lux < 180 and temp > 2800 and temp < 3000:
        print ("yellow detected")
    if red > 27 and red < 32 and green < 20 and green > 16 and lux > 140 and lux < 180 and temp > 3050 and temp < 3500:
        print ("green detected")
    if red > 27 and red < 32 and green < 19 and green > 14 and lux > 110 and lux < 135 and temp > 3050 and temp < 3500:
        print ("purple detected")
    else:
        print("nothing detected")
    time.sleep(5)
