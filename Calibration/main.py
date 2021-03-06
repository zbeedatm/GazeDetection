from Calibration.calibration import *

'''
##################################  Internal    ###########################################
'''

# Calibration IntrinsicMatrix cam 2
K1 = [[1735.07413218856, 0, 620.516194741532]
      , [0, 1750.83104207743, 331.901503243506]
      , [0, 0, 1]]
[u1, v1] = (555, 211)

internal1 = InternalCalibration(K1, [u1, v1])

# Calibration IntrinsicMatrix cam 2
K2 = [[1458.52518965647, 0, 580.557436340655]
      , [0, 1469.88062249262, 183.271603928670]
      , [0, 0, 1]]

[u2, v2] = (342, 535)

internal2 = InternalCalibration(K2, [u2, v2])


# Calibration IntrinsicMatrix cam 3
K3 = [[1015.94455114065, 0, 631.121893747347]
      , [0, 910.231786997275, 232.228547959323]
      , [0, 0, 1]]
[u3, v3] = (330, 307)

internal3 = InternalCalibration(K3, [u3, v3])

'''
##################################  External    ###########################################
'''

R13 = [[0.782349000121169, -0.169501257718318, 0.599332433330048]
        , [0.239591635241890, 0.970114436262439, -0.0383904789932114]
        , [-0.574913811220017, 0.173629790609559, 0.799579142725319]]

O13 = np.array([74.7606406889431, -14.7327553488660, -6.42281079025235])

external_1_3 = ExternalCalibration(R13, O13)


R23 = [[0.640911870995147, 0.135362174426536, -0.755585240295243]
        , [-0.199621137194033, 0.979853449428017, 0.00621443717306676]
        , [0.741204003768774, 0.146847878358991, 0.655020858766041]]

O23 = [-89.3699830996722, -26.0686885000889, 78.5946933204621]

external_2_3 = ExternalCalibration(R23, O23)

'''
##################################  Main    ###########################################
'''

print("Between 1 and 3 ::")
x3, x1 = find_3d_points(internal3, internal1, external_1_3)
# plot_3d(x3, x1)

print("\nBetween 2 and 3 ::")
x3, x2 = find_3d_points(internal3, internal2, external_2_3)
# plot_3d(x3, x1)

print("\n------------  Least Squar --------------")
x, xx = find_3d_points_by_least_square(internal3, internal1, external_1_3)
