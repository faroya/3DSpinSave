import open3d as o3d
import numpy as np
import cv2
import os

wildtype_image_path = "images/Wildtype63D.ply"
mesh = o3d.io.read_triangle_mesh(wildtype_image_path)
mesh.compute_vertex_normals()


# we can display the image as a point cloud
# pcd_WildType = mesh.sample_points_uniformly(number_of_points=500)
# o3d.visualization.draw_geometries([pcd_WildType])


# Define parameters for frame saving
output_frames_folder = "output_frames"
os.makedirs(output_frames_folder, exist_ok=True)
num_frames = 10  # Number of frames
rotation_degrees_per_frame = 360 / num_frames  # Rotate 360 degrees over the frames

# Initialize Open3D visualizer
vis = o3d.visualization.Visualizer()
vis.create_window()

# Save the frames as images
for frame_idx in range(num_frames):
    # Clear the visualizer and add the mesh at the current rotation
    vis.clear_geometries()
    mesh.rotate(mesh.get_rotation_matrix_from_xyz((0, np.radians(rotation_degrees_per_frame * frame_idx), 0)))
    vis.add_geometry(mesh)

    # Capture the current visualization as an image
    vis.poll_events()
    vis.update_renderer()
    color_image = vis.capture_screen_float_buffer()

    # Convert the Open3D image to an OpenCV-compatible format
    color_image_cv = np.array(color_image)
    color_image_cv = cv2.cvtColor((color_image_cv * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)  # OpenCV uses BGR format

    # Save the frame as an image
    frame_filename = os.path.join(output_frames_folder, f"frame_{frame_idx:03d}.png")
    cv2.imwrite(frame_filename, color_image_cv)

# Release the visualizer
vis.destroy_window()
