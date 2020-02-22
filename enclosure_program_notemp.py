import time
import RPi.GPIO as GPIO
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 68)

# Setup fan and button GPIO pins
GPIO.setwarnings(False) # Turn off warnings
GPIO.setmode(GPIO.BCM)

FAN_PIN = 24
BUTTON_PIN = 27
LED_PIN = 16
GPIO.setup(FAN_PIN, GPIO.OUT) # Set fan pin
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set button pin, with initial value off
GPIO.setup(LED_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

fan_state=False
button=False

button_state = 0
led_button = False

if __name__ == '__main__':
    print("Starting Printer Enclosure program")
    # for x in range(0, 68):
    #     pixels[x] = (255, 197, 143)
    #     time.sleep(.02)
    for x in range (4):
        pixels[34] = (255, 197, 143)
        pixels[35] = (255, 197, 143)
        time.sleep(.2)
        pixels[34] = (0,0,0)
        pixels[35] = (0,0,0)
        time.sleep(.2)
    while True:
        if GPIO.input(LED_PIN) == GPIO.LOW:
            if led_button == False:
                led_button=True
                print("turning LEDs on")
                for x in range(0, 68):
                    pixels[x] = (0, 0, 0)
                    time.sleep(.02)
                    
        else:
            if led_button == True:
                led_button=False
                print("Turning LEDs off")
                for x in range(0, 68):
                    pixels[x] = (255, 197, 143)
                    time.sleep(.02)


 
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            if (button == False):
                print("Button Pressed")
                GPIO.output(FAN_PIN, True)
                button = True
                fan_state = True
        else:  # Otherwise check if it is more than 40 degrees in the box
            if (button == True):
                button = False
                fan_state = False
                GPIO.output(FAN_PIN, False)
    
        time.sleep(.1)
