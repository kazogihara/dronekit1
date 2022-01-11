from dronekit import connect,VehicleMode,TimeoutError,mavutil
import time



def go_with_velocity(velocity_x,velocity_y,velocity_z,duration):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(0,0,0,mavutil.mavlink.MAV_FRAME_LOCAL_NED,0b0000111111000111,0,0,0,velocity_x,velocity_y,velocity_z,0,0,0,0,0)  

    for x in range(0,duration):
        vehicle.send_mavlink(msg)
        time.sleep(1)


vehicle = connect('localhost:14550',wait_ready=True)
print("connected")


vehicle.mode = VehicleMode("GUIDED")
while not vehicle.mode == "GUIDED":
    print("Wait for change mode")
    time.sleep(1)
print("mode: GUIDED")

vehicle.armed = True
while not vehicle.is_armable:
    print("Wait for arm")
    time.sleep(1)
print("Armed!")


try:
    print("takeoff")
    vehicle.wait_simple_takeoff(10,0.5,10)
except TimeoutError as e:
    print(e)

print("go square")
go_with_velocity(1,0,0,5)
go_with_velocity(0,1,0,5)
go_with_velocity(1,0,0,5)
go_with_velocity(0,-1,0,10)
go_with_velocity(-1,0,0,5)
go_with_velocity(0,1,0,5)
go_with_velocity(-1,0,0,5)

vehicle.mode = VehicleMode("LAND")
while not vehicle.mode == "LAND":
    print("Wait for change mode")
    time.sleep(1)

vehicle.close()
