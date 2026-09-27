# mission_3 Submission

- Name: (not provided)
- Section: (not provided)

## Explanations

### heading

The robot calculates the heading error between its current direction and the direction toward the next goal point. The PID uses that error to determine how much the robot should turn by adjusting the wheel speeds. Kp reacts to the current error, Ki corrects accumulated error, and Kd reduces overshooting and oscillation.

### integration

The PID depends on odometry to know where the robot is. If the wheel-radius estimate is wrong, the robot calculates the wrong distance traveled, so its estimated position becomes inaccurate. The controller can then make the correct correction based on bad position data, causing the actual robot to drift away from the planned path.