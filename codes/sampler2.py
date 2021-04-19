import os
from time import sleep
import cv2
from pathlib import Path
## create directory for a "standard" data set
#for i in range(1,11):
#    os.mkdir('D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler2/l%s' % i)
#    os.mkdir('D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler2/l%s/positive' % i)
#    os.mkdir('D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler2/l%s/negative' % i)
def triplelet_generator():
    f = open("../../data/edgedetection/data2/data2.TXT", "r")
    common_in_dir = 'D:/academic/homework&assignment/senior design/data/edgedetection/data2/'

#common_dir_r = 'D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler2/l%s' % i
#common_dir_p = 'D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler2/l%s/positive' % i
#common_dir_n = 'D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler2/l%s' % i
    for i in range(1,100):
        img_name = f.readline()
        if img_name[0] == 'r':
            nbr = img_name[4]
            img_path = 'D:/academic/homework&assignment/senior design/data/edgedetection/data2/r_1_%s.jpg' % img_name[4]
            img = cv2.imread(img_path, 0)

            cv2.imwrite('D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler2/l%s/r.jpg' % nbr, img)
        else:
         # judge if it is opsitive or negative
            img_path1 = 'D:/academic/homework&assignment/senior design/data/edgedetection/data2/'
            img_path2 = img_name
            print(img_name)
        #img = cv2.imread(img_pat2,0)
        #print(img)
            print(img_path2)
            r_or_w = img_name[-2]
            #if r_or_w == '1'


