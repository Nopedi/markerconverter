import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
import random
import time

class QRCodePublisher(Node):

    def __init__(self):
        super().__init__('qr_code_publisher')
        self.publisher_ = self.create_publisher(PoseStamped, 'aruco_marker_pose', 10)
        timer_period = 2  # Sekunden
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = PoseStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'camera_frame'
        msg.pose.position.x = round(random.uniform(-10, 10), 2)
        msg.pose.position.y = round(random.uniform(-10, 10), 2)
        msg.pose.position.z = round(random.uniform(-10, 10), 2)
        msg.pose.orientation.x = 0.0
        msg.pose.orientation.y = 0.0
        msg.pose.orientation.z = 0.0
        msg.pose.orientation.w = 1.0

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg}')

def main(args=None):
    rclpy.init(args=args)
    qr_code_publisher = QRCodePublisher()
    rclpy.spin(qr_code_publisher)

    qr_code_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
