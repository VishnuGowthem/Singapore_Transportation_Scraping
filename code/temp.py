#to scrape subzone and planning area data from 

#importing urllib2, beautifulsoup and csv
import csv
from bs4 import BeautifulSoup
import httplib
import urllib
import unicodecsv
import json
from selenium import webdriver

with open('/Users/VishnuGT/Programming/PythonPrograms/TempNodes.csv', 'rb') as f:
    reader = csv.reader(f)
    busnodes_xy_list = list(reader)

#print busnodes_xy_list
#open a cursor to csv
with open('/Users/VishnuGT/Programming/PythonPrograms/Temp_Results.csv','wb') as f1:
    writer=unicodecsv.writer(f1, delimiter=',', lineterminator = '\n')
    #header row
    writer.writerow(["GEO_SPATIAL_KEY","SUBZONE","PLANNING_AREA"])
  
    #Token from onemap on registering 
    onemaptoken = "OmhQrshNuIlE96zT0NBLUJedUSLj3N4HDGWKPvIfoYBuE+2JKud5n3+Ci7Sbpw8w9Ziwp/AcdAszqrQQT2qCGS4UKIuaLlmI2w2mxtcOhwbWfmbs3jNUCw==|mv73ZvjFcSo=" 
 
    for i in range(len(busnodes_xy_list)):
	#skipping header row
	if i != 0:
		geo_node = busnodes_xy_list[i][0]
        	x_coordinate = busnodes_xy_list[i][1]
		y_coordinate = busnodes_xy_list[i][2]

		subzone_html_link = "http://www.onemap.sg/DOSAPI/Service1.svc/GetPolyFromPt?token=qo/" + onemaptoken + "&querypoint=" + x_coordinate + "," + y_coordinate + "&lyrname=SUB_ZONE"
		planning_area_html_link = "http://www.onemap.sg/DOSAPI/Service1.svc/GetPolyFromPt?token=qo/" + onemaptoken + "&querypoint=" + x_coordinate + "," + y_coordinate + "&lyrname=PLANNING_AREA"
		urlhandle = urllib.urlopen(subzone_html_link)
		content = urlhandle.read()
		json_subzone_data = json.loads(content)
		if json_subzone_data['features']:
			print "testing"
			subzone_str = json_subzone_data['features'][0]['attributes']['subzone_n']
		else:
			subzone_str = "EMPTY"
		urlhandle = urllib.urlopen(planning_area_html_link)
		content = urlhandle.read()
		json_planning_data = json.loads(content)
		if json_planning_data['features']:
			planning_str = json_planning_data['features'][0]['attributes']['PLN_AREA_N']
		else:
			planning_str = "EMPTY"
	
		#print "Subzone : "
		#print subzone_str     
		#print "Planning Area : "
		#print planning_str
		row = [(geo_node),(subzone_str),(planning_str)]	
    		writer.writerow(row) 
f1.close()

