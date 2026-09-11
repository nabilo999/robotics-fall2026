# Mission 1

## Command Path Explanation

A proposed command travels on /student_cmd_vel. The guard checks the proposed movement and then publishes the approved command on /cmd_vel.

## Graph Explanation

ros2 graph is the connection of different root systems described as nodes. shows us how they communicate with each other

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

I found the ranges field, which represents distance measurements from the LiDAR around the robot.  

- 3.1357498168945312 - 3.0510787963867188 - 3.0570406913757324 - 2.017237663269043 - 2.0161142349243164

## Tools Explanation

Gazebo simulates the robot's movement, sensors, and physics checks. while RViz is responsible for displaying ROS 2 data so a person can inspect it.
