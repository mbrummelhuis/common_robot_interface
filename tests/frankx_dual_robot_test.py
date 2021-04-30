# -*- coding: utf-8 -*-
"""Simple test script for AsyncRobot class using FrankxController.
"""

import time

import numpy as np

from cri.robot import SyncRobot, AsyncRobot
from cri.controller import FrankxController

np.set_printoptions(precision=2, suppress=True)


def main():
    base_frame = (0, 0, 0, 0, 0, 0)
    work_frame = (400, 0, 300, 180, 0, 180)   # base frame: x->front, y->right, z->up

    with AsyncRobot(SyncRobot(FrankxController(ip='172.16.0.2'))) as robot_1, \
        AsyncRobot(SyncRobot(FrankxController(ip='172.16.1.2'))) as robot_2:

        robots = [robot_1, robot_2]

        # Set robot axes and TCP
        for i, robot in enumerate(robots):
            robot.axes = 'sxyz'     # static/extrinsic frame xyz convention
            robot.tcp = (0, 0, 89.1, 0, 0, -135)    # standard TacTip offset

            # Display robot info
            print("Robot {} info: {}".format(i + 1, robot.info))

        # Initialize joint angles
        print("Initializing joint angles ...")
        for robot in robots:
            robot.move_joints((0, -35, 0, -150, 0, 115, -45))

        # Move to origin of work frame
        print("Moving to origin of work frame ...")
        for robot in robots:
            robot.coord_frame = work_frame
            robot.move_linear((0, 0, 0, 0, 0, 0))

        # Increase and decrease all joint angles
        print("Increasing and decreasing all joint angles ...")
        for robot in robots:
            robot.move_joints(robot.joint_angles + (5,)*7)
            robot.move_joints(robot.joint_angles - (5,)*7)

        # Move backward and forward
        print("Moving backward and forward ...")
        for robot in robots:
            robot.move_linear((20, 0, 0, 0, 0, 0))
            robot.move_linear((0, 0, 0, 0, 0, 0))

        # Move right and left
        print("Moving right and left ...")
        for robot in robots:
            robot.move_linear((0, 20, 0, 0, 0, 0))
            robot.move_linear((0, 0, 0, 0, 0, 0))

        # Move down and up
        print("Moving down and up ...")
        for robot in robots:
            robot.move_linear((0, 0, 20, 0, 0, 0))
            robot.move_linear((0, 0, 0, 0, 0, 0))

        # Roll right and left
        print("Rolling right and left ...")
        for robot in robots:
            robot.move_linear((0, 0, 0, 20, 0, 0))
            robot.move_linear((0, 0, 0, 0, 0, 0))

        # Roll forward and backward
        print("Rolling forward and backward ...")
        for robot in robots:
            robot.move_linear((0, 0, 0, 0, 20, 0))
            robot.move_linear((0, 0, 0, 0, 0, 0))

        # Turn clockwise and anticlockwise around work frame z-axis
        print("Turning clockwise and anticlockwise around work frame z-axis ...")
        for robot in robots:
            robot.move_linear((0, 0, 0, 0, 0, 20))
            robot.move_linear((0, 0, 0, 0, 0, 0))

        print("Moving to offset pose and making tap move up and down ...")
        for robot in robots:
            robot.move_linear((20, 20, 20, 20, 20, 20))
            robot.coord_frame = base_frame
            robot.coord_frame = robot.target_pose
            robot.move_linear((0, 0, 20, 0, 0, 0))
            robot.move_linear((0, 0, 0, 0, 0, 0))

        print("Moving to origin of work frame ...")
        for robot in robots:
            robot.coord_frame = work_frame
            robot.move_linear((0, 0, 0, 0, 0, 0))

        # Pause before commencing asynchronous tests
        print("Waiting for 5 secs ...")
        time.sleep(5)
        print("Repeating test sequence for asynchronous moves ...")

        # Increase and decrease all joint angles (async)
        print("Increasing and decreasing all joint angles ...")
        for robot in robots:
            robot.async_move_joints(robot.joint_angles + (5,)*7)
        for robot in robots:
            robot.async_result()
        for robot in robots:
            robot.async_move_joints(robot.joint_angles - (5,)*7)
        for robot in robots:
            robot.async_result()

        # Move backward and forward (async)
        print("Moving backward and forward (async) ...")
        for robot in robots:
            robot.async_move_linear((20, 0, 0, 0, 0, 0))
        for robot in robots:
            robot.async_result()
        for robot in robots:
            robot.async_move_linear((0, 0, 0, 0, 0, 0))
        for robot in robots:
            robot.async_result()

        # Move right and left
        print("Moving right and left (async) ...")
        for robot in robots:
            robot.async_move_linear((0, 20, 0, 0, 0, 0))
        for robot in robots:
            robot.async_result()
        for robot in robots:
            robot.async_move_linear((0, 0, 0, 0, 0, 0))
        for robot in robots:
            robot.async_result()

        # Move down and up (async)
        print("Moving down and up (async) ...")
        for robot in robots:
            robot.async_move_linear((0, 0, 20, 0, 0, 0))
        for robot in robots:
            robot.async_result()
        for robot in robots:
            robot.async_move_linear((0, 0, 0, 0, 0, 0))
        for robot in robots:
            robot.async_result()

        # Roll right and left (async)
        print("Rolling right and left (async) ...")
        for robot in robots:
            robot.async_move_linear((0, 0, 0, 20, 0, 0))
        for robot in robots:
            robot.async_result()
        for robot in robots:
            robot.async_move_linear((0, 0, 0, 0, 0, 0))
        for robot in robots:
            robot.async_result()

        # Roll forward and backward (async)
        print("Rolling forward and backward (async) ...")
        for robot in robots:
            robot.async_move_linear((0, 0, 0, 0, 20, 0))
        for robot in robots:
            robot.async_result()
        for robot in robots:
            robot.async_move_linear((0, 0, 0, 0, 0, 0))
        for robot in robots:
            robot.async_result()

        # Turn clockwise and anticlockwise around work frame z-axis (async)
        print("Turning clockwise and anticlockwise around work frame z-axis (async) ...")
        for robot in robots:
            robot.async_move_linear((0, 0, 0, 0, 0, 20))
        for robot in robots:
            robot.async_result()
        for robot in robots:
            robot.async_move_linear((0, 0, 0, 0, 0, 0))
        for robot in robots:
            robot.async_result()

        # Move to offset pose then tap down and up in sensor frame (async)
        print("Moving to offset pose and making tap move up and down (async) ...")
        for robot in robots:
            robot.async_move_linear((20, 20, 20, 20, 20, 20))
        for robot in robots:
            robot.async_result()
        for robot in robots:
            robot.coord_frame = base_frame
            robot.coord_frame = robot.target_pose
            robot.async_move_linear((0, 0, 20, 0, 0, 0))
        for robot in robots:
            robot.async_result()
        for robot in robots:
            robot.async_move_linear((0, 0, 0, 0, 0, 0))
        for robot in robots:
            robot.async_result()

        print("Moving to origin of work frame ...")
        for robot in robots:
            robot.coord_frame = work_frame
            robot.async_move_linear((0, 0, 0, 0, 0, 0))
        for robot in robots:
            robot.async_result()


if __name__ == '__main__':
    main()