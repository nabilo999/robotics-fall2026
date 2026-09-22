# Mission 3

## Specification

I will drive forward 0.40 m, stop, rotate left 90°, stop, then drive forward another 0.40 m and stop. I will use 0.20 m/s for driving and 0.50 rad/s for turning. Success means ending near (0.40, 0.40) m with a heading of 1.57 rad (90°).

## Saved Specification

I will drive forward 0.40 m, stop, rotate left 90°, stop, then drive forward another 0.40 m and stop. I will use 0.20 m/s for driving and 0.50 rad/s for turning. Success means ending near (0.40, 0.40) m with a heading of 1.57 rad (90°).

## Assigned Pattern

l_path

## Original Prompt

This is a ROS 2 Jazzy Python package. Implement only build_pattern(pattern_name: str) -> list[Segment] for 'l_path' in the existing pattern.py.
The course-provided pattern_node.py calls this function, publishes the returned segments repeatedly through /student_cmd_vel, and sends the final zero command.
Use the existing Segment class with linear_x (m/s), angular_z (rad/s), and duration (s).
Return the ordered segments for the assigned specification and raise ValueError for an unknown pattern name.
Stay within 0.22 m/s, 0.80 rad/s, 30 seconds per segment, and 60 seconds total.
Do not replace the wrapper or course checks. Explain assumptions and propose tests.
My specification:
I will drive forward 0.40 m, stop, rotate left 90°, stop, then drive forward another 0.40 m and stop. I will use 0.20 m/s for driving and 0.50 rad/s for turning. Success means ending near (0.40, 0.40) m with a heading of 1.57 rad (90°).

## Original Output

def build_pattern(pattern_name: str) -> list[Segment]:
    if pattern_name != "l_path":
        raise ValueError(f"Unknown pattern: {pattern_name}")

    return [
        Segment(linear_x=0.20, angular_z=0.0, duration=2.0),
        Segment(linear_x=0.0, angular_z=0.50, duration=1.57 / 0.50),
        Segment(linear_x=0.20, angular_z=0.0, duration=2.0),
    ]

## Original Source

def build_pattern(pattern_name: str) -> list[Segment]:
    if pattern_name != "l_path":
        raise ValueError(f"Unknown pattern: {pattern_name}")

    return [
        Segment(linear_x=0.20, angular_z=0.0, duration=2.0),
        Segment(linear_x=0.0, angular_z=0.50, duration=1.57 / 0.50),
        Segment(linear_x=0.20, angular_z=0.0, duration=2.0),
    ]

## Assumptions

The AI assumes positive linear_x moves forward, positive angular_z turns left, speeds are in m/s and rad/s, and duration is in seconds.  

## Problems

I checked that all speeds stay within the limits and that it is using function correctly

## Test Plan

Pattern behavior test: Verify: forward → left turn → forward. Expected: (0.40, 0.40) and heading = 1.57 rad. 
Velocity-limit test: Check |linear_x| ≤ 0.22 and |angular_z| ≤ 0.80. 
Stop test: Verify the wrapper sends zero velocity after the final segment. Expected: linear_x = 0 and angular_z = 0.

## Modifications

I replaced only the NotImplementedError in build_pattern and kept the existing Segment class.

## Live Pending

True

## Evidence Analysis

The 9 passing tests confirm the L-path has valid Segment objects, bounded speeds, positive durations, two 0.40 m forward moves, a left 90° turn. The endpoint is also near (0.40, 0.40) with a 90° heading. 

## Ai Disclosure

I used chatgpt to draft the first output then then the refined one

## Live Issue

no error was given
