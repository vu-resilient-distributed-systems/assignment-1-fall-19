'''
Skeleton script which calls the controller and the TorcsEnv scripts
Invokes the drive_example function which has both the leader car and the follower car functionalities
Use the PID controllers in Controller.py to complete the code for multi-agent experiment setup.
'''

import Controller
import TorcsEnv

def drive_example(c, num):
    S, R = c.S.d, c.R.d

    if (num==0):
        # The leader car code goes here. You will have to use the PID controller to compute steer, speed, gear for the car.
        # Towards the end of this loop you will have to publish speed information using TCP to the follower car.

    if (num==1):
        # The follower car controller code goes here. You will have to use the PID controller to compute steer, speed, gear for the car.
        # You will have to receive speed of leader car using TCP and use in the PID controller code.

if __name__ == "__main__":
    #Adding different clients (cars) to the TORCS simulation
    CS=[TorcsEnv.Client(p=P) for P in [3001, 3002]]
    for step in range(CS[0].maxSteps, 0, -1):#The simulation steps
        num = 0
        for C in CS:
            C.get_servers_input()#Get sensor values from the simulator
            drive_example(C, num)#Invoke the python client for the car controller
            C.respond_to_server()#Send the actuator control signals to the simulator
            num+=1
    C.shutdown()
