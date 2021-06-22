# Bittle : ROS package

## Introduction

My work is a way to learn ros.

I used urdf files and CAO file from : https://github.com/AIWintermuteAI/Bittle_URDF

Thanks to @AIWintermuteAI for his work !

## Presentation

This is a ROS package that you can use to develop many algoritmh to control Bittle in a Gazebo simulation.

You can found a python file ``joint_publisher.py`` in the src folder. 

This program send a position to the simulation for the specified joint. See details in the file.

You can control all the motor of bittle trough the name of these joints listed here :


- left_back_knee_joint
- left_back_shoulder_joint
- left_front_knee_joint
- left_front_shoulder_joint
- right_back_knee_joint
- right_back_shoulder_joint
- right_front_knee_joint
- right_front_shoulder_joint
- joint_state_controller

## Install
You need this package :

https://bitbucket.org/theconstructcore/spawn_robot_tools/src/master/

move `spawn_robot_tools_pkg` in the src folder of catkin folder.

Then; run 
```sh
rosdep install spawn_robot_tools_pkg
```

then move this repository in your ``catkin_ws/src`` folder.

Then : run
```sh
rosdep install bittle_ros_gazebo
```

and use catkin_make in ``catkin_ws``

## Launch

First source your devel/setup

To launch the gazebo simulation you need to run this command in the ``src/launch``:
```sh
roslaunch display.launch
```

And in antoher tab you can run a python program to control the robot.


## Informations

Tested on Ubuntu 20.04 with ROS Noetic.
