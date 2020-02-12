# Printer Enclosure Program

These files are inteded to be used in the prusa printer enclosures at Calvin University on Raspberry Pi Zero W computers. The parts list is what was used for the 3 printer enclosures done in February of 2020.

### Pi ip adresses and usernames

- prusapi1: 153.106.1.50
- prusapi2: 153.106.1.51
- prusapi3: 153.106.1.52


## Parts

- 3x Raspberry Pi Zero W (with individual power supplies)
- 3x [Sunfounder RTC Nano](https://www.sunfounder.com/pcf8563-real-time-clock.html)
- 3x [IRF520 MOSFET Driver Module](https://www.amazon.com/IRF520-MOSFET-Driver-Arduino-Raspberry/dp/B07F7SV84V/ref=asc_df_B07F7SV84V/?tag=hyprod-20&linkCode=df0&hvadid=242027088707&hvpos=1o1&hvnetw=g&hvrand=16724190271650521161&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9017521&hvtargid=pla-489073861129&psc=1)
- 3x [12v Fan](https://www.amazon.com/Rosewill-Bearing-Computer-ROCF-13001-Standard/dp/B00KB8CB9O/ref=sr_1_6?keywords=5v+fan+120mm&qid=1580848486&sr=8-6)
- 3x [Toggle switch for fans](https://www.amazon.com/Rocker-Switch-Household-Appliances-MXRS/dp/B07L9JWVVR/ref=sr_1_12?keywords=toggle%2Bswitch%2B10000%2Bpack&qid=1581039736&sr=8-12&th=1)
- 1x [Momentary Switch for power](https://www.amazon.com/dp/B015X34IP6/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B015X34IP6&pd_rd_w=bGWUs&pf_rd_p=45a72588-80f7-4414-9851-786f6c16d42b&pd_rd_wg=BAYmB&pf_rd_r=KWFACYN015Y4N8E34SGD&pd_rd_r=2679690b-2d48-42c0-b261-dad01652c70b&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFCUUYwVFkwRk00QkcmZW5jcnlwdGVkSWQ9QTAyMzUwNTUyUFk3OUc4UEJETTVYJmVuY3J5cHRlZEFkSWQ9QTAxODQ4NjkzVTJVSEFGVVg2QUhGJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)   
- 1x [Individually addressable LED Strip](https://www.amazon.com/BTF-LIGHTING-WS2812B-Individual-Addressable-Non-waterproof/dp/B01CDTEJBG/ref=sr_1_1_sspa?crid=EMRRIWRZHQS7&keywords=individually%2Baddressable%2Bled%2Bstrip&qid=1580324344&sprefix=individually%2Baddressable%2Caps%2C158&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTTE2OU5WQjQ0ODZXJmVuY3J5cHRlZElkPUEwMTc3MzQzMlpJRFVPTlJSNzRBUSZlbmNyeXB0ZWRBZElkPUEwNzc0Mjk0RUxJNU9YV0EwODJaJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1)

## Wiring
![photo](https://lh3.googleusercontent.com/vem8Xpil1XM2C7p8tA4gBcofuDyzzfPfsX5OXxg9VfzfKP1tbHLu8hUG-KteC0AZJ6uWhpcQD0DmmX6Aw1TZv-hNVxh7ZVBDOzPwixHhLcQg2viSHejO4xptIUXBe_FAw781i3yH_QMA6jomYAwFAA_HaoVXMZO6B-VuAA-JJI6zUm_gjI9jph5U5eCUvJ48uEyIOzU6pF8kY4X2xopHPaWvubHASvXQcC7t1_mpIEWcxbnxZuNRhOMC_fbqZfLebb5kXUgUb_05FqJTMYhy0yMPImNJc8IPRCotHr17aQlaQZVoft_ivHJcl6Au-tMD54X-tsnC3U4g0c0ATsdpMvgjNfNDxPMy0YTSqJoi7LOJz-riLmuCNxNw7iZiTsxusFPiPOfWISlRvLHkCcwg8p5muvBQHrNXqJwzQOSqr22gtDOd6V9LeZ8u712bkkkzfqqxwNOJH2en-RSUNeSz3en-2dr7BSvuz4_A0mkxIdpryc1qToxiKK0HbbzRTIj47JFRQzk9AiAxOpBQklhgioQYgDwpqKHbZGDh0sHPUcwthV5wpYsCL1eppj-PDlD8TMEv9BtTtAww4-GLOlWQxZqz9gNU5dj1WNuxnvJgr5WtNXu18sh7WtpKLf_hI5dw00a3-Cu9w6QFWhJhzLZtz5jqe7kV52oX3fiGTa8VEVmYj2IyfCY3J1o=w906-h731-no)

![Single Module](https://lh3.googleusercontent.com/f9M_e5tYCQ0vInbCXLP84DLRWwk6WJmVoZw4nX364aKirdTtrSSYpBhqQ85vCfKRRTyhZA7PVK03ddK8HlkA1MHGGPrKLjVMfFOgy7F0KK5HOP_ZQk2nyVU01CV53AeUc69GKBvplC4dDNA15BVLAclBdp-AjkdPnM7eXXeSr3GHaP5uLpKxbhKukn-B64q0zoceNA7kWilyXFOl8SaNo0iWrBjxEqSvxKd2P4E7-UPGuh85sOLUFJUYPnvW3HlKLFV1ohZs9evpg8VLU8NRE0Xnn7fxEAGBZHsvVhmwQU_X0mMB1d0Bs1Cpr1l7yHfQyc1rgbjoAN2CB14h6EZ54_-gVLEcZqHhI4K-ZMYU6peN3cRVUUwkWJ_-iQT_L9gkN3BM0RMBy5OON2-brdt4NeZfRTn6_5CGYrcwSMAPogg8n5805s_Wd-73KqCU-TfMpiyWbVTSdzuDSgX9-RdICye_aQVw1jduP2VCNZbDiB9VsQOJaCScEM64F8N3rsBfC9z1mN3eDF9zfXhLTsECTSghbi1fRbHxSMIgAhCEatqAGGL9x2Ov2hZYOv2hdbwwpUeshSRK-VHLY5WxRw12wQRRYDUrG1lxoXiRYHCJkkA8bNQEjN92ohvMOBLvqdzcfowZw6TU84Irp2iH2BqQtE9-7zDWNpZIuXYvxuXisQyQmkvX0iKNxkpmh0v3hqRhbZlaB-9ozdUC04mgqEAaEO8wFqFN-uBL9DDz5dQIR21FXCVC=w632-h871-no)

The same (12v) power supply is used for all of the fans and another (5v) is used for all of the LEDs.

*Note the RTC module is not the same as the one used, the labels on the leads are incorrect.*

### Pin reference for Pi

Fan switch
| Pin | Name    | Connect To   |
|-----|---------|--------------|
| 4   | 5v      | Switch pin 1 |
| 13  | GPIO 27 | Switch pin 2 |

RTC-Nano
| Pin | Name   | Connect To  |
|-----|--------|-------------|
| 1   | 3.3V   | 3.3V        |
| 3   | SDA    | SDA         |
| 5   | SCL    | SCL         |
| 7   | GPIO 4 | ds18b20 Out |
| 9   | GND    | GND         |

MOS Module
| Pin | Name    | Connect To |
|-----|---------|------------|
| 14  | GND     | GND        |
| 18  | GPIO 24 | SIG        |

LED Strip
| Pin | Name    | Connect To |
|-----|---------|------------|
| 20  | GND     | GND        |
| 22  | GPIO 25 | Din        |

LED Switch
| Pin | Name    | Connect To  |
|-----|---------|-------------|
| 6   | GND     | Yellow wire |
| 11  | GPIO 17 | Green wire  |

## Setup
Setup the raspberry pi so that all of the code will work.
### Temperature probe
To use RTC-nano module on Raspberry Pi, you need to complete some configuration. Here two ways are provided: auto-configuration by script and manual configuration.
**Auto-configuration:**

1. Log into the Raspberry Pi, open a terminal.
2. Download the package by github:
```
git clone https://github.com/sunfounder/SunFounder_RTC_Nano.git
```
3. Get into the code directory to install:
```
cd SunFounder_RTC_Nano 
sudo ./install
```
![Terminal image](http://wiki.sunfounder.cc/images/6/68/Rtc-nano.png)

**Prompts in installation:**

You'll be prompted about whether to sync the time on the Raspberry Pi to the RTC or not; if you type in no, you can set it manually.
In manual setting, type in the date and then time, and the setting value will be saved as the time on the RTC module.
When the setting is done, you will see a reboot prompt, type in yes.

*For manual installation, please see the RTC-nano wiki page linked below*

After the library installation is done, we can import this in Python programming. For the library’s API and documentation, please refer to the Appendix.

*Taken from the SunFounder wiki on the RTC-Nano device. ([Link](http://wiki.sunfounder.cc/index.php?title=RTC-Nano#Configuration))*

### GPIO Setup

If the RPi.GPIO library is not installed on the Pi (comes preinstalled in some pis), use these commands to install the RPi.GPIO library:
```
sudo apt-get update
sudo apt-get -y install python-rpi.gpio
```

### LED Strip Setup

Before we install the Raspberry Pi library for the WS2812 LEDs, some preparations have to be made:

1. The package sources are updated:
```
sudo apt-get update
```
2. We install the required packages (confirm with Y):
```
sudo apt-get install gcc make build-essential python-dev git scons swig
```
3. The audio output must be deactivated. For this we edit the file
```
sudo nano /etc/modprobe.d/snd-blacklist.conf
```
Here we add the following line:
```
blacklist snd_bcm2835
```
Then the file is saved by pressing CTRL + O and CTRL + X closes the editor.

4. We also need to edit the configuration file:
```
sudo nano /boot/config.txt
```
Below are lines with the following content (with Ctrl + W you can search):
```
# Enable audio (loads snd_bcm2835)
dtparam=audio=on
```
This bottom line is commented out with a hashtag # at the beginning of the line: `#dtparam=audio=on`

5. We restart the system
```
sudo reboot
```

Now we can download the library.
```
git clone https://github.com/jgarff/rpi_ws281x
```
In this directory are on the one hand some C files included, which can be easily compiled. The example code for this is easy to understand. In order to use them in Python, we need to compile them:
```
cd rpi_ws281x/
sudo scons
```
However, in this tutorial we are mainly interested in the Python variant and therefore switch to the Python folder:
```
cd python
```
Here we carry out the installation:
```
sudo python setup.py build
sudo python setup.py install
```
This will allow us to carry out a first test in the next step.

*This is taken from the website [tutorials-raspberrypi.com](https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/) article on the NeoPixel LED strip.*

### Setup Auto Script running
**Auto Login Setup**

The first step is to enable the Pi to login automatically without requiring any user intervention. This step is optional.

At the command prompt or in a terminal window type :
```
sudo raspi-config
followed by Enter.
```
Select “Boot Options” then “Desktop/CLI” then “Console Autologin”

**Prepare Script**

My test script is called “myscript.py” and is located in /home/pi/. This is what it contains :
```
#!/usr/bin/python
print("******************************************************")
print("* This is a test script. There are many like it,     *")
print("* but this one is mine. My script is my best friend. *")
print("* It is my life. I must master it as I must master   *")
print("* my life.                                           *")
print("******************************************************")
```
You can download this directly to your Pi by using the following command :
```
wget https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/myscript.py
```
I strongly suggest getting this working before trying any other scripts!

**Auto-run Script Setup**

Now we need to tell the operating system to run the script for the Pi user. In the command prompt or in a terminal window type :
```
sudo nano /etc/profile
```
Scroll to the bottom and add the following line :
```
sudo python /home/pi/myscript.py
```
where “/home/pi/myscript.py” is the path to your script.

Type “Ctrl+X” to exit, then “Y” to save followed by “Enter” twice.

**A Script Without End**

You will only be returned to the command line when your script is complete. If your script contains an endless loop then you may want to use this line in the profile file instead :
```
sudo python /home/pi/myscript.py &
```
This will allow the script to run in the background but you will not see any text output from it.

**Reboot and Test**

To test if this has worked reboot your Pi using :
```
sudo reboot
```
When it starts up your script will run and you will see something like this :
```
Autorun script result
```
Due to the technique we’ve used the script is run whenever the Pi user logs in. This means if you create other terminal sessions (via SSH for example) the script will run each time.
