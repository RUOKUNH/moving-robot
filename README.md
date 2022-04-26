# Introduction
An lesson project of SJTU-AU336, save for further reviewing

# How to use
create a new work space and replace the src file with this

# construct map in new environmen 
run commands one-by-one as follows
open your ros environment: 
```
roslaunch turtlebot3_gazebo turtlebot3_world_small_bringup.launch
```
start the slam node: 
```
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```
start the control node:
```
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
after finishing slam, clear files in src/turtlebot3/turtlebot3_navigation/maps and save new maps by running
```
rosrun map_server map_saver -f map
```

Here is an vedio example
![image](https://github.com/RUOKUNH/moving-robot/tree/main/vedio/slam 00_00_00-00_00_30.gif)
# do navigation in the map
open environment by: 
```
roslaunch turtlebot3_gazebo turtlebot3_world_small_bringup.launch 
```
start the navagation node: 
```
roslaunch turtlebot3_navigation turtlebot3_navigation.launch 
```
At beginning, the position in rviz and gazebo are different. We need to relocalize the moving robot first, by pressing the pose estimation button in rviz and choose a proper poition to put the robot.
After relocalization, do navigation nearby to recognize the local environment.
Then you can do navigation in any position of the map.

Here is an vedio example
![image](https://github.com/RUOKUNH/moving-robot/tree/main/vedio/final 00_00_00-00_00_30.gif)
