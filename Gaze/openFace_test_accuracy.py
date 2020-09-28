import pandas as pd
# from Gaze.scene_data import SceneData
from Calibration.calibration import *

CONFIDENCE = 0.75

'''
##################################  Internal    ###########################################
'''

# Calibration IntrinsicMatrix cam 2
K1 = [[1735.07413218856, 0, 620.516194741532]
      , [0, 1750.83104207743, 331.901503243506]
      , [0, 0, 1]]
# K1 = [[82.7788648641717, 0, 0]
#       , [0, 77.0528785357509, 0]
#       , [504.280090951542, 323.979166674502, 1]]

# Just for testing
# (u1, v1) = [975, 490]
# (u1, v1) = [932, 617]
# internal1 = InternalCalibration(K1, [u1, v1])

# Calibration IntrinsicMatrix cam 2
K2 = [[1458.52518965647, 0, 580.557436340655]
      , [0, 1469.88062249262, 183.271603928670]
      , [0, 0, 1]]
# K2 = [[1237.02203100685, 0, 0]
#       , [0, 1784.21721755858, 0]
#       , [1211.16951302219, 13.7117890271353, 1]]

# Just for testing
# (u2, v2) = [53, 579]
# (u2, v2) = [78, 734]
# internal2 = InternalCalibration(K2, [u2, v2])

# Calibration IntrinsicMatrix cam 3
K3 = [[1015.94455114065, 0, 631.121893747347]
      , [0, 910.231786997275, 232.228547959323]
      , [0, 0, 1]]
# K3 = [[12271.4066202721, 0, 0]
#       , [0, 1043.78616891625, 0]
#       , [722.819303535740, 443.841924757028, 1]]

# Just for testing
# (u3, v3) = [570, 331]
# (u3, v3) = [557, 421]
# internal3 = InternalCalibration(K3, [u3, v3])


'''
##################################  External    ###########################################
'''

# R13 = [[0.782349000121169, -0.169501257718318, 0.599332433330048]
#         , [0.239591635241890, 0.970114436262439, -0.0383904789932114]
#         , [-0.574913811220017, 0.173629790609559, 0.799579142725319]]
# O13 = np.array([74.7606406889431, -14.7327553488660, -6.42281079025235])

R13 = [[0.0735701461673042, -0.406081845799201, 0.910870445291335]
        , [0.00706140456992441, 0.913534786388679, 0.406699312297538]
        , [-0.997265045090031, -0.0234889031268826, 0.0700763959652219]]
O13 = np.array([2.16596448233734, -10.6714788048812, 86.5916312387693])

external_1_3 = ExternalCalibration(R13, O13)


# R23 = [[0.640911870995147, 0.135362174426536, -0.755585240295243]
#         , [-0.199621137194033, 0.979853449428017, 0.00621443717306676]
#         , [0.741204003768774, 0.146847878358991, 0.655020858766041]]
# O23 = [-89.3699830996722, -26.0686885000889, 78.5946933204621]

R23 = [[0.382501261001655, -0.389541485144936, 0.837824693288054]
        , [0.466134012919456, 0.864283093329979, 0.189033903264909]
        , [-0.797754265003797, 0.318232880034481, 0.512167908730342]]
O23 = [103.972466012667, -109.844445044669, 150.025886539706]

external_2_3 = ExternalCalibration(R23, O23)

'''
##################################  Main    ###########################################
'''

# Test 3D point calculation after calibration - manually
# x3, x1 = find_3d_points(internal3, internal1, external_1_3)
# print("3D point on cam1: ", x1)
# print("3D point on cam3: ", x3)
# dist = np.linalg.norm(x1 - x3)
# print("\nDistance between two points: ", dist, "\n")

# scene_data1 = SceneData('processed/1.csv')
# scene_data2 = SceneData('processed/2.csv')
# scene_data3 = SceneData('processed/3.csv')

df1 = pd.read_csv("processed/1.csv")
df1.columns = df1.columns.str.replace(' ', '')
df2 = pd.read_csv("processed/2.csv")
df2.columns = df2.columns.str.replace(' ', '')
df3 = pd.read_csv("processed/3_multi.csv")
df3.columns = df3.columns.str.replace(' ', '')

# df1.printSchema()
# print(df1.columns)

print("Processed 1 len:", len(df1), "  Processed 2 len:", len(df2), " Processed 3 len:", len(df3))

df3_face1 = df3[df3['face_id'] == 0]
df3_face2 = df3[df3['face_id'] == 1]

print("Processed Face 1 len:", len(df3_face1), "    Processed Face 2 len:", len(df3_face2), "\n")

