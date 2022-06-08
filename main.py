from duplicater import mailcopier
import json

f = open('config.json')
data = json.load(f)

mailcopier(number= str(data["number"]), orginalmail= data["mail"], location= data["saveFileLocation"])