import json, urllib2, requests

# How to find sensor ID?
# 1. Find station ID here: http://api.gios.gov.pl/pjp-api/rest/station/findAll (example: 129)
# 2. Find sensor ID here: http://api.gios.gov.pl/pjp-api/rest/station/sensors/129 (example: 744)
# 3. Enter sensor ID below:
sensorId = "744"

pm = urllib2.urlopen('http://api.gios.gov.pl/pjp-api/rest/data/getData/' + sensorId)
wjson = pm.read()
wjdata = json.loads(wjson)
pm25 = wjdata['values'][2]['value']
if pm25:
 pm25 = str(pm25)
 sep = '.'
 pm25 = pm25.split(sep, 1)[0]
 print pm25