import json
import os
import sys
import argparse
import numpy as np

class process_date:
    def __init__(self, folder_path, write_path, label):
        self.folder_path  = folder_path
        self.write_path = write_path
        self.key_point = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 16, 17, 18, 19, 20, 24, 25, 26, 27, 28, 29, 30, 31, 32, 36, 37, 38, 39, 40, 41}
        self.counter = np.zeros(75, dtype = int)
        files = os.listdir(self.folder_path)
        for filename in files:
            self.json_path = self.folder_path + filename
            #print(self.json_path)
            self.pose_keypoints_2d = []
            self.person_num = 0
            if self.output() == True:
                print ('ture')
                with open(self.write_path, 'a') as file:
                    for index in range(len(self.pose_keypoints_2d)):
                        file.write(str(self.pose_keypoints_2d[index]))
                        file.write('\n')
                    file.write(filename + label + '\n')
                file.close()
                # self.person_id = -2  
        print(self.counter)   
        
    def resolveJson(self):
        fileJson = open(self.json_path,'rb')
        #print(self.json_path)
        fileJson = json.load(fileJson)
        people = fileJson["people"]
    #    person_id = fileJson["person_id"]
    #    pose_keypoints_2d = fileJson["pose_keypoints_2d"]
        return (people)

    def output(self):
        People = self.resolveJson()
        # print(result)
        for person in People:
            
            
            # print(type(person))
            # self.person_id = person['person_id']
            #self.person_num += 1
            count = 0
            self.pose_keypoints_2d = person['pose_keypoints_2d']
            print(self.pose_keypoints_2d)
            for index in range(len(self.pose_keypoints_2d)):
                if self.pose_keypoints_2d[index] == 0:
                    self.counter[index] += 1
            self.pose_keypoints_2d = [self.pose_keypoints_2d[index] for index in range(len(self.pose_keypoints_2d)) if self.pose_keypoints_2d[index] != 0 and index in self.key_point]
            print(self.pose_keypoints_2d)
            print(len(self.pose_keypoints_2d))
            if len(self.pose_keypoints_2d) == 33:
                return True
            # for items, index in  self.pose_keypoints_2d:
            #     print (items, index)
            # #     if self.pose_keypoints_2d[items] parser.add_argument("-folder_path", type=str, default=None,
            # #         count += 1
            # #         self.pose_keypoints_2d.remove(0)
            # # print(count)
            # # print(len(self.pose_keypoints_2d))
            # # print(len(self.pose_keypoints_2d))
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder_path", type=str, default=None,
                        help="path to the folder for the json to be processed (default: None)")
    parser.add_argument("--write_path", type=str, default=None,
                        help="path to the folder for the results to be saved (default: None)")
    parser.add_argument("--label", type=str, default=None,
                        help="label (default: None)")
    args = parser.parse_args()
    folder_path = args.folder_path
    write_path = args.write_path
    label = args.label

    process_date(folder_path, write_path, label)
    # process_date(r'/home/hts/hts2019/openpose/Res/','/home/hts/hts2019/openpose/keypoints.txt')            
    # path = r'/home/hts/hts2019/openpose/Res/01_keypoints.json'
    # output()