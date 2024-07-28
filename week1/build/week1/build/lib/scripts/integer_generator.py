#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class IntegerGenerator(Node):
    def __init__(self):
        super().__init__('integer_generator')
        self.publisher_ = self.create_publisher(Int32, '/integers', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  # 1 second timer

    def timer_callback(self):
        num = random.randint(1, 100)
        self.get_logger().info(f"Generated number: {num}")
        msg = Int32()
        msg.data = num
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    integer_generator = IntegerGenerator()
    rclpy.spin(integer_generator)
    integer_generator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
