# Week 1: Discovering a Robot Through ROS 2

## Student

- Name: Nabil Said
- Email: NABIL.SAID54@login.cuny.edu

## mission_1.command_path_explanation

A proposed command travels on /student_cmd_vel. The guard checks the proposed movement and then publishes the approved command on /cmd_vel.

## mission_1.graph_explanation

ros2 graph is the connection of different root systems described as nodes. shows us how they communicate with each other

## mission_1.guided_checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## mission_1.scan_observation

I found the ranges field, which represents distance measurements from the LiDAR around the robot.  

- 3.1357498168945312 - 3.0510787963867188 - 3.0570406913757324 - 2.017237663269043 - 2.0161142349243164

## mission_1.tools_explanation

Gazebo simulates the robot's movement, sensors, and physics checks. while RViz is responsible for displaying ROS 2 data so a person can inspect it.

## mission_2.measurement_explanation

In the Curve trial, the estimated traveled path measures the distance the robot actually traveled along its curved route, while the start-to-end distance measures the straight-line distance between its starting and ending positions. that is why the straight-line distance is shorter than the curved path.  

## mission_2.modified_settings

{'angular_z': 0.6, 'duration': 4.0, 'linear_x': 0.12}

## mission_2.motion_comparison

I predicted that the robot would rotate in place because its forward speed was 0 m/s and its turning speed was 0.5 rad/s. The measured direction change was 55.4°, while the estimated traveled path was 0 m, which shows that the robot turned without moving forward.

## mission_2.prediction_locks

{'curve': '2026-09-10T17:36:10.406521+00:00', 'curve_modified': '2026-09-10T17:43:33.413193+00:00', 'rotation': '2026-09-10T17:31:15.966658+00:00', 'straight': '2026-09-10T17:17:52.726529+00:00'}

## mission_2.predictions

{'curve': 'I predict a n eartic movement because its always changing direction and moving forward', 'curve_modified': 'This curve should be wide because a bigger radius means a wider turn', 'rotation': 'I predict its position will stay the same while its direction will keep spinning', 'straight': 'I predict the robot will move straight forward without turning.'}

## mission_2.safety_explanation

The command guard checks every proposed driving command and prevents invalid or overly large speeds from reaching the robot.  
The final zero command stops the robot at the end of the trial by setting the forward speed and turning speed to zero.  
The timeout is needed if the program crashes or stops communicating while the robot is moving. It automatically sends a stop command after 0.5 seconds without receiving a new command.  

## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'behavior': {'changed': True, 'normal': True}, 'deliberative': {'changed': True, 'normal': True}, 'hybrid': {'changed': True, 'normal': True}, 'reactive': {'changed': True, 'normal': True}, 'safety': {'changed': True, 'normal': True}}

## part_3.activity

{'communication': {'service': True, 'topic': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'broken': True, 'echo': True, 'node_info': True, 'nodes': True, 'services': True, 'topic_info': True, 'topics': True}, 'middleware': {'multiple': True, 'single': True}}
