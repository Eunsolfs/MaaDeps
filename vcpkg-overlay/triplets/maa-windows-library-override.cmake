set(VCPKG_LIBRARY_LINKAGE static)

if(PORT STREQUAL "opencv4")
  set(VCPKG_LIBRARY_LINKAGE static)
  set(VCPKG_CMAKE_CONFIGURE_OPTIONS ${VCPKG_CMAKE_CONFIGURE_OPTIONS} -DENABLE_LTO=ON)
endif()

if(PORT STREQUAL "maa-onnxruntime")
    set(VCPKG_LIBRARY_LINKAGE static)
endif()

if(PORT STREQUAL "directml-bin")
    # DirectML 只支持动态库链接
    set(VCPKG_LIBRARY_LINKAGE dynamic)
    set(VCPKG_CRT_LINKAGE dynamic)
endif()

if(PORT STREQUAL "maa-fastdeploy")
  set(VCPKG_LIBRARY_LINKAGE static)
endif()

# 移除自定义 DLL 后缀
# set(VCPKG_CMAKE_CONFIGURE_OPTIONS ${VCPKG_CMAKE_CONFIGURE_OPTIONS} -DCMAKE_SHARED_LIBRARY_SUFFIX_CXX=_maa.dll)

if (PORT STREQUAL "opencv")
  set(VCPKG_LIBRARY_LINKAGE static)
  list(APPEND VCPKG_CMAKE_CONFIGURE_OPTIONS -DBUILD_opencv_hdf=OFF -DBUILD_opencv_quality=OFF)
endif ()
