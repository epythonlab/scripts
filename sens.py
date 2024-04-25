import os
import sys
from com.dtmilano.android.viewclient import ViewClient

device, serialno = ViewClient.connectToDeviceOrExit()

# Get the sensor data
sensor_data, _ = device.shell('dumpsys sensorservice')

# Print the sensor data
print(sensor_data)
