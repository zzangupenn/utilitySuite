import numpy as np
class open3dUtils:
    """
    Utility class for working with Open3D geometries and visualizations.

    Features:
    - Creates a camera frustum visualization from an extrinsic matrix.
    - Maintains a list of Open3D geometry objects to be visualized together.
    - Provides a simple interface to add, clear, and display objects in a visualizer.
    - Supports customizable camera frustum size, color, aspect ratio, transparency, and linewidth.
    - Optionally shows coordinate axes in the visualizer.

    Attributes:
    -----------
    object_list : list
        List of Open3D geometry objects to visualize.
    show_axis : bool
        Whether to show the coordinate frame axes in the viewer.

    Methods:
    --------
    create_camera_poses(extrinsic, size=1, color=[1,0,0], aspect_ratio=0.3, alpha=0.15, linewidths=0.1)
        Creates an Open3D LineSet representing a camera frustum from the extrinsic matrix.

    add_object(object)
        Adds an Open3D geometry object to the visualization list.

    clear_object()
        Clears all objects from the visualization list.

    show(background_color=np.asarray([0.0, 0.0, 0.0]))
        Opens an Open3D visualizer window and renders all added geometries.
    """
    def __init__(self):
        from scipy.spatial.transform import Rotation
        import open3d as o3d
        self.Rotation = Rotation
        self.o3d = o3d
        self.object_list = []
        self.show_axis = True

    def create_camera_poses(self, extrinsic, size=1, color=[1, 0, 0], aspect_ratio=0.3, alpha=0.15, linewidths=0.1):
        focal_len_scaled = size
        vertex_std = np.array([[0, 0, 0, 1],
                                [focal_len_scaled * aspect_ratio, -focal_len_scaled * aspect_ratio, focal_len_scaled, 1],
                                [focal_len_scaled * aspect_ratio, focal_len_scaled * aspect_ratio, focal_len_scaled, 1],
                                [-focal_len_scaled * aspect_ratio, focal_len_scaled * aspect_ratio, focal_len_scaled, 1],
                                [-focal_len_scaled * aspect_ratio, -focal_len_scaled * aspect_ratio, focal_len_scaled, 1],
                                [0, focal_len_scaled * aspect_ratio, focal_len_scaled, 1],
                                [0, 0, focal_len_scaled, 1],])
        T = np.eye(4)
        T[:3, :3] = self.Rotation.from_euler('Y', [180], degrees=True).as_matrix()
        for ind in range(vertex_std.shape[0]):
            vertex_std[ind] = T @ vertex_std[ind]
        vertex_transformed = vertex_std @ extrinsic.T
        
        points = vertex_transformed[:, :3]
        lines = [[0, 1], [0, 2], [1, 2], [2, 3], [0, 3], [0, 4], [3, 4], [1, 4], [5, 6], [0, 6]]
        colors = [color for i in range(len(lines))]
        line_set = self.o3d.geometry.LineSet()
        line_set.points = self.o3d.utility.Vector3dVector(points)
        line_set.lines = self.o3d.utility.Vector2iVector(lines)
        line_set.colors = self.o3d.utility.Vector3dVector(colors)
        return line_set
    
    def add_object(self, object):
        self.object_list.append(object)
    
    def clear_object(self):
        self.object_list = []
        
    def show(self, background_color=np.asarray([0.0, 0.0, 0.0])):
        viewer = self.o3d.visualization.Visualizer()
        viewer.create_window()
        for geometry in self.object_list:
            viewer.add_geometry(geometry)
        opt = viewer.get_render_option()
        opt.show_coordinate_frame = self.show_axis
        opt.background_color = background_color
        viewer.run()
        viewer.destroy_window()
        del viewer
        del opt