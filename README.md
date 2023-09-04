# 3DSpinSave

# 3D Mesh Visualization and Rotation

This repository contains a Python script that visualizes a 3D mesh, rotates it, and saves the resulting frames as images.

## Requirements

- Open3D
- NumPy
- OpenCV
- PIL
- IPython

## Installation

To install the required packages, run:

```bash
pip install open3d numpy opencv-python Pillow IPython


## Usage

1. Update the `wildtype_image_path` variable in the script to the path of your `.ply` file.

2. Run the script:


The script will visualize the 3D mesh, rotate it, and save the resulting frames as images in the `output_frames` folder.

## Details

The script uses the Open3D library to read a 3D mesh from a `.ply` file and visualize it. It then rotates the mesh and captures the frames of the rotation, saving them as images.

The script first reads the 3D mesh from the specified `.ply` file and computes its vertex normals. It then initializes the Open3D visualizer and sets up the parameters for the rotation and frame saving.

The script then enters a loop where it rotates the mesh by a small amount, adds it to the visualizer, captures the current visualization as an image, converts the image to an OpenCV-compatible format, and saves the image as a `.png` file in the `output_frames` folder.

The script rotates the mesh 360 degrees over the specified number of frames and saves each frame as an image.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update the tests as appropriate.

 
