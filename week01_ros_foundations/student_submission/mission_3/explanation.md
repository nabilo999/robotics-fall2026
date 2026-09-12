# Mission 3

## Data To Command

First, front_distance() checks each LiDAR reading and calculates its angle based on readings that are within the front viewing area, are finite, and are greater than zero. It then returns the closest valid reading.
Second, decide_velocity() uses that distance. If the distance is missing or is less than or equal to the stopping distance, it returns 0.0 which tells the robot to stop. If the path is clear, it returns the forward speed, limited to a safe maximum of 0.18 m/s.

## Missing Data Safety

The robot stops when there is no valid front measurement because missing sensor data should be treated as unsafe. If the robot treated missing data as a clear path, it could move forward and cause an accident.

## System Layers

The robot stops when there is no valid front measurement because missing sensor data should be treated as unsafe. If the robot treated missing data as a clear path, it could move forward and cause an accident.
