#Main scripts which calls the controller and the TorcsEnv scripts
#Invokes the drive_example function which has both the leader car and the follower car functionalities
#Includes random generation of leader car speeds and its position on the track
#Refer: http://xed.ch/p/snakeoil/ for sensor and actuator functionalities

import Controller#imports PID controllers
import TorcsEnv#TORCS simulation functions
import csv
import socket
import threading#for threading
from threading import Thread

#Variables required for setting the PID controls
targetSpeed = 60.0 #target speed the leader car has to maintain
targetStrE = 0.0
Vl = 0.0 # leader car velocity

#Define a publisher socket for LeaderCar to publish its Speed Vl
def Publisher():

    #Refer to github examples to create TCP Client socket

    return sock1

#Define a subscriber socket for the FollowerCar to receive the speed Vl from the LeaderCar.
def Subscriber():

    #Refer to github examples to create TCP Server socket

    return sock2

#Define a Car1 function that receives the sensor data from the simulator and computes the actuations.
#Use the Sensor values in the PID controllers from controller.py to compute actuations R['accel'], R['steer'],R['gear']
#Then respond to the server with the actuation values
def Car1(sock1,CS):
    #1. Connect to car2's server socket
    
    for step in range(CS[0].maxSteps, 0, -1):#The simulation steps

    #2. get sensor inputs
    CS[0].get_servers_input()
    S, R = CS[0].S.d, CS[0].R.d #S --sensors and R--actuators

    #3. compute the actuations R['accel'], R['steer'],R['gear'] for the first car using PID controllers for LeaderCar
    R['steer'] = Controller.steeringControl(S, targetStrE)
    R['accel'] = Controller.speedControl(S, R, targetSpeed)
    R['gear'] = Controller.automaticGear(S)

    #4. Send S['SpeedX'] to the followercar using the publisher

    #5. Log the sensor and actuator data S['SpeedX'], S['SpeedY'], S['SpeedZ'], R['accel'], R['steer'], R['gear'] to a buffer

    # Respond the actuation values to the simulator
    CS[0].respond_to_server()

#Define a Car2 function that receives sensor data from simulator, Speed S['SpeedX'] from the leader car and computes the actuations
#Use the Sensor values in the PID controllers from controller.py to compute actuations R['accel'], R['steer'],R['gear']
#Then respond to the server with the actuation values
def Car2(sock2,CS):
    #1. Listen on the server socket
    
    #2. Accept the connection from car1. Use the accepted socket to receive input below
    
    for step in range(CS[1].maxSteps, 0, -1):#The simulation steps

    #3. Receive the speed value sent by the car 1 as a new variable Vl from the LeaderCar using the subscriber socket.

    #get sensor inputs similar to the Leader Car
    CS[1].get_servers_input()
    S, R = CS[1].S.d, CS[1].R.d #S --sensors and R--actuators

    #compute the actuations R['accel'], R['steer'],R['gear'] for the first car using PID controllers for LeaderCar
    #Vl refers to the speed S['SpeedX'] of the LeaderCar
    R['steer'] = Controller.ACCSteeringController(S)
    [acc, brake, Xr] = Controller.ACCVelocityController(Vl, S)
    R['accel'] = acc
    R['brake'] = brake
    R['gear'] = Controller.automaticGear(S)

    #4. Log the sensor and actuator data S['SpeedX'], S['SpeedY'], S['SpeedZ'], R['accel'], R['steer'], R['gear'] to a buffer.

    #Respond the actuation values to the simulator
    CS[1].respond_to_server()


#Define main which calls three threads one each for LeaderCar, FollowerCar.
def main(CS):

    #call the publisher and subscriber functions to create publisher and subscriber sockets.
    sock1 = Publisher()
    sock2 = Subscriber()

    #Create three threads to call the LeaderCar, FollowerCar and Buffer functions.
    FollowerThread = Thread(target=Car2, args = (sock2,CS))
    FollowerThread.daemon = True
    FollowerThread.start()

    #1. do the same for the other car

    #2. Join the threads

if __name__ == "__main__":
    #Adding different clients to the simulation
    CS=[TorcsEnv.Client(p=P) for P in [3001, 3002]]
    main(CS)#main function
