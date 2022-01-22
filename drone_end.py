from flask import Flask
from dronekit import connect,VehicleMode,TimeoutError,mavutil
import time

SUCCESS_CODE="0"

app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/rtl')
def rtl():
    vehicle = connect('localhost:14550',wait_ready=True)
    print("connected")
    vehicle.mode = VehicleMode("RTL")
    while not vehicle.mode == "RTL":
        print("Wait for change mode")
        time.sleep(1)
    vehicle.close()
    return SUCCESS_CODE

app.run(port=8000, debug=True)