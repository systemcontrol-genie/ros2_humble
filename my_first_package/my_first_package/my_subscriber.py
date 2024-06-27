import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose


class TurtlesimSurbscriber(Node):
    def __init__(self):
        super().__init__('turtlesim_subscriber')
        self.sub = self.create_subscription(Pose, 'turtle1/pose', self.callback, 10)
        self.sub 


    def callback(self, msg):
        print("x : ", msg.x, "y:", msg.y)

def main(arge = None):
    rp.init(args=arge)
    turtlesim_subscriber = TurtlesimSurbscriber()
    rp.spin(turtlesim_subscriber)

    turtlesim_subscriber.destroy_node()
    rp.shutdown()


if __name__ == "__maim__":
    main()