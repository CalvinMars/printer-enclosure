import time
import RPi.GPIO as GPIO
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# Find temperature probe
DS18B20="/sys/bus/w1/devices/28-000009a29c16/w1_slave"

# Setup fan and button GPIO pins (23 and 10)
GPIO.setwarnings(False) # Turn off warnings
GPIO.setmode(GPIO.BCM)

FAN_PIN = 24
BUTTON_PIN = 27
GPIO.setup(FAN_PIN, GPIO.OUT) # Set fan pin
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set button pin, with initial value off

fan_state=False
button=False

button_state = 0


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    colorWipe(strip, Color(255,255,255))
    while True:
        # Get reading from probe
        f = open(DS18B20, "r")
        data = f.read()
        f.close()

        # Only use the temperature data
        (discard, sep, reading) = data.partition(' t=')

        # Devide to find Celcius
        temp = float(reading) / 1000.0
        print(temp);
        
        print(GPIO.input(BUTTON_PIN))
        # If button is pressed, turn fan on
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            if (button == False):
                print("Button Pressed")
                GPIO.output(FAN_PIN, True)
                button = True
                fan_state = True
        else:  # Otherwise check if it is more than 40 degrees in the box
            button = False
        #Turn fan on if temperature is more than 40 degrees C
            if(temp >= 25):
                if (fan_state == False):
                    print("turning fan on")
                    fan_state = True
                    GPIO.output(FAN_PIN, True)
            
            else: # Turn fan off if less than 40 degrees C
                if (fan_state == True):
                    print("turning fan off")
                    fan_state = False
                    GPIO.output(FAN_PIN, False)
        
        
        time.sleep(1)
