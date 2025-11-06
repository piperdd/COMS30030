'''
Department of Computer Science, University of Bristol
COMS30030: Image Processing and Computer Vision

3-D from Stereo: Lab Sheet 1
3-D simulator

Yuhang Ming yuhang.ming@bristol.ac.uk
Andrew Calway andrew@cs.bris.ac.uk
'''

import cv2
import open3d as o3d
import matplotlib.pyplot as plt
import numpy as np

'''
Interaction menu:
P  : Take a screen capture.
D  : Take a depth capture.

Official doc on visualisation interactions:
http://www.open3d.org/docs/latest/tutorial/Basic/visualization.html
'''

def transform_points(points, H):
    '''
    transform list of 3-D points using 4x4 coordinate transformation matrix H
    converts points to homogeneous coordinates prior to matrix multiplication
    
    input:
      points: Nx3 matrix with each row being a 3-D point
      H: 4x4 transformation matrix
    
    return:
      new_points: Nx3 matrix with each row being a 3-D point
    '''
    # compute pt_w = H * pt_c
    n,m = points.shape
    new_points = np.concatenate([points, np.ones((n,1))], axis=1)
    new_points = H.dot(new_points.transpose())
    new_points = new_points / new_points[3,:]
    new_points = new_points[:3,:].transpose()
    return new_points

