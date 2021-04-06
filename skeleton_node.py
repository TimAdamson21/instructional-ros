#!/usr/bin/env python

import rospy  # If you are doing ROS in python, then you will always need this import

# Message imports go here

# Service imports go here

# All other imports go here


# Hyper-parameters go here
SLEEP_RATE = 10


class NodeObject(object):
    """
    Note: In the init function, I will first give a description of each part, and then I will give an example

    """

    def __init__(self):
        # Everything besides pubs, subs, services, and service proxies go here
        pass

        # Publishers go here

        # Service Proxies go here

        # Subscribers go here

        # Services go here



def main():
    rospy.init_node("node_name")

    node_name = NodeObject()

    rate = rospy.Rate(SLEEP_RATE)

    # This while loop is what keeps the node from dieing
    while not rospy.is_shutdown():
        # If I wanted my node to constantly publish something, I would put the publishing here
        rate.sleep()


if __name__ == '__main__':
    main()
