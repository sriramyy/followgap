import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ReceiverNode(Node):

    def __init__(self):
        super().__init__('receiver_node')
        
        # This subscribes to the sender's topic, which is in the 'car_A' namespace
        # The leading '/' is important - it makes this an absolute topic path.
        self.subscription = self.create_subscription(
            String,
            '/car_A/opponent_data',  # <-- This must match the sender's namespaced topic
            self.listener_callback,
            10)
        self.get_logger().info('Receiver node is running and listening for opponent...')

    def listener_callback(self, msg):
        # This function is called every time a message is received
        self.get_logger().info(f'I HEARD: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    receiver_node = ReceiverNode()
    rclpy.spin(receiver_node)
    
    receiver_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()