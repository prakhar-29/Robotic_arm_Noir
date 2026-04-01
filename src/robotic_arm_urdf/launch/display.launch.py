from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    # Declare the 'model' argument
    model_arg = DeclareLaunchArgument(
        'model',
        default_value='',
        description='Path to the URDF model file'
    )

    # Load robot description from URDF file
    urdf_file = os.path.join(
        get_package_share_directory('robotic_arm_urdf'),
        'urdf',
        'robotic_arm_urdf.urdf'
    )

    with open(urdf_file, 'r') as f:
        robot_description_content = f.read()

    robot_description = {'robot_description': robot_description_content}

    # joint_state_publisher_gui node
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
    )

    # robot_state_publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[robot_description]
    )

    # rviz2 node
    rviz_config_file = os.path.join(
        get_package_share_directory('robotic_arm_urdf'),
        'urdf.rviz'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        output='screen'
    )

    return LaunchDescription([
        model_arg,
        joint_state_publisher_gui_node,
        robot_state_publisher_node,
        rviz_node,
    ])
