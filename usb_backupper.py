#!/usr/bin/env python
# Developped by : ShadMaN

import glib
import os
import datetime
import shutil
import argparse
import time
from pyudev import Context, Monitor
import RPi.GPIO as GPIO

# get parameters if available
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--maximum",type=int, help="Maximum file size to copy")
args = vars(ap.parse_args())

if args.get("maximum", None):
	max_size = args.get("maximum", None)
else:
	max_size = 10

# set up the LED pin to output
channel = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

try:
    from pyudev.glib import MonitorObserver
#when a new USB detected
    def device_event(observer, device):
    	if device.action == 'add' :
		print("a new drive detected")
    		time.sleep(3)
    		source_folder = "/media/pi/"+os.listdir('/media/pi/')[0]
    		files = os.listdir(source_folder)
    		newdir = datetime.datetime.now()
    		destination = '/home/pi/Desktop/backups'
		#create destination folder if not exists
    		if not os.path.exists(destination+'/%s'%newdir):
    			os.makedirs(destination+'/%s'%newdir)
    		destination=destination+'/%s'%newdir
    		try :
				# Turn on the LED and start the copying process
				GPIO.output(channel, True)
				#copy all files from USB to destination folder
				shutil.copytree(source_folder, destination+'/data')
				print("copying files from the drive")
				time.sleep(2)
				#Turn off the LED when complete
				GPIO.output(channel, False)
				exit(0)
    		except Exception as e:
    			exit(0)
        else :
        	print("device removed")
except:
    from pyudev.glib import GUDevMonitorObserver as MonitorObserver

    def device_event(observer, action, device):
        print('event {0} on device {1}'.format(action, device))

context = Context()
monitor = Monitor.from_netlink(context)

monitor.filter_by(subsystem='usb')
observer = MonitorObserver(monitor)

observer.connect('device-event', device_event)
monitor.start()

glib.MainLoop().run()

# Developped by : DevHB
