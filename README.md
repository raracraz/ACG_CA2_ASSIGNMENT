# Introduction
This repository contains the codebase for the ACG_CA2_ASSIGNMENT project. The main component of this project is a server that monitors a specific directory for changes and handles incoming requests.

## Structure
"""
- server/server.py: This is the main server script that watches the /home/camera1/Public/Footage/ directory for changes and manages the server's operations.
- camera#/client.py: This is the camera script that gets the images and sends the images to the server for secure storage via sFTP.
"""

## Issues:
"""
- server.py: Can only watch a single directory for changes, change to watch multiple directories in the Watcher function.
"""
