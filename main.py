from yeelight import *
import json



devices_array = []
devices_list = discover_bulbs()
for device in devices_list:
	devices_array.append(Bulb(device['ip']))


print(devices_array)
