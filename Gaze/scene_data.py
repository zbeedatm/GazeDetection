import csv


class SceneData:
    def __init__(self, file_path):
        with open(file_path, encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # a map between frame id to frame info
            self.frame_id_to_frame_info = {}
            count = 0
            for row in csv_reader:
                if count == 0:
                    count = count + 1
                    continue
                if row[0] not in self.frame_id_to_frame_info.keys():
                    self.frame_id_to_frame_info[row[0]] = [Frame(row)]
                else:
                    self.frame_id_to_frame_info[row[0]].append(Frame(row))


class Frame:

    def __init__(self, row):
        self.timestamp = float(row[2])
        self.confidence = float(row[3])
        self.success = float(row[4])

        self.face_id = float(row[1])

        self.gaze_0_x = float(row[5])
        self.gaze_0_y = float(row[6])
        self.gaze_0_z = float(row[7])
        self.gaze_1_x = float(row[8])
        self.gaze_1_y = float(row[9])
        self.gaze_1_z = float(row[10])

        self.gaze_angle_x = float(row[11])
        self.gaze_angle_y = float(row[12])

        # left eye: eye_lmk_x_8 in 2D
        self.eye_lmk_x_8 = float(row[133])
        # left eye: eye_lmk_x_11 in 2D
        self.eye_lmk_x_11 = float(row[136])
        # left eye: eye_lmk_x_14 in 2D
        self.eye_lmk_x_14 = float(row[139])
        # left eye: eye_lmk_x_17 in 2D
        self.eye_lmk_x_17 = float(row[142])

        # left eye: eye_lmk_y_8 in 2D
        self.eye_lmk_y_8 = float(row[189])
        # left eye: eye_lmk_y_11 in 2D
        self.eye_lmk_y_11 = float(row[192])
        # left eye: eye_lmk_y_14 in 2D
        self.eye_lmk_Y_14 = float(row[195])
        # left eye: eye_lmk_y_17 in 2D
        self.eye_lmk_y_17 = float(row[198])

        # left eye: eye_lmk_X_8 in 3D
        self.eye_lmk_X_8 = float(row[133])
        # left eye: eye_lmk_X_11 in 3D
        self.eye_lmk_X_11 = float(row[136])
        # left eye: eye_lmk_X_14 in 3D
        self.eye_lmk_X_14 = float(row[139])
        # left eye: eye_lmk_X_17 in 3D
        self.eye_lmk_X_17 = float(row[142])

        # left eye: eye_lmk_Y_8 in 3D
        self.eye_lmk_Y_8 = float(row[189])
        # left eye: eye_lmk_Y_11 in 3D
        self.eye_lmk_Y_11 = float(row[192])
        # left eye: eye_lmk_Y_14 in 3D
        self.eye_lmk_Y_14 = float(row[195])
        # left eye: eye_lmk_Y_17 in 3D
        self.eye_lmk_Y_17 = float(row[198])

        # left eye: eye_lmk_Z_8 in 3D
        self.eye_lmk_Z_8 = float(row[245])
        # left eye: eye_lmk_Z_11 in 3D
        self.eye_lmk_Z_11 = float(row[248])
        # left eye: eye_lmk_Z_14 in 3D
        self.eye_lmk_Z_14 = float(row[251])
        # left eye: eye_lmk_Z_17 in 3D
        self.eye_lmk_Z_17 = float(row[254])

        # right eye: eye_lmk_x_36 in 2D
        self.eye_lmk_x_36 = float(row[161])
        # right eye: eye_lmk_x_39 in 2D
        self.eye_lmk_x_39 = float(row[164])
        # right eye: eye_lmk_x_42 in 2D
        self.eye_lmk_x_42 = float(row[167])
        # right eye: eye_lmk_x_45 in 2D
        self.eye_lmk_x_45 = float(row[170])

        # right eye: eye_lmk_y_36 in 2D
        self.eye_lmk_y_36 = float(row[217])
        # right eye: eye_lmk_y_39 in 2D
        self.eye_lmk_y_39 = float(row[220])
        # right eye: eye_lmk_y_42 in 2D
        self.eye_lmk_y_42 = float(row[223])
        # right eye: eye_lmk_y_45 in 2D
        self.eye_lmk_y_45 = float(row[226])

        # right eye: eye_lmk_X_36 in 3D
        self.eye_lmk_X_36 = float(row[161])
        # right eye: eye_lmk_X_39 in 3D
        self.eye_lmk_X_39 = float(row[164])
        # right eye: eye_lmk_X_42 in 3D
        self.eye_lmk_X_42 = float(row[167])
        # right eye: eye_lmk_X_45 in 3D
        self.eye_lmk_X_45 = float(row[170])

        # right eye: eye_lmk_Y_36 in 3D
        self.eye_lmk_Y_36 = float(row[217])
        # right eye: eye_lmk_Y_39 in 3D
        self.eye_lmk_Y_39 = float(row[220])
        # right eye: eye_lmk_Y_42 in 3D
        self.eye_lmk_Y_42 = float(row[223])
        # right eye: eye_lmk_Y_45 in 3D
        self.eye_lmk_Y_45 = float(row[226])

        # right eye: eye_lmk_Z_36 in 3D
        self.eye_lmk_Z_36 = float(row[273])
        # right eye: eye_lmk_Z_39 in 3D
        self.eye_lmk_Z_39 = float(row[276])
        # right eye: eye_lmk_Z_42 in 3D
        self.eye_lmk_Z_42 = float(row[279])
        # right eye: eye_lmk_Z_45 in 3D
        self.eye_lmk_Z_45 =float( row[282])

        # Head pos
        self.pose_Tx = float(row[293])
        self.pose_Ty = float(row[294])
        self.pose_Tz = float(row[295])

        # location land mark
        self.X_0 = float(row[435])
        self.X_1 = float(row[436])
        self.X_2 = float(row[437])
        self.X_3 = float(row[438])
        self.X_4 = float(row[439])
        self.X_5 = float(row[440])
        self.X_6 = float(row[441])
        self.X_7 = float(row[442])
        self.X_8 = float(row[443])
        self.X_9 = float(row[444])
        self.X_10 = float(row[445])
        self.X_11 = float(row[446])
        self.X_12 = float(row[447])
        self.X_13 = float(row[448])
        self.X_14 = float(row[449])
        self.X_15 = float(row[450])
        self.X_16 = float(row[451])
        self.X_17 = float(row[452])
        self.X_18 = float(row[453])
        self.X_19 = float(row[454])
        self.X_20 = float(row[455])
        self.X_21 = float(row[456])
        self.X_22 = float(row[457])
        self.X_23 = float(row[458])
        self.X_24 = float(row[459])
        self.X_25 = float(row[460])
        self.X_26 = float(row[461])

        self.Y_0 = float(row[503])
        self.Y_1 = float(row[504])
        self.Y_2 = float(row[505])
        self.Y_3 = float(row[506])
        self.Y_4 = float(row[507])
        self.Y_5 = float(row[508])
        self.Y_6 = float(row[509])
        self.Y_7 = float(row[510])
        self.Y_8 = float(row[511])
        self.Y_9 = float(row[512])
        self.Y_10 = float(row[513])
        self.Y_11 = float(row[514])
        self.Y_12 = float(row[515])
        self.Y_13 = float(row[516])
        self.Y_14 = float(row[517])
        self.Y_15 = float(row[518])
        self.Y_16 = float(row[519])
        self.Y_17 = float(row[520])
        self.Y_18 = float(row[521])
        self.Y_19 = float(row[522])
        self.Y_20 = float(row[523])
        self.Y_21 = float(row[524])
        self.Y_22 = float(row[525])
        self.Y_23 = float(row[526])
        self.Y_24 = float(row[527])
        self.Y_25 = float(row[528])
        self.Y_26 = float(row[529])

        self.Z_0 = float(row[571])
        self.Z_1 = float(row[572])
        self.Z_2 = float(row[573])
        self.Z_3 = float(row[574])
        self.Z_4 = float(row[575])
        self.Z_5 = float(row[576])
        self.Z_6 = float(row[577])
        self.Z_7 = float(row[578])
        self.Z_8 = float(row[579])
        self.Z_9 = float(row[580])
        self.Z_10 = float(row[581])
        self.Z_11 = float(row[582])
        self.Z_12 = float(row[583])
        self.Z_13 = float(row[584])
        self.Z_14 = float(row[585])
        self.Z_15 = float(row[586])
        self.Z_16 = float(row[587])
        self.Z_17 = float(row[588])
        self.Z_18 = float(row[589])
        self.Z_19 = float(row[590])
        self.Z_20 = float(row[591])
        self.Z_21 = float(row[592])
        self.Z_22 = float(row[593])
        self.Z_23 = float(row[594])
        self.Z_24 = float(row[595])
        self.Z_25 = float(row[596])
        self.Z_26 = float(row[597])


# s = SceneData('./processed/1.csv')
# print(s.frame_id_to_frame_info.keys())
