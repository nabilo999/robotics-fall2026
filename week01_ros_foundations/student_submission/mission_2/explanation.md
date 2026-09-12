# Mission 2

## Measurement Explanation

In the Curve trial, the estimated traveled path measures the distance the robot actually traveled along its curved route, while the start-to-end distance measures the straight-line distance between its starting and ending positions. that is why the straight-line distance is shorter than the curved path.  

## Modified Settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}

## Motion Comparison

I predicted that the robot would rotate in place because its forward speed was 0 m/s and its turning speed was 0.5 rad/s. The measured direction change was 55.4°, while the estimated traveled path was 0 m, which shows that the robot turned without moving forward.

## Prediction Locks

{'curve': '2026-09-10T17:36:10.406521+00:00', 'curve_modified': '2026-09-10T17:43:33.413193+00:00', 'rotation': '2026-09-10T17:31:15.966658+00:00', 'straight': '2026-09-10T17:17:52.726529+00:00'}

## Predictions

{'curve': 'I predict a n eartic movement because its always changing direction and moving forward', 'curve_modified': 'This curve should be wide because a bigger radius means a wider turn', 'rotation': 'I predict its position will stay the same while its direction will keep spinning', 'straight': 'I predict the robot will move straight forward without turning.'}

## Safety Explanation

The command guard checks every proposed driving command and prevents invalid or overly large speeds from reaching the robot.  
The final zero command stops the robot at the end of the trial by setting the forward speed and turning speed to zero.  
The timeout is needed if the program crashes or stops communicating while the robot is moving. It automatically sends a stop command after 0.5 seconds without receiving a new command.  
