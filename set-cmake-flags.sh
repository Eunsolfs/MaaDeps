#!/bin/bash
# 设置 VCPKG_CMAKE_ARGS 环境变量，用于抑制 CMake 开发者警告
export VCPKG_CMAKE_ARGS="-Wno-dev -DCMAKE_MESSAGE_LOG_LEVEL=WARNING"

echo "VCPKG_CMAKE_ARGS 环境变量已设置为: $VCPKG_CMAKE_ARGS"
