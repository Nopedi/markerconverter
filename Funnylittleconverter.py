import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class QRCodeListener(Node):

    def __init__(self):
        super().__init__('qr_code_listener')
        self.subscription = self.create_subscription(
            PoseStamped,
            'aruco_marker_pose',  # Topic, das die ArUco-Marker-Daten published
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(PoseStamped, 'transformed_aruco_marker_pose', 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        print("KOmmt bis hier")
        self.get_logger().info(f'Received message: {msg}')

        # Transformation anwenden
        transformed_pose = self.transform_pose(msg)

        # Veröffentlichung der transformierten Nachricht
        self.publisher_.publish(transformed_pose)
        self.get_logger().info(f'Transformed message published: {transformed_pose}')

    def transform_pose(self, pose):
        # Beispiel: Einfache Translation (Verschiebung)
        dx = 1.0  # Beispielwert für Verschiebung in x-Richtung
        dy = 2.0  # Beispielwert für Verschiebung in y-Richtung
        dz = 3.0  # Beispielwert für Verschiebung in z-Richtung

        transformed_pose = PoseStamped()
        transformed_pose.header = pose.header
        transformed_pose.pose.position.x = pose.pose.position.x + dx
        transformed_pose.pose.position.y = pose.pose.position.y + dy
        transformed_pose.pose.position.z = pose.pose.position.z + dz
        transformed_pose.pose.orientation = pose.pose.orientation  # Unverändert übernommen

        return transformed_pose

def main(args=None):
    rclpy.init(args=args)
    qr_code_listener = QRCodeListener()
    rclpy.spin(qr_code_listener)

    qr_code_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
