#Train Locator
#created by Jake Lukawski

import requests
import time
import xml.etree.ElementTree as elementTree
import stationid

key = '' # Your key (See https://www.transitchicago.com/developers/traintrackerapply/)

def main():
  locator()

def locator():
        selectedStation, line = stationid.stationid()
        selectedStation = str(selectedStation)
        timeFormat = '%Y%m%d %H:%M:%S'
        url = requests.get('http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key='+key+'&mapid='+selectedStation)
        url = url.text
        root = elementTree.fromstring(url)
        i = 3
        timestamp = root[0].text
        timestamp = int(time.mktime(time.strptime(timestamp, timeFormat)))
        station = root[i][2].text
        route = formatLine(line)
        print ('------------------------------\nStation: {} ({} line)'.format(station,route))
        for each in root:
                try:
                        run = root[i][4].text
                        route = root[i][5].text
                        destination = root[i][7].text
                        arrival = root[i][10].text
                        arrival = int(time.mktime(time.strptime(arrival, timeFormat)))
                        if route == line:
                                prediction = arrival - timestamp # in seconds
                                if prediction < 60:
                                        prediction = 'DUE'
                                else:
                                        prediction = str(round(prediction/60)) + ' min' # in minutes 
                                print ('------------------------------\nRun {} to \n{:<20}{:>10}'.format(run,destination,prediction))
                except IndexError:
                        pass
                i = i + 1
        print ('------------------------------')
        repeat = input("Press enter to select new station")
        if repeat == '':
                locator()
                
def formatLine(line):
    if line == 'G':
        line = 'Green'
    if line == 'Brn':
        line = 'Brown'
    if line == 'P':
        line = 'Purple'
    if line == 'Org':
        line = 'Orange'
    if line == 'Y':
        line = 'Yellow'
    return line

if __name__== "__main__":
  main()
