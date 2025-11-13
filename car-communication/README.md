## Car Communication Package

Allows a receiver car to receive odometer information (position, speed) from a sender car. 
*Note: make sure `sender_node` & `receiver_node` are in another subdirectory `car_communication/`* 

To use: (on both cars)
\
`source install/setup.bash`
\
`export ROS_DOMAIN_ID=30`

On the **SENDER** car
\
`ros2 run car_communication sender`

On the **RECEIVER** car
\
`ros2 run car_communication receiver`
