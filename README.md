# urdf_class_draizzat


At ros2 workspace, install required dependency: 

```
cd ~/ros2_class_ws/
rosdep install --from-paths src --ignore-src --rosdistro humble -y

```

Then compile the package:
```
colcon build
source ~/ros2_class_ws/install/setup.bash

```

Launch the file as below, depending on the file name of the urdf file: 

```
ros2 launch urdf_class_draizzat  display.launch.py model:=urdf/02-multipleshapes.urdf
ros2 launch urdf_class_draizzat  display.launch.py model:=urdf/07-physics.urdf 

ros2 launch urdf_class_draizzat  rviz.gazebo.launch.py model:=urdf/07-physics.urdf 

```

Filename available: 

01-myfirst.urdf  
02-multipleshapes.urdf  
03-origins.urdf  
04-materials.urdf  
05-visual.urdf  
06-flexible.urdf  
07-physics.urdf  
08-macroed.urdf.xacro