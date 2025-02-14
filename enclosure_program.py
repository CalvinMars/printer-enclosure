import time
import RPi.GPIO as GPIO
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 68)

# Find temperature probe
DS18B20="/sys/bus/w1/devices/28-000009a29c16/w1_slave"

# Setup fan and button GPIO pins (23 and 10)
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
        # Get reading from probe
        f = open(DS18B20, "r")
        data = f.read()
        f.close()

        # Only use the temperature data
        (discard, sep, reading) = data.partition(' t=')

        # Devide to find Celcius
        temp = float(reading) / 1000.0
        if i%100 == 1:
            print(temp)
        # print(temp)
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


        # print(GPIO.input(BUTTON_PIN))
        # If button is pressed, turn fan on
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
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
        
        i+=i
        time.sleep(.1)
