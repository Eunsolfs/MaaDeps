#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
import subprocess
from pathlib import Path

# 获取当前脚本所在目录
basedir = os.path.dirname(os.path.abspath(__file__))

def main():
    parser = argparse.ArgumentParser(description='Build a specific package for MaaDeps')
    parser.add_argument('--package', required=True, help='Package config file name (without .json extension)')
    parser.add_argument('--target', required=True, help='Target triplet (e.g., x64-windows)')
    parser.add_argument('--tarball', action='store_true', help='Create tarball')
    parser.add_argument('--cmake-args', default='', help='Additional CMake arguments')

    args = parser.parse_args()

    # 验证包配置文件存在
    package_config = os.path.join(basedir, 'package-configs', f'{args.package}.json')
    if not os.path.exists(package_config):
        print(f"Error: Package config file {package_config} not found")
        sys.exit(1)

    # 创建临时 vcpkg.json
    temp_vcpkg_json = os.path.join(basedir, 'vcpkg.json.bak')
    vcpkg_json = os.path.join(basedir, 'vcpkg.json')

    # 备份原始 vcpkg.json
    if os.path.exists(vcpkg_json):
        shutil.copy2(vcpkg_json, temp_vcpkg_json)

    try:
        # 复制包配置文件到 vcpkg.json
        shutil.copy2(package_config, vcpkg_json)

        # 构建命令
        cmd = [
            sys.executable,
            os.path.join(basedir, 'build.py'),
            '--target', args.target
        ]

        if args.tarball:
            cmd.append('--tarball')

        if args.cmake_args:
            cmd.extend(['--', args.cmake_args])

        # 执行构建
        print(f"Building package {args.package} for target {args.target}")
        subprocess.check_call(cmd)

        # 如果需要创建 tarball，重命名 tarball 目录以包含包名
        if args.tarball and os.path.exists(os.path.join(basedir, 'tarball')):
            package_tarball_dir = os.path.join(basedir, f'tarball-{args.package}')

            # 如果目标目录已存在，先删除
            if os.path.exists(package_tarball_dir):
                shutil.rmtree(package_tarball_dir)

            # 重命名 tarball 目录
            shutil.move(os.path.join(basedir, 'tarball'), package_tarball_dir)
            print(f"Created tarball in {package_tarball_dir}")

        print(f"Package {args.package} built successfully")

    finally:
        # 恢复原始 vcpkg.json
        if os.path.exists(temp_vcpkg_json):
            shutil.move(temp_vcpkg_json, vcpkg_json)

if __name__ == "__main__":
    main()
