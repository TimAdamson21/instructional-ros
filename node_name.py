#!/usr/bin/env python

import rospy  # If you are doing ROS in python, then you will always need this import

# Message imports go here
from std_msgs.msg import String

# Service imports go here
from std_srvs.srv import Trigger, TriggerRequest, TriggerResponse

# All other imports go here
import os
import sys

# Hyper-parameters go here
SLEEP_RATE = 10


class NodeObject(object):
    """
    Note: In the init function, I will first give a description of each part, and then I will give an example

    """
    def __init__(self):
        # Everything besides pubs, subs, services, and service proxies go here
        self.object_attribute = "bar"
        self.sound_dir_filepath = "/home/tda22/catkin_ws/src/shutter-photography/shutter_photography/funny_files/sounds/"

        # Publishers go here
        self.publisher_topic_name_pub = rospy.Publisher('/ros_package_name/publisher_topic_name', String, queue_size=10)
        self.take_picture_pub = rospy.Publisher('/shutter_photography/take_picture', String, queue_size=10)

        # Service Proxies go here
        self.service_proxy_topic_name_sp = rospy.ServiceProxy("/ros_package_name/service_proxy_topic_name", Trigger)
        self.sound_out_sp = rospy.ServiceProxy('/shutter_photography/sound_out_srv', Trigger)

        # Subscribers go here
        self.subscriber_topic_name_sub = rospy.Subscriber('/ros_package_name/subscriber_topic_name', String, self.subscriber_topic_name_cb, queue_size=10)
        self.sound_output_sub = rospy.Subscriber('/shutter_photography/sound_output', String, self.sound_output_cb, queue_size=10)

        # Services go here
        self.service_topic_name_srv = rospy.Service("/ros_package_name/service_topic_name", Trigger, self.service_topic_name_cb)
        self.sound_output_srv = rospy.Service('/shutter_photography/sound_output_srv', Trigger, self.sound_output_srv_cb)


    def subscriber_topic_name_cb(self, msg):
        # This is where you handle the message that you just got in.
        # If you want to publish, simply use one of the publishers that you created on the object, like this:
        self.publisher_topic_name_pub.publish("dummy_string")

    def sound_output_cb(self, msg):
        pass

    def service_topic_name_cb(self, request):
        # Because this is a service call back and not a message callback, it takes in a Request, and not a Message.
        # This callback must also return a Response. Returning a response could look like this:
        return TriggerResponse(True, "error_message_goes_here")

    def sound_output_srv_cb(self, request):
        pass


def main():
    rospy.init_node("node_name")

    node_name = NodeObject()

    rate = rospy.Rate(SLEEP_RATE)
    
    # This while loop is what keeps the node from dieing
    while not rospy.is_shutdown():
        # If I wanted my node to constantly publish something, I would put the publishing here
        node_name.publisher_topic_name_pub.publish("dummy_string")
        rate.sleep()


if __name__ == '__main__':
    main()
