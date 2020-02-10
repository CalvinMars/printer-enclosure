import glob
import time
import datetime
import RPi.GPIO as GPIO

# Setup fan and button GPIO pins (23 and 10)
GPIO.setwarnings(False) # Turn off warnings
GPIO.setmode(GPIO.BCM)

FAN_PIN = 23
BUTTON_PIN = 10
GPIO.setup(FAN_PIN, GPIO.OUT) # Set fan pin
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set button pin, with initial value off

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

fan_state=False

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
        
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
    
wait_unit = min
wait_input = 5
if wait_unit == min:
    wait = wait_input * 60
else:
    wait = wait_input

 
while True:
    temp = read_temp()
    
    #timer = datetime.datetime.now()
    #print(temp)
    #f = open('/home/sam/Desktop/temp_log', 'a')
    #f.write('\n' + str(temp) + ',' + str(timer))
    #f.close()
    if GPIO.input(10) == GPIO.HIGH:
        GPIO.output(FAN_PIN, True)

    else:
        
    #Turn fan on if temperature is more than 40 degrees C
        if(float(temp) >= 40):
            if (fanstate == False):
                print("turning fan on")
                fan_state = True
                GPIO.output(FAN_PIN, True)
           
        else: # Turn fan off if less than 40 degrees C
            if (fanstate == True):
                print("turning fan off")
                fan_state = False
                GPIO.output(FAN_PIN, False)
    
    time.sleep(wait)