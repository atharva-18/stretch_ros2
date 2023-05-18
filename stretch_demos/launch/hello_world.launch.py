import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

DEBUG_DIRECTORY = os.environ.get("HELLO_FLEET_PATH", "/home/hello-robot/stretch_user")

def generate_launch_description():
    stretch_core_path = get_package_share_directory('stretch_core')

    imu_filter = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([str(stretch_core_path) + '/launch/imu_filter.launch.py'])
    )
    stretch_ekf = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([str(stretch_core_path) + '/launch/stretch_ekf.launch.py'])
    )
    rplidar = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([str(stretch_core_path) + '/launch/rplidar.launch.py'])
    )
    stretch_scan_matcher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([str(stretch_core_path) + '/launch/stretch_scan_matcher.launch.py'])
    )
    keyboard_teleop = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([str(stretch_core_path) + '/launch/keyboard_teleop.launch.py'])
    )

    return LaunchDescription([
        Node(
            package='stretch_demos',
            executable='hello_world',
            name='hello_world',
            parameters=[
                {"debug_directory": DEBUG_DIRECTORY}
            ]
        ),
        Node(
            package='stretch_funmap',
            executable='funmap',
            name='funmap',
            parameters=[
                {"debug_directory": DEBUG_DIRECTORY}
            ]
        ),
        imu_filter,
        stretch_ekf,
        rplidar,
        stretch_scan_matcher,
        keyboard_teleop
    ])