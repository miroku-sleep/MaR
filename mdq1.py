import numpy as np
def rot_trans(x_ang, y_ang, z_ang):
    x0 = np.radians(float(x_ang))
    y0 = np.radians(float(y_ang))
    z0 = np.radians(float(z_ang))

    Rx = np.array([[1, 0, 0],
                   [0, np.cos(x0), -np.sin(x0)],
                   [0, np.sin(x0), np.cos(x0)]])
    
    Ry = np.array([[np.cos(y0), 0, np.sin(y0)],
                   [0, 1, 0],
                   [-np.sin(y0), 0, np.cos(y0)]])
    
    
    Rz = np.array([[np.cos(z0), -np.sin(z0), 0],
                   [np.sin(z0), np.cos(z0), 0],
                   [0, 0, 1]])
    
    return Rx @ Ry @ Rz

obj_cord=input("enter object coordinates(camera frame): ")
obj_cord=np.fromstring(obj_cord, sep=',')

rvr_frame=input("enter Rover Position (World Frame): ")
rvr_frame=np.fromstring(rvr_frame, sep=',')

x_ang=input(" x Angle in degrees): ")
y_ang=input(" y Angle in degrees): ")
z_ang=input(" z Angle in degrees): ")

obj_cam=rot_trans(x_ang, y_ang, z_ang)
obj_cord=obj_cam @ obj_cord

obj_wcord=obj_cord+rvr_frame

print(f"Object Coordinates (World Frame): {obj_wcord}")

