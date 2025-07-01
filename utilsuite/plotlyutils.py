import numpy as np
class plotlyUtils:
    def __init__(self, renderer = None) -> None:
        import plotly.graph_objects as go
        import plotly.io as pio
        self.pio = pio
        self.go = go
        if renderer is not None:
            self.pio.renderers.default = renderer
        
    def _extrinsic2pyramid_mesh(self, extrinsic, color='r', focal_len_scaled=1, aspect_ratio=1.3, alpha=0.15, linewidths=0.1):
        vertex_std = np.array([[0, 0, 0, 1],
                                [focal_len_scaled * aspect_ratio, -focal_len_scaled * aspect_ratio, focal_len_scaled, 1],
                                [focal_len_scaled * aspect_ratio, focal_len_scaled * aspect_ratio, focal_len_scaled, 1],
                                [-focal_len_scaled * aspect_ratio, focal_len_scaled * aspect_ratio, focal_len_scaled, 1],
                                [-focal_len_scaled * aspect_ratio, -focal_len_scaled * aspect_ratio, focal_len_scaled, 1]])
        vertex_transformed = vertex_std @ extrinsic.T
        return vertex_transformed

    def _create_camera_pose(self, vertex, color=[1, 0, 0]):
        return self.go.Mesh3d(
            # 8 vertices of a cube
            x=vertex[:, 0],
            y=vertex[:, 1],
            z=vertex[:, 2],

            # i, j and k give the vertices of triangles
            i = [0, 0, 0, 0],
            j = [1, 2, 3, 4],
            k = [2, 3, 4, 1],
            showscale=True,
            opacity=0.5,
            facecolor=[list(color)] * 5
        )
        
    def create_point(self, xyz, color=[1, 0, 0]):
        return self.go.Scatter3d(
            x = xyz[0],
            y = xyz[1],
            z = xyz[2],
            opacity = 1,
            surfacecolor = color)

    def add_plot_data(self, data_list, data_in, color):
        for ind in range(len(data_in)):
            vertex = self._extrinsic2pyramid_mesh(data_in[ind], aspect_ratio=0.5)
            data_list.append(self._create_camera_pose(vertex, color=color))
        return data_list
    
    def plot3d_show(self, data_list, axis_limits):
        fig = self.go.Figure(data=data_list)
        fig.update_layout(
            margin=dict(l=20, r=20, t=20, b=20),
            scene = dict(
                xaxis = dict(nticks=4, range=[axis_limits[0], axis_limits[1]],),
                yaxis = dict(nticks=4, range=[axis_limits[2], axis_limits[3]],),
                zaxis = dict(nticks=4, range=[axis_limits[4], axis_limits[5]],),
                aspectmode='data'),
            width = 1350
            )
        fig.show()