# print("here", flush=True)
if __name__ == '__main__': 
    bDisplayAxis = True

    ####################################
    #### Setup objects in the scene ####
    ####################################

    # create plane to hold all spheres
    h, w = 24, 12
    # place the support plane on the x-z plane
    box_mesh=o3d.geometry.TriangleMesh.create_box(width=h,height=0.05,depth=w)
    box_H=np.array(
                 [[1, 0, 0, -h/2],
                  [0, 1, 0, -0.05],
                  [0, 0, 1, -w/2],
                  [0, 0, 0, 1]]
                )
    box_rgb = [0.7, 0.7, 0.7]
    name_list = ['plane']
    mesh_list, H_list, RGB_list = [box_mesh], [box_H], [box_rgb]

    # create spheres
    name_list.append('sphere_r')
    sph_mesh=o3d.geometry.TriangleMesh.create_sphere(radius=2)
    mesh_list.append(sph_mesh)
    H_list.append(np.array(
                    [[1, 0, 0, -4],
                     [0, 1, 0, 2],
                     [0, 0, 1, -2],
                     [0, 0, 0, 1]]
            ))
    RGB_list.append([0., 0.5, 0.5])

    name_list.append('sphere_g')
    sph_mesh=o3d.geometry.TriangleMesh.create_sphere(radius=2)
    mesh_list.append(sph_mesh)
    H_list.append(np.array(
                    [[1, 0, 0, -7],
                     [0, 1, 0, 2],
                     [0, 0, 1, 3],
                     [0, 0, 0, 1]]
            ))
    RGB_list.append([0., 0.5, 0.5])

    name_list.append('sphere_b')
    sph_mesh=o3d.geometry.TriangleMesh.create_sphere(radius=1.5)
    mesh_list.append(sph_mesh)
    H_list.append(np.array(
                    [[1, 0, 0, 4],
                     [0, 1, 0, 1.5],
                     [0, 0, 1, 4],
                     [0, 0, 0, 1]]
            ))
    RGB_list.append([0., 0.5, 0.5])


    #########################################
    '''
    Question 2: Add another sphere to the scene

    Write your code here to define another sphere
    in world coordinate frame
    '''
    name_list.append('sphere_world')
    sph_mesh=o3d.geometry.TriangleMesh.create_sphere(radius=1.)
    mesh_list.append(sph_mesh)
    ## the tranlsation part doesn't need to be exactly the same
    ## as long as the new sphere is on the plane and not touching
    ## other spheres
    H_list.append(np.array(
                    [[1, 0, 0, 4],
                     [0, 1, 0, 1.],
                     [0, 0, 1, -3],
                     [0, 0, 0, 1]]
            ))
    RGB_list.append([0., 0.5, 0.5])
    #########################################


    # arrange plane and sphere in the space
    obj_meshes = []
    for (mesh, H, rgb) in zip(mesh_list, H_list, RGB_list):
        # apply location
        mesh.vertices = o3d.utility.Vector3dVector(
            transform_points(np.asarray(mesh.vertices), H)
        )
        # paint meshes in uniform colours here
        mesh.paint_uniform_color(rgb)
        mesh.compute_vertex_normals()
        obj_meshes.append(mesh)

    # add optional coordinate system
    if bDisplayAxis:
        coord_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1., origin=[0, 0, 0])
        obj_meshes = obj_meshes+[coord_frame]
        RGB_list.append([1., 1., 1.])
        name_list.append('coords')


    ###################################
    #### Setup camera orientations ####
    ###################################

    # set camera pose (world to camera)
    # # camera init 
    # # placed at the world origin, and looking at z-positive direction, 
    # # x-positive to right, y-positive to down
    # H_init = np.eye(4)      
    # print(H_init)

    # camera_0 (world to camera)
    theta = np.pi * 45*5/180.
    # theta = 0.
    H0_wc = np.array(
                [[1,            0,              0,  0],
                [0, np.cos(theta), -np.sin(theta),  0], 
                [0, np.sin(theta),  np.cos(theta), 20], 
                [0, 0, 0, 1]]
            )

    # camera_1 (world to camera)
    theta = np.pi * 80/180.
    H1_0 = np.array(
                [[np.cos(theta),  0, np.sin(theta), 0],
                 [0,              1, 0,             0],
                 [-np.sin(theta), 0, np.cos(theta), 0],
                 [0, 0, 0, 1]]
            )
    theta = np.pi * 45*5/180.
    H1_1 = np.array(
                [[1, 0,            0,              0],
                [0, np.cos(theta), -np.sin(theta), -4],
                [0, np.sin(theta), np.cos(theta),  20],
                [0, 0, 0, 1]]
            )
    H1_wc = np.matmul(H1_1, H1_0)
    render_list = [(H0_wc, 'view0.png', 'depth0.png'), 
                   (H1_wc, 'view1.png', 'depth1.png')]


    ###################################################
    '''
    Extra Question: Add an extra camera view here

    Write your code here to define camera poses
    '''
    ## the students can have different theta values for H2_0
    ## but the theta for H2_1 should be the same or at least similar
    ## to keep the new camera roughly the same height as cam_0 and cam_1 
    theta = np.pi * -80/180.
    H2_0 = np.array(
                [[np.cos(theta),  0, np.sin(theta), 0],
                 [0,              1, 0,             0],
                 [-np.sin(theta), 0, np.cos(theta), 0],
                 [0, 0, 0, 1]]
            )
    theta = np.pi * 45*5/180.
    H2_1 = np.array(
                [[1, 0,            0,              0],
                [0, np.cos(theta), -np.sin(theta), -4],
                [0, np.sin(theta), np.cos(theta),  20],
                [0, 0, 0, 1]]
            )
    H2_wc = np.matmul(H2_1, H2_0)
    render_list.append((H2_wc, 'view2.png', 'depth2.png'))
    ###################################################


    # set camera intrinsics
    # the defines a pinhole camera with image size 640x480, 
    # focal length ~415.7 and image centre at (319.5,239.5)
    K = o3d.camera.PinholeCameraIntrinsic(640, 480, 415.69219381653056, 415.69219381653056, 319.5, 239.5)
    
    # Print the poses of the cameras and the intrinsic matrix defining the pinhole camera
    print('Pose_0:\n', H0_wc)
    print('Pose_1:\n', H1_wc)
    print('Intrinsics\n:', K.intrinsic_matrix)
    # o3d.io.write_pinhole_camera_intrinsic("test.json", K)


    ############################################################
    '''
    Question 4-6: Add spheres w.r.t. camera coordinate frames

    Write your code here to define the sphere
    in the camera coordinate frame
    '''
    # Note: in the following 3-D column vectors are denoted (1,2,3).
    #
    # Q4:
    # From above definition of H0_wc, the origin of world coordinate system
    # is defined wrt camera 0 coordinate system by vector (0,0,20). To see this,
    # note if P_w is the 3-D vector defining a point in 3-D space and P'_w is P_w
    # in homogeneous coordinates, ie P'_w=(P_w,1), then P'_c=H0_wcP'_w and hence
    # P_c=R0_wcP_w+T, where P_c is the vector defining the point in the camera
    # coordinate system and P'_c is P_c in homogeneous coordinates. The world origin 
    # is P_w=(0,0,0), hence wrt the camera it represented by the vector P_c=T, which
    # in this case is (0,0,20). This vector starts at the COP, passes through the
    # centre of the image and cuts the plane at the world origin, which lies on the plane.
    # Hence a sphere with centre defined by this vector will intersect the plane, with a
    # half sphere above and below. To see this, define the vector wrt the camera:
    vec = np.array([[0, 0, 20]])
    # then transform into world coordinates using the inverse of H0_wc (to give H0_cw)
    # before adding to the list of spheres for rendering (see below)
    vec_w = transform_points(vec, np.linalg.inv(H0_wc))

    # Q5:
    # To change the depth so that the sphere sits on the plane, we need to change the
    # depth according to the sphere radius (1.5). Note that the sphere centre needs to 
    # sit on the same ray from the camera and be a perpendicular distance equal to the 
    # radius above the plane. Since the angle to the plane is 45 degrees (see the camera
    # pose given by H0_wc), from Pythagorus, this means the depth along the ray needs to
    # reduce by \sqrt(2)r=3/\sqrt(2), ie we should use the vector (0,0,20-3/sqrt(2))
    #vec = np.array([[0, 0, 20-3/np.sqrt(2)]])
    #vec_w = transform_points(vec, np.linalg.inv(H0_wc))

    # Q6
    # We can place a sphere so that its centre projects to the right of the image centre
    # in camera 0 by adding a non-zero term to the x component of the vector defining
    # the sphere centre wrt camera 0. For example, we can place it 5 units away from the world
    # coordinate origin on the plane, ie:
    #vec = np.array([[5, 0, 20]])
    #vec_w = transform_points(vec, np.linalg.inv(H0_wc))

    # This sphere will also intersect the plane as the depth (along z axis) is still 20
    # To get it to sit on the plane we need to take account of the radius again and 'slide'
    # it back up the ray. The trigonometry is a bit more involved but still straightforward 
    # and can be implemented as follows:
    #vec = np.array([[5, 0, 20]])
    #reqlen = np.linalg.norm(vec)-3/np.sqrt(2)
    #reqang = np.arctan(5/20)
    #vec = np.array([[reqlen*np.sin(reqang),0,reqlen*np.cos(reqang)]])
    #vec_w = transform_points(vec, np.linalg.inv(H0_wc))

    # add sphere to list for rendering and create mesh and transformation matrix
    # to position centre as defined by vec_w
    name_list.append('sphere_cam')
    RGB_list.append([0., 0.5, 0.5])
    sph_mesh=o3d.geometry.TriangleMesh.create_sphere(radius=1.5)
    H_new = np.array(
                    [[1, 0, 0, vec_w[0, 0]],
                     [0, 1, 0, vec_w[0, 1]],
                     [0, 0, 1, vec_w[0, 2]],
                     [0, 0, 0, 1]]
            )
    sph_mesh.vertices = o3d.utility.Vector3dVector(
        transform_points(np.asarray(sph_mesh.vertices), H_new)
    )
    sph_mesh.paint_uniform_color([0.5, 0.5, 0.0])
    sph_mesh.compute_vertex_normals()
    obj_meshes.append(sph_mesh)
    ############################################################


    # Rendering RGB-D frames given camera poses
    # create visualiser and get rendered views
    cam = o3d.camera.PinholeCameraParameters()
    cam.intrinsic = K
    vis = o3d.visualization.Visualizer()
    vis.create_window(width=640, height=480, left=0, top=0)
    for m in obj_meshes:
        vis.add_geometry(m)
    ctr = vis.get_view_control()
    for (H_wc, name, dname) in render_list:
        cam.extrinsic = H_wc
        ctr.convert_from_pinhole_camera_parameters(cam)
        vis.poll_events()
        vis.update_renderer()
        vis.capture_screen_image(name, True)
        vis.capture_depth_image(dname, True)
    vis.run()
    vis.destroy_window()
