import numpy as np
from sympy import Point3D, Line3D


# A function that converts a 3d coordinate from camera space 1 to camera space 2.
def convert_from_camera1_to_camera2(point_in_3d_in_camera1, rotation_and_translation_2):
    point_in_4d_in_camera1 = np.concatenate((point_in_3d_in_camera1, np.array([1])), axis=0)
    result1 = np.dot(rotation_and_translation_2, point_in_4d_in_camera1)
    # print('projeted is: ', result1)

    return result1


# A function that project a 3d point on the image.
def project_to_2d(point_in_3d, k1):
    result = point_in_3d.dot(k1)
    result = result / result[2]
    return result


# A function that returns if person1 is looking at person2.
# Input:
# Output: Yes | No.
def calc_gaze_points_dist(right_eye1, left_eye1, right_eye2, left_eye2, points2):

    l1 = Line3D(Point3D(right_eye1[0], right_eye1[1], right_eye1[2]), Point3D(right_eye2[0], right_eye2[1], right_eye2[2]))
    l2 = Line3D(Point3D(left_eye1[0], left_eye1[1], left_eye1[2]), Point3D(left_eye2[0], left_eye2[1], left_eye2[2]))

    for p2 in points2:
        point = Point3D(p2[0], p2[1], p2[2])

        dist1 = l1.distance(point)
        dist2 = l2.distance(point)

        if(dist1 < 100 or dist2 < 100):
            return True
    return False



# Check if person1 is looking at person2
def is_looking(frame_info1, frame_info2, rotation_and_translation_3_for_first, rotation_and_translation_3_for_second, all_frame):

    eye1_left = np.array(
        [(frame_info1.eye_lmk_X_8 + frame_info1.eye_lmk_X_14)/2,
         (frame_info1.eye_lmk_Y_8 + frame_info1.eye_lmk_Y_14)/2,
         (frame_info1.eye_lmk_Z_8 + frame_info1.eye_lmk_Z_14)/2])
    # print("eye1_left for bayan is: ", eye1_left)

    eye1_right = np.array(
        [(frame_info1.eye_lmk_X_36 + frame_info1.eye_lmk_X_42) / 2,
         (frame_info1.eye_lmk_Y_36 + frame_info1.eye_lmk_Y_42) / 2,
         (frame_info1.eye_lmk_Z_36 + frame_info1.eye_lmk_Z_42) / 2])

    # print("eye1_right for bayan is: ", eye1_right)

    eye1_left_gaze = np.array([frame_info1.gaze_0_x, frame_info1.gaze_0_y, frame_info1.gaze_0_z])

    # print("eye1_left_gaze for bayan is: ", eye1_left_gaze)

    eye1_right_gaze = np.array([frame_info1.gaze_1_x, frame_info1.gaze_1_y, frame_info1.gaze_1_z])

    # print("eye1_right_gaze for bayan is: ", eye1_left_gaze)

    list_of_points_in_camera2 = []
    list_of_points_in_camera3 = []
    landmark = np.array([frame_info2.X_0, frame_info2.Y_0, frame_info2.Z_0])

    list_of_points_in_camera2.append(landmark)

    landmark = np.array([frame_info2.X_16, frame_info2.Y_16, frame_info2.Z_16])

    list_of_points_in_camera2.append(landmark)

    landmark = np.array([frame_info2.X_19, frame_info2.Y_19, frame_info2.Z_19])

    list_of_points_in_camera2.append(landmark)

    landmark = np.array([frame_info2.X_24, frame_info2.Y_24, frame_info2.Z_24])

    list_of_points_in_camera2.append(landmark)

    ###############################################

    landmark = np.array([all_frame.X_0, all_frame.Y_0, all_frame.Z_0])

    list_of_points_in_camera3.append(landmark)

    landmark = np.array([all_frame.X_16, all_frame.Y_16, all_frame.Z_16])

    list_of_points_in_camera3.append(landmark)

    landmark = np.array([all_frame.X_19, all_frame.Y_19, all_frame.Z_19])

    list_of_points_in_camera3.append(landmark)

    landmark = np.array([all_frame.X_24, all_frame.Y_24, all_frame.Z_24])

    list_of_points_in_camera3.append(landmark)

    landmark = np.array([all_frame.pose_Tx, all_frame.pose_Ty, all_frame.pose_Tz ])

    list_of_points_in_camera3.append(landmark)

    # project all to camera3 world:

    list_of_projected_points = []
    # print("merav points")
    for point in list_of_points_in_camera2:
        # print("point is: ", point)
        projected_point = convert_from_camera1_to_camera2(point, rotation_and_translation_3_for_second)
        list_of_projected_points.append(projected_point)

    # print("bayan points")
    # print("projected_eye_left")
    projected_eye_left = convert_from_camera1_to_camera2(eye1_left, rotation_and_translation_3_for_first)
    # print("projected_eye_right ")
    projected_eye_right = convert_from_camera1_to_camera2(eye1_right, rotation_and_translation_3_for_first)
    # print("projected_extended_eye1_left")
    projected_extended_eye1_left = convert_from_camera1_to_camera2(700*eye1_left_gaze + eye1_left, rotation_and_translation_3_for_first)
    # print("projected_extended_eye1_right")
    projected_extended_eye1_right = convert_from_camera1_to_camera2(700*eye1_right_gaze + eye1_right, rotation_and_translation_3_for_first)
    # print("eye1_right_gaze after projection is: ", (projected_extended_eye1_right - projected_eye_right)/ np.linalg.norm((projected_extended_eye1_right - projected_eye_right)))
    # print("eye1_left_gaze after projection is: ", (projected_extended_eye1_left - projected_eye_left)/ np.linalg.norm(projected_extended_eye1_left - projected_eye_left))
    res = calc_gaze_points_dist(projected_eye_left ,
                          projected_eye_right,
                          projected_extended_eye1_left,
                          projected_extended_eye1_right,
                          list_of_projected_points)
    if res == True:
        return projected_eye_right, projected_extended_eye1_right, res

    res = calc_gaze_points_dist(projected_eye_left,
                          projected_eye_right,
                          projected_extended_eye1_left,
                          projected_extended_eye1_right,
                          list_of_points_in_camera3)

    return projected_eye_right, projected_extended_eye1_right, res
