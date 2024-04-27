# aruco-marker-distance-measurement
This is a GitHub repository that contains code for measuring the distance between a camera and an Aruco marker using computer vision techniques. The repository implements algorithms to detect and decode the marker and then estimate its position in 3D space, using OpenCV.

## Project Demo
https://github.com/debjotyms/aruco-marker-distance-measurement/assets/96808014/82ffdbb3-ab71-42cd-bb19-5555d3990d4f

## Project Overview

The project is aimed at measuring distances using a marker known as "7x7_100.png" and a custom checkerboard pattern for calibration. The main functionality involves capturing images or video frames, detecting the marker, estimating its pose, and calculating the distance from the camera to the marker.

![check](https://github.com/debjotyms/aruco-marker-distance-measurement/assets/96808014/bbc5661f-91de-4579-8181-5ea156fd4c8f)

## Files

1. **calib.pkl**: This file stores the calibration parameters obtained from the calibration process, including the camera matrix, distortion coefficients, rotation vectors, and translation vectors.

2. **calib.py**: This Python script is used for camera calibration. It reads a series of images of a custom checkerboard pattern, detects the corners, and calibrates the camera using OpenCV's `calibrateCamera` function. The calibration results are saved in the "calib.pkl" file.

3. **main.py**: This script is the main application for distance measurement. It loads the calibration parameters from "calib.pkl", initializes the camera, detects the marker using ArUco markers from OpenCV, estimates its pose, and calculates the distance from the camera to the marker.

4. **20 jpg files**: These are images of the custom checkerboard pattern used for camera calibration.

## Instructions

1. **Calibration**: Before using the distance measurement functionality, it's necessary to calibrate the camera using the provided checkerboard images. Run `calib.py` to perform camera calibration. Ensure that the images of the checkerboard are located in a directory named "img".

2. **Distance Measurement**: After successful calibration, run `main.py` to measure distances using the custom marker. The script will initialize the camera and continuously display the video feed with detected markers and calculated distances.

3. **Marker**: The project uses a specific marker image named "7x7_100.png". Ensure this marker is visible to the camera during distance measurement.

## Dependencies

- Python 3.10
- OpenCV (cv2)
- NumPy

## Usage

To run the project:

1. Clone the repository to your local machine.
2. Follow the instructions for calibration and distance measurement as outlined above.

## License

This project is licensed under the [MIT License](LICENSE).
