# MaaDeps

Collection of build scripts to build MAA dependencies for popular platforms

## Usage

### Building All Dependencies

To build all dependencies at once:

```bash
python build.py --tarball --target <target-triplet>
```

Where `<target-triplet>` is your target platform (e.g., `x64-windows`, `x64-linux`, etc.)

### Building Individual Packages

To build a specific package:

```bash
python build-package.py --package <package-name> --target <target-triplet> --tarball
```

Available packages:
- `opencv` - OpenCV and OpenCV4 libraries
- `onnxruntime` - ONNX Runtime with DirectML support (Windows only)
- `directml` - DirectML library (Windows only, requires dynamic CRT)
- `fastdeploy` - FastDeploy library
- `boost` - Boost libraries (asio, core, dll, process, uuid)
- `misc` - Miscellaneous dependencies (zlib, cppzmq)

## GitHub Workflows

- `build.yml` - Builds all dependencies at once
- `buildwin.yml` - Builds all dependencies for Windows
- `build-packages.yml` - Builds individual packages separately

### Build Order

The `build-packages.yml` workflow ensures that packages are built in the correct order to handle dependencies. Specifically:

- DirectML is built before ONNX Runtime, since ONNX Runtime depends on DirectML
- Other packages are built in the order specified

## Suppressing CMake Warnings

To suppress CMake developer warnings, we've implemented several approaches:

1. Added `-Wno-dev` and `-DCMAKE_MESSAGE_LOG_LEVEL=WARNING` flags in triplet files
2. Added these flags to `vcpkg-configuration.json`
3. Provided environment variable scripts:
   - Windows: `set-cmake-flags.bat`
   - Unix: `set-cmake-flags.sh`

You can run these scripts before building to suppress warnings.

## Best Practices

- [MaaAssistantArknights](https://github.com/MaaAssistantArknights/MaaAssistantArknights)
  《明日方舟》小助手，全日常一键长草！| A one-click tool for the daily tasks of Arknights, supporting all clients.

- [MaaFramework](https://github.com/MaaXYZ/MaaFramework)
  基于图像识别的自动化黑盒测试框架 | A automation black-box testing framework based on image recognition
