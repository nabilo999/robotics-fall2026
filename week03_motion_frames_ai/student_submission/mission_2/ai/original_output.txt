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