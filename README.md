# UGV Simulation

## Installation
Step 1. Download _src_  folder

Step 2. To create new workspace.
Open terminal and Enter.
 
```
    $ mkdir -p ugvsim_ws/src
    $ cd ~ugvsim_ws/src
    $ catkin_init_workspace
    $ cd ~/ugvsim_ws
    $ catkin_make 
```
Step 3. Adding Repo to created workspace
```
$ cd ~/ugvsim_ws/src/
$ catkin_create_pkg mybot_control
$ catkin_create_pkg mybot_description
$ catkin_create_pkg mybot_gazebo
```
Copy contents of respective folder from repository to these new folders.

## Launching simulation
```
$ source ~/ugvsim/devel/setup.sh
$ roslaunch mybot_gazebo mybot_world.launch
```
## Keyboard Controlling Robot

### Setup
```
$ cd ~/ugvsim/src
$ catkin_create_pkg key_teleop
```
Now copy contents of this folder form repo.

### To Run
```
$ source ~/ugvsim/devel/setup.sh
$ rosrun key_teleop key_teleop.py key_vel:=cmd_vel
```
if script is unexcecutable
```
$ sudo chmod u+x key_teleop.py
```

See [moorerobots.com](moorerobots.com) for tutorial
 
