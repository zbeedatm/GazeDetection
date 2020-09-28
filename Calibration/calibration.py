import numpy as np

'''
  Internal calibration of one camera:
  ----------------------------------
  k - Calibration matrix (the intrinsicMatrix)
  p=[u, v] - pixel in the image
  d - Direction vector
'''


class InternalCalibration:
    def __init__(self, k, p: [int, int]):
        self.k = k
        self.u = p[0]
        self.v = p[1]
        self.d = np.linalg.inv(self.k).dot([self.u, self.v, 1])


'''
  External calibration between 2 cameras:
  ---------------------------------------
  R - Rotation Matrix of camera one relative to camera two
  O - Orientation Vector: Translation of camera one relative to camera two
'''


class ExternalCalibration:
    def __init__(self, r, o):
        self.r = r
        self.o = o


'''
  External calibration output between 2 cameras:
  ---------------------------------------------
  R - Rotation Matrix of camera one relative to camera two
  O - Translation vector of camera one relative to camera two
  
  Annotations:
  ---------
  org - of camera which represents the real world (with origin [0,0])
  rel - of relative camera with translation vector
      
  Output:
  ------
  3D point on each camera
'''

minimum_distance = 100


def find_3d_points(internal_org: InternalCalibration, internal_rel: InternalCalibration, external: ExternalCalibration):
    dist = 1000
    x_org = None
    x_rel = None

    d_mul = np.matmul(np.linalg.inv(external.r), internal_rel.d)

    while dist > minimum_distance:
        alpha = np.random.randint(200)
        beta = np.random.randint(200)

        #print("alpha: ", alpha)
        #print("beta: ", beta)

        x_org = alpha*internal_org.d + [0, 0, 0]
        x_rel = beta*d_mul + external.o

        dist = np.linalg.norm(x_org - x_rel)
        #print("distance: ", dist)

    # print("distance between 2 closest points: ", dist)
    # print("alpha: ", alpha)
    # print("beta: ", beta)
    # print("X Origin: ", x_org)
    # print("X Relative: ", x_rel)
    return x_org, x_rel


def find_3d_points1(d_org, d_rel, external: ExternalCalibration):
    dist = 1000
    x_org = 0
    x_rel = 0

    d_mul = np.matmul(np.linalg.inv(external.r), d_rel)

    while dist > minimum_distance:
        alpha = np.random.randint(200)
        beta = np.random.randint(200)

        #print("alpha: ", alpha)
        #print("beta: ", beta)

        x_org = alpha*d_org + [0, 0, 0]
        x_rel = beta*d_mul + external.o

        dist = np.linalg.norm(x_org - x_rel)
        #print("distance: ", dist)

    # print("distance between 2 closest points: ", dist)
    # print("alpha: ", alpha)
    # print("beta: ", beta)
    # print("X Origin: ", x_org)
    # print("X Relative: ", x_rel)
    return x_org, x_rel


def find_3d_points_by_least_square(internal_org: InternalCalibration, internal_rel: InternalCalibration, external: ExternalCalibration):
    o_org = [0, 0, 0]
    d_mul = np.matmul(np.linalg.inv(external.r), internal_rel.d)

    a = np.array([internal_org.d, d_mul]) # TODO - internal_rel.d])
    # print("A=",A)

    b = external.o - o_org
    # print("b=",b)

    # Ax=b
    beta, alpha = np.linalg.lstsq(a.T, b, rcond=None)[0]
    # beta=-beta
    print("alpha: ", alpha)
    print("beta: ", beta)

    x_org = o_org + -alpha * internal_org.d
    print("X Origin=", x_org)

    x_rel = external.o + beta * internal_rel.d
    print("X Relative=", x_rel)

    return x_org, x_rel


def plot_3d(x1, x2):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x1, x2, c='r', marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

