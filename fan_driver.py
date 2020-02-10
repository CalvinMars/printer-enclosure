import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
FAN_PIN = 23
GPIO.setup(FAN_PIN, GPIO.OUT)


textFile = open("temp_log.txt", 'r')

fanstate=False
for x in range(40):
    lastLine = textFile.readline()
    temp = lastLine[-10:-1]
    print(temp)
    if(float(temp) >= 40):
        if (fanstate == False):
           print("turning fan on")
           fanstate = True
           #GPIO.output(FAN_PIN, True)
    else:
        if (fanstate == True):
            print("turning fan off")
            fanstate = False
            #GPIO.output(FAN_PIN, False)

        

textFile.close()