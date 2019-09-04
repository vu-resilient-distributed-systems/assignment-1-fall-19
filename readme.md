**Assignment 1 - Due September 10**

**Setting up multi-agent car following experiment with TORCS using TCP**

******************

**Due: 1 week**

In this assignment you will learn to use TORCS – An open source car
racing simulator, and setup an experiment for car platooning. In this
scenario there will be two cars namely the leader and the follower. The
leader car is responsible to maintain a set speed for the platoon, and
to drive within the tracks. The follower car is responsible to follow
the leader car maintaining a minimum distance (dmin).

Now, for the follower car to maintain an accurate dmin it has to receive
the speed (V) information of the leader car. Once, it receives the speed
value, it readjusts its speed in order to accurately maintain dmin. So,
for this information exchange you will need to setup a TCP network
between the two cars.

The code we provide have two PID controllers that control
the steering and speed of the cars. Brief summary of the cars and their
controllers are explained below:

**Car 1:** Also referred to as the leader car. Uses two PID controllers
which take in the LIDAR data, position sensor, and speed sensor values
to compute the steer and speed actions to maintain the car within the
track.

**Goals:** (1) Maintain target speed (V = 60 mph), and (2) maintain
appropriate steering to stay within the track.

**Car 2:** Also referred to as the follower car. Uses two PID
controllers which takes in the LIDAR data, position sensor, and speed
sensor values to compute the steer and speed actions to maintain the car
within the track. In addition, it also uses information from the leader
car to maintain a minimum distance (d = 10m) from the front car.

**Goals:** (1) Maintain minimum distance from the leader car, and (2)
maintain appropriate steering to stay within the track.

*****

**Scripts** 
-   Controller.py has the PID controllers for the two cars.

-   TorcsEnv.py is the simulator code which has all the functionalities for simulator - controller interaction.

-   Car.py is the skeleton code which has to be completed by you for the platoon experiment.

**Tasks to be completed**

-   Installing and setting up TORCS for the experiment. \[30 points\]

-   Setup a TCP network between the Car’s to relay speed information of
    the leader car to the follower car. \[30 points\]

-   Collect the following sensor data of the follower car in a csv file: Speed (in X,
    Y, Z orientation), position on track, gear, distance from start,
    distance from opponent, rpm, damage, steer, acceleration, and brake.
    \[10 points\]

-   Collect the speed (V) of the two cars in csv file and plot them
    using Matplotlib. \[15 points\]

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

**TORCS Multi-Car setup Program Flow**

![Program Flow](https://github.com/Shreyasramakrishna90/TORCS/blob/master/TORCS%20Program%20Flow.png)

**Useful References**

-   Installing TORCS: https://github.com/fmirus/torcs-1.3.7#torcs-137

-   Setting up TORCS for multi-car experiments (important to get started): [PDF](https://github.com/vu-resilient-distributed-systems/assignment-1-fall-19/blob/master/Setting%20Up%20Multi-Car%20Experiments%20with%20TORCS.pdf)

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
