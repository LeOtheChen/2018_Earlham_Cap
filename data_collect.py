import csv
import serial
ser = serial.Serial('/dev/cu.usbmodem1421',9600)
with open('data.csv','w',newline='') as csvfile:
	writehandle = csv.writer(csvfile)
	while True:
		byte2string = ser.readline().decode('utf-8')
		line = byte2string.translate('/r/n')
		splitted = line.split(",")
		writehandle.writerow(splitted)	 
ser.close
