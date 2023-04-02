import psutil

battery= psutil.sensors_battery()
# print(psutil.sensors_fans())

print("Your device battery percentage is: ",battery.percent)