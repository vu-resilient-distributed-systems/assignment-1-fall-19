# Assignment 1

**Due September 12**

The goal of this assignment is to help you understand different mechanisms to setup a distributed communication between two process. As part of the assignment, we have provided you instructions to setup TORCS -- an open source car racing simulator. The instructions are available [here](MultiCarSetupWithTorcs.pdf). Note that you should use a Linux machine, preferably latest version of ubuntu. If you doo not have a linux machine you can try this on a virtual machine. See the instructions for setting up a virtual machine with linux at https://github.com/vu-resilient-distributed-systems/lectures-fall-2019, section getting started.

## Assignment Contents

The assignment folder contains the following files

* **Car.py** -- this contains the code skeleton for two cars. They receive their state from the simulator, then use the controller to compute the actuation signals and finally send the actuation commands back to the simulator. **The parts of the networking code to be filled have been marked with numbers**. 
* **Controller.py** -- Two PID controllers that control the steering and speed of the cars. The PID controller of the leader car  takes in the LIDAR data, position sensor, and speed sensor values to compute the steer and speed actions to maintain the car within the
track. It tries to maintain a  target speed (V = 60 mph) and controls steering to stay within the track. Note the V=60 is set in the car.py at line 14. You can change it to see what happens. But for the initial tasks keep this at 60. The controller for the second car
es the  PID controllers which takes in the LIDAR data, position sensor, and speed sensor values to compute the steer and speed actions to maintain the car within the track. In addition, it also uses information from the leader car to maintain a minimum distance (d = 10m) from the front car. This expected distance is hard coded in the controller. So do not change it.
* **TorcsEnv.py** --is the simulator code which has all the functionalities for simulator - controller interaction. (TORCS simulation code)

These three files should be downloaded to your machine. You can use the git clone for that. Your goal is to fill the contents of the car.py to ensure that you are able to simulate the car following scenario as described below.

## Car following scenario

In this scenario there are two cars namely the leader and the follower. The
leader car is responsible to maintain a set speed for the platoon, and
to drive within the tracks. The follower car is responsible to follow
the leader car maintaining a minimum distance (dmin).

To maintain an accurate dmin the follower car has to receive
the speed along the x axis of the leader car. Once, it receives the speed
value, it readjusts its speed in order to accurately maintain dmin.

## Program Flow

The program flow between the various components is shown in the figure below.

![Program Flow](https://github.com/vu-resilient-distributed-systems/assignment-1-fall-19/blob/master/ProgramFlow.png)


## Tasks to be completed

-   Reading and write a reconstructive summary of the [publish subscribe paper](https://github.com/vu-resilient-distributed-systems/lectures-fall-2019/blob/master/Module-2-MiddlewareAndBackend/reading/TheManyFacesOfPublishSubscribe.pdf). Focus on the concepts learned and concepts that you have a question about. 
-  Installing and setting up TORCS for the experiment. \[10 points\]
-  Setup a TCP network between the Car’s to relay speed information of     the leader car to the follower car. The networking section of the Car.py is marked with numbers and you will have to complete it. \[30 points\]

-   Collect the following sensor data of the follower car in a csv file: Speed (in X,
    Y, Z orientation), position on track, gear, distance from start, damage, steer, acceleration, and brake.
    \[15 points\]

-   Plot the speed (S['SpeedX']) of the two cars using Matplotlib. \[10 points\]

-   Answer the following questions: \[15 points\]

    -   Does the TORCS simulator work in a blocking or non-blocking
        manner?

    -   What is the simulation time step of TORCS.

    -   How long is your python script taking to compute the control
        action? What will happen if your scripts takes longer to compute
        than the simulation time step?

    -   Is TCP or UDP better for a V2V network in this experiment?
        Compare time overhead for a TCP reply vs. the criticality of the
        information being relayed.

**Submissions**

-   Submit your code and a readme explaining how to run your submission.

-   Submit required csv files and plots. Clearly describe the plots. 

-   Submit answers to subjective questions.


**Useful References**

-   Installing TORCS: https://github.com/fmirus/torcs-1.3.7#torcs-137

-   Setting up TORCS for multi-car experiments (important to get started): [PDF](https://github.com/vu-resilient-distributed-systems/assignment-1-fall-19/blob/master/Setting%20Up%20Multi-Car%20Experiments%20with%20TORCS.pdf)

-   Reference Code for using sensors and actuators in TORCS: http://xed.ch/p/snakeoil/

-   TORCS Manual:
    [*https://arxiv.org/pdf/1304.1672.pdf*](https://arxiv.org/pdf/1304.1672.pdf)

-   Familiarizing with TORCS :
    [*http://www.berniw.org/tutorials/robot/tutorial.html*](http://www.berniw.org/tutorials/robot/tutorial.html)

-   Papers using TORCS simulator:

    -   [*https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=5286466*](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=5286466)

    -   [*https://ieeexplore.ieee.org/document/5286480*](https://ieeexplore.ieee.org/document/5286480)

        [*http://deepdriving.cs.princeton.edu/paper.pdf*](http://deepdriving.cs.princeton.edu/paper.pdf)

Note: Video for the multi-agent TORCS experiments can be found at:
<https://www.youtube.com/watch?v=T0XEiCNlq9k>
