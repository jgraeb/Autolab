#!/usr/bin/env python
import rospy 
import os
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose2D

# name of output file; overwrite the flyTracks data everytime you run the code (assumes the file given by the filename exists)
filename = os.path.join( '.','dataFile.txt')
f = open(filename, 'r+')
f.truncate(0)

def callback(data):
	x = data.pose.position.x
	y = data.pose.position.y
	z = data.pose.position.z
	f.write('{0} {1} {2}\n'.format(x, y, z))
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/vrpn_client_node/RigidBody01/pose", PoseStamped, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
	print("Listener - Logging position data")
	listener()
