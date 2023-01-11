### Distance calculation using Ultrasonic detection when a key on a keyboard is pressed
More information can be found on pdf file.

Addthe extractedd file to the catkin_ws file.

1. Execute keyboard library
------------
```sh
cd ~/catkin_ws
catkin build
source ~/catkin_ws/devel/setup.bash
(in this place, "cd ~/catkin_ws" may be needed)
rosrun keyboard keyboard
```

In another terminal
```sh
rostopic list
rostopic echo /chatter
```
Testing can be done: press a random key on a terminal that appears.

2. Execute keypressed node
------------
```sh
cd ~/catkin_ws
catkin build
source ~/catkin_ws/devel/setup.bash
rosrun mmi_package keypressed_node.py
```
In another terminal
```sh
rostopic list
rostopic echo /dkey
```


3. Execute nh node on Arduino
------------
Open publisher.ino file on Arduino software, upload the code to the Arduino (already connected by scheme to the sensor).
Make sure the Board chosen in the Tools section is "Arduino UNO" and Serial Port is /dev/ttyACM0
```sh
rosrun rosserial_python serial_node.py /dev/ttyACM0
```

In another terminal:
```sh
rostopic list
rostopic echo /chatter
```

4. Execute distrange node
------------
```sh
cd ~/catkin_ws
catkin build
source ~/catkin_ws/devel/setup.bash
rosrun mmi_package distancerange_node.py
```

In another terminal:
```sh
rostopic list
rostopic echo /distrange
```
