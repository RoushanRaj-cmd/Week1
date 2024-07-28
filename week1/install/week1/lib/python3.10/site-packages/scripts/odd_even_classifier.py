#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class OddEvenClassifier(Node):
    def __init__(self):
        super().__init__('odd_even_classifier')
        self.subscription = self.create_subscription(
            Int32,
            '/integers',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(String, '/oddeven', 10)
    
    def listener_callback(self, msg):
        result = "Odd" if msg.data % 2 else "Even"
        self.get_logger().info(f"Received number: {msg.data} is {result}")
        result_msg = String()
        result_msg.data = result
        self.publisher_.publish(result_msg)

def main(args=None):
    rclpy.init(args=args)
    odd_even_classifier = OddEvenClassifier()
    rclpy.spin(odd_even_classifier)
    odd_even_classifier.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
