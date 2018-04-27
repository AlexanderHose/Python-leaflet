import googlemaps
from datetime import datetime
import csv
import sys
import json
import time

def findLocations():
	gmaps = googlemaps.Client(key='') #Googlemaps Key
	count = 0
	v = True
	#Define save point of json file
	file = open('result.json', 'w')
	feeds = []
	
	#location of csv file
	with open('export.csv', 'r', encoding='ISO-8859-1') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			try:
				#rows from the csv file which should be parsed to Google
				print("[+] Searching for: " + row[0].split(';')[2] + " - " + row[0].split(';')[3])
				geocode_result = gmaps.geocode(row[0].split(';')[3] + ", " + row[0].split(';')[2])
				feeds.append(geocode_result)
				if(v):
					print (geocode_result)
			except (IndexError, googlemaps.exceptions.Timeout) as e:
				print(e)
				pass
			count += 1
		json.dump(feeds, file, separators=(',',':'))	
		file.close()

def plotMap():
	try:
		result = open('result.json', 'r')
		parsed = json.load(result)
		for index in range(len(parsed)):
			print(json.dumps(parsed[index][0]['geometry']['location']))
	except (ValueError, IndexError) as e:
		print(e)
		pass

result = input("Enter option [1 = Search for locations]: ")
if(result == "1"):
	findLocations()
elif(result == "2"):
	plotMap()
