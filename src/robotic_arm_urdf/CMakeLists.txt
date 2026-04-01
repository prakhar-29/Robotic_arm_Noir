cmake_minimum_required(VERSION 3.8)
project(robotic_arm_urdf)

find_package(ament_cmake REQUIRED)

# Install directories
install(DIRECTORY
  config
  launch
  meshes
  urdf
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
