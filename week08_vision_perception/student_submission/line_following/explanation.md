# line_following

## comparison
In the straight practice run, the robot followed the line fairly steadily. The mask picked out the line, and the centering error stayed small, so it didn’t need much steering correction. On the curved track, the original settings still reached the finish, but the robot drifted more around bends and sometimes wobbled. I increased the gain from 0.08 to 0.16 and left everything else unchanged. On the second track run, I noticed less drifting, and the recorded error was lower overall. The stronger steering corrections kept the line closer to the middle of the camera view. It also finished sooner because it spent less time slowing down to handle large errors.

## limits
My practice run eventually entered LINE_LOST and stopped before I ended the controller. That means the image processing no longer found a usable line region, so the controller stopped instead of continuing without guidance. The recording alone doesn’t establish exactly why the line was lost. For a real delivery robot, following a colored line would not be enough to move safely around people. It would also need obstacle and distance sensing, such as depth cameras or lidar, and testing with people crossing its path, changing lighting, blocked routes and sensor failures. Reaching the end of this simulated track doesn’t prove it could handle those situations safely.
