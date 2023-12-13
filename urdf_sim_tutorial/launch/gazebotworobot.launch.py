from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # These are the arguments you can pass to this launch file, for example paused:=true
    gui_arg = DeclareLaunchArgument(name='gui', default_value='true')
    package_arg = DeclareLaunchArgument('urdf_package',
                                        description='The package where the robot description is located',
                                        default_value='urdf_class_draizzat')
    model_arg = DeclareLaunchArgument('urdf_package_path',
                                      description='The path to the robot description relative to the package root',
                                      default_value='urdf/08-macroed.urdf.xacro')

    empty_world_launch = IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('gazebo_ros'), 'launch', 'gazebo.launch.py']),
        launch_arguments={'gui': LaunchConfiguration('gui'), 'pause': 'true'}.items(),
    )

    description_launch_py = IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('urdf_launch'), 'launch', 'description.launch.py']),
        launch_arguments={'urdf_package': LaunchConfiguration('urdf_package'),
                          'urdf_package_path': LaunchConfiguration('urdf_package_path')}.items()
    )

    # Push robot_description to factory and spawn robots in Gazebo
    urdf_spawner_node1 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='urdf_spawner1',
        arguments=['-topic', '/robot_description', '-entity', 'robot1', '-z', '0.5', '-unpause'],
        output='screen',
    )

    urdf_spawner_node2 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='urdf_spawner2',
        arguments=['-topic', '/robot_description', '-entity', 'robot2', '-x', '2.0', '-y', '0.0', '-z', '0.5', '-unpause'],
        output='screen',
    )

    return LaunchDescription([
        gui_arg,
        package_arg,
        model_arg,
        empty_world_launch,
        description_launch_py,
        urdf_spawner_node1,
        urdf_spawner_node2,
    ])
