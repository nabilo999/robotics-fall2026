# Mission 2

## Snapshot

{'source': 'reference', 'captured_at': '2026-09-22T03:16:46.922306+00:00', 'description': 'Instructor-defined frame geometry. No live ROS transforms were measured.', 'frames': ['odom', 'base_link', 'base_scan', 'rear_camera_link', 'hall_camera'], 'transforms': {'base_scan_to_base_link': {'translation': {'x': 0.2, 'y': 0.0, 'z': 0.14}, 'yaw': 0.0}, 'rear_camera_to_base_link': {'translation': {'x': -0.18, 'y': 0.0, 'z': 0.22}, 'yaw': 3.141592653589793}, 'hall_camera_to_base_link': {'translation': {'x': -1.5, 'y': 0.5, 'z': 1.2}, 'yaw': -1.5707963267948966}}}

## Frame Context

The rear-camera transform stays fixed because the rear camera is physically mounted on the robot. Its position and orientation relative to base_link do not change as the robot moves
The hallway-camera-to-base_link transform changes because the hallway camera is fixed in the environment while the robot moves. Therefore, the robot's position changes relative to that camera over time.

## Initial Prompt

Write ROS 2 Python code that converts a point detected by the hallway camera into the robot's base_link frame.


## Initial Output

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped
import tf2_ros
from tf2_geometry_msgs import do_transform_point


class CameraToBaseLink(Node):
    def __init__(self):
        super().__init__('camera_to_base_link')

        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(
            self.tf_buffer, self
        )

        self.subscription = self.create_subscription(
            PointStamped,
            '/camera/point',
            self.point_callback,
            10
        )

    def point_callback(self, point_msg):
        try:
            # Transform the point from the hallway camera frame
            # into the robot's base_link frame.
            transform = self.tf_buffer.lookup_transform(
                'base_link',
                point_msg.header.frame_id,
                rclpy.time.Time()
            )

            transformed_point = do_transform_point(
                point_msg,
                transform
            )

            self.get_logger().info(
                f'Point in base_link: '
                f'x={transformed_point.point.x:.3f}, '
                f'y={transformed_point.point.y:.3f}, '
                f'z={transformed_point.point.z:.3f}'
            )

        except Exception as e:
            self.get_logger().warn(
                f'Could not transform point: {e}'
            )


def main(args=None):
    rclpy.init(args=args)

    node = CameraToBaseLink()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

## Initial Source

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped
import tf2_ros
from tf2_geometry_msgs import do_transform_point


class CameraToBaseLink(Node):
    def __init__(self):
        super().__init__('camera_to_base_link')

        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(
            self.tf_buffer, self
        )

        self.subscription = self.create_subscription(
            PointStamped,
            '/camera/point',
            self.point_callback,
            10
        )

    def point_callback(self, point_msg):
        try:
            # Transform the point from the hallway camera frame
            # into the robot's base_link frame.
            transform = self.tf_buffer.lookup_transform(
                'base_link',
                point_msg.header.frame_id,
                rclpy.time.Time()
            )

            transformed_point = do_transform_point(
                point_msg,
                transform
            )

            self.get_logger().info(
                f'Point in base_link: '
                f'x={transformed_point.point.x:.3f}, '
                f'y={transformed_point.point.y:.3f}, '
                f'z={transformed_point.point.z:.3f}'
            )

        except Exception as e:
            self.get_logger().warn(
                f'Could not transform point: {e}'
            )


def main(args=None):
    rclpy.init(args=args)

    node = CameraToBaseLink()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

## Initial Analysis

It assumes point_msg.header.frame_id correctly identifies the hallway camera frame.  
It uses rclpy.time.Time() to request the latest available transform rather than explicitly using the point's timestamp. This could be wrong if the robot is moving.  

## Improved Changes

The improved prompt explicitly requires hall_camera → base_link, it uses the point’s original timestamp, relies on the TF buffer instead of hard-coded offsets, and returns None if the transform is unavailable rather than failing or moving the robot.

## Live Pending

True

## Synthesis

The original AI response assumed a generic input frame and created its own ROS node, subscriptions, and TF buffer. It also requested the latest transform rather than using the observation timestamp, which can produce an incorrect robot-relative point while the robot is moving. The revised function accepts only hall_camera, asks the supplied TF buffer to transform the stamped point to base_link, and returns None when TF is unavailable The rotated-coordinate test detects whether the frame rotation is applied correctly, while the unavailable-transform test verifies the safe fallback. When transform data is unavailable, the robot should avoid acting on that observation and wait for valid data.

## Live Issue

the error was not sent