'''             First Try           '''
# Find the frame number on which the openFace algorithm starts to get confidence results
# for index1, row in df1.iterrows():
#     if row['confidence'] > 0.6 and row['eye_lmk_x_11'] != 0.0 and row['eye_lmk_y_11'] != 0.0:
#         internal1 = InternalCalibration(K1, [row['eye_lmk_x_11'], row['eye_lmk_y_11']])
#         print("Cam1 - Frame: ", index1)
#         print("Direction vector camera 1: ", internal1.d)
#         break
#
# for index2, row in df2.iterrows():
#     if row['confidence'] > 0.6 and row['eye_lmk_x_11'] != 0.0 and row['eye_lmk_y_11'] != 0.0:
#         internal2 = InternalCalibration(K2, [row['eye_lmk_x_11'], row['eye_lmk_y_11']])
#         print("Came2 - Frame: ", index2)
#         print("Direction vector camera 2: ", internal2.d)
#         break
#
# internal3 = InternalCalibration(K3, [df3['eye_lmk_x_11'].iloc[index1], df3['eye_lmk_y_11'].iloc[index1]])
# print("Direction vector camera 3: ", internal3.d)
# print("\n")
#
# for index, row in df1.iterrows():
#     # print(row['eye_lmk_x_11'], row['eye_lmk_y_11'])
#     if row['confidence'] > 0.6 and row['eye_lmk_x_11'] != 0.0 and row['eye_lmk_y_11'] != 0.0:
#         x3, x1 = find_3d_points(internal3, internal1, external_1_3)
#         print("3D point calculated: ", x1)
#         df1_3d_point = [row['eye_lmk_X_11'], row['eye_lmk_Y_11'], row['eye_lmk_Z_11']]
#         print("3D point from openFace: ", df1_3d_point)
#         dist = np.linalg.norm(x1 - df1_3d_point)
#         print("Distance between two points: ", dist, "\n")
#         df1['eye_lmk_11_distance'] = dist
#     else:
#         df1['eye_lmk_11_distance'] = 0.0
#
# for index, row in df2.iterrows():
#     # print(row['eye_lmk_x_11'], row['eye_lmk_y_11'])
#     if row['confidence'] > 0.6 and row['eye_lmk_x_11'] != 0.0 and row['eye_lmk_y_11'] != 0.0:
#         x3, x2 = find_3d_points(internal3, internal2, external_2_3)
#         print("3D point calculated: ", x2)
#         df2_3d_point = [row['eye_lmk_X_11'], row['eye_lmk_Y_11'], row['eye_lmk_Z_11']]
#         print("3D point from openFace: ", df2_3d_point)
#         dist = np.linalg.norm(x2 - df2_3d_point)
#         print("Distance between two points: ", dist, "\n")
#         df2['eye_lmk_11_distance'] = dist
#     else:
#         df2['eye_lmk_11_distance'] = 0.0

'''         Second Try          '''
# df23 = pd.DataFrame()
# directions = {}
# for index, row in df2.iterrows():
#     # print(row['eye_lmk_x_11'], row['eye_lmk_y_11'])
#     if row['confidence'] > 0.6 and row['eye_lmk_x_11'] != 0.0 and row['eye_lmk_y_11'] != 0.0:
#         internal1 = InternalCalibration(K2, [row['eye_lmk_x_11'], row['eye_lmk_y_11']])
#         # df23['eye_lmk_11_d2'] = internal1.d
#         directions[index, 0] = internal1.d
#     else:
#         # df23['eye_lmk_11_d2'] = None
#         directions[index, 0] = None
#
# for index, row in df3.iterrows():
#     # print(row['eye_lmk_x_11'], row['eye_lmk_y_11'])
#     if row['confidence'] > 0.6 and row['eye_lmk_x_11'] != 0.0 and row['eye_lmk_y_11'] != 0.0:
#         internal3 = InternalCalibration(K3, [row['eye_lmk_x_11'], row['eye_lmk_y_11']])
#         # df23['eye_lmk_11_d3'] = internal3.d
#         directions[index, 1] = internal3.d
#     else:
#         # df23['eye_lmk_11_d3'] = None
#         directions[index, 1] = None
#
# print(directions)
# for index in range(len(directions)):
#     if directions[index, 0] is not None and directions[index, 1] is not None:
#         x3, x2 = find_3d_points1(directions[index, 0], directions[index, 1], external_2_3)
#         print("3D point calculated: ", x2)
#         df2_3d_point = [row['eye_lmk_X_11'], row['eye_lmk_Y_11'], row['eye_lmk_Z_11']]
#         print("3D point from openFace: ", df2_3d_point)
#         dist = np.linalg.norm(x2 - df2_3d_point)
#         print("Distance between two points: ", dist, "\n")
#         # df23['eye_lmk_11_distance'] = dist

'''     Third Try       '''
for index1, row in df1.iterrows():
    if row['confidence'] > CONFIDENCE and row['eye_lmk_x_11'] != 0.0 and row['eye_lmk_y_11'] != 0.0:
        # Get the relevant row in cam3 processed output for face 1 based on frame number and timestamp
        df3_filtered_row = df3_face1[(df3_face1['timestamp'] == row['timestamp']) & (df3_face1['frame'] == row['frame'])]
        if len(df3_filtered_row) > 0:
            internal1 = InternalCalibration(K1, [row['eye_lmk_x_11'], row['eye_lmk_y_11']])
            print("Cam1 - Frame: ", index1 + 1)
            print("Timestamp:", row['timestamp'])
            print("Direction vector camera 1: ", internal1.d)

            internal3 = InternalCalibration(K3, [df3_filtered_row['eye_lmk_x_11'].iloc[0], df3_filtered_row['eye_lmk_y_11'].iloc[0]])
            print("Direction vector camera 3: ", internal3.d)

            x3, x1 = find_3d_points(internal3, internal1, external_1_3)
            print("3D point calculated: ", x1)
            df1_3d_point = [row['eye_lmk_X_11'], row['eye_lmk_Y_11'], row['eye_lmk_Z_11']]
            print("3D point from openFace: ", df1_3d_point)
            dist = np.linalg.norm(x1 - df1_3d_point)
            print("Distance between two points: ", dist, "\n")
            df1['eye_lmk_11_distance'] = dist
        else:
            df1['eye_lmk_11_distance'] = 0.0


