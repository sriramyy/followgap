import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SenderNode(Node):

    def __init__(self):
        super().__init__('sender_node')
        # This creates a publisher on the topic 'opponent_data'
        self.publisher_ = self.create_publisher(String, 'opponent_data', 10)
        
        # We'll publish a message every 1 second
        timer_period = 1.0  
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Data from opponent car! Count: {self.i}'
        
        # Publish the message
        self.publisher_.publish(msg)
        
        # Log to the console
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    sender_node = SenderNode()
    rclpy.spin(sender_node)
    
    sender_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()