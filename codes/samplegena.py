import os
import cv2
import PIL
## these three resizer make all image in same demension (pixel)
def director_maker():
    for i in range(1,11):
        os.mkdir('D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler22/l%s' % i)
        os.mkdir('D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler22/l%s/positive' % i)
        os.mkdir('D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler22/l%s/negative' % i)

def r_resizer():
    dim = (256, 255)
    for i in range(1,10):
        r = cv2.imread('D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler2/l%s/r.jpg' % i,0)
        new_r = cv2.resize(r,dim)
        cv2.imwrite('D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler22/l%s/r.jpg' % i, new_r)

common_dir = 'D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler2'

def p_resizer():

    dim = (256, 255)
    for i in range(1,13):
        list1 = os.listdir('D:/academic/homework&assignment/senior design/data/edgedetection/data_3th/l%s/positive' % i)
        common_dir = 'D:/academic/homework&assignment/senior design/data/edgedetection/data_3th/l%s/positive/' % i
        img_nbr = len(list1)
        for z in range (1,img_nbr+1):
            img_name = list1[z-1]
            img_path = common_dir + img_name
            p = cv2.imread(img_path,0)
            new_p = cv2.resize(p,dim)
            cv2.imwrite('D:/academic/homework&assignment/senior design/data/edgedetection/data_3th/l%s/positive/img_%s.jpg' % (i,z) , new_p)

def n_resizer():
    dim = (256, 255)
    for i in range(1, 13):
        list1 = os.listdir(
            'D:/academic/homework&assignment/senior design/data/edgedetection/data_3th/l%s/negative' % i)
        common_dir = 'D:/academic/homework&assignment/senior design/data/edgedetection/data_3th/l%s/negative/' % i
        img_nbr = len(list1)
        for z in range(1, img_nbr + 1):
            img_name = list1[z - 1]
            img_path = common_dir + img_name
            p = cv2.imread(img_path, 0)
            new_p = cv2.resize(p, dim)
            cv2.imwrite(
                'D:/academic/homework&assignment/senior design/data/edgedetection/data_3th/l%s/negative/img_%s.jpg' % (
                i, z), new_p)

def triple_generator():
    f = open('D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler22/samples.txt','w')
    for i in range(1, 10):
        list_p = os.listdir(
            'D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler22/l%s/positive' % i)
        list_n = os.listdir(
            'D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler22/l%s/negative' % i)
        nbr_p = len(list_p)
        nbr_n = len(list_n)
        r_path = 'D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler22/l%s/r.jpg' % i
        for z in range(1,nbr_p+1):
            good_name = list_p[z-1]
            good_path1 = 'D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler22/l%s/positive/' % i
            good_path = good_path1 + good_name
            for x in range(1,nbr_n+1):
                bad_name = list_n[x-1]
                bad_path1 = 'D:/academic/homework&assignment/senior design/data/edgedetection/data2sampler22/l%s/negative/' % i
                bad_path = bad_path1 + bad_name
                one_line = r_path + ',' + good_path + ',' + bad_path
                f.write(one_line)
                f.write('\n')

def val_remake():
    images = os.listdir('D:/academic/homework&assignment/senior design/data/edgedetection/ori_val')
    nbr = 0
    n = len(images)
    for i in range(0,n):
        dir1= 'D:/academic/homework&assignment/senior design/data/edgedetection/ori_val/'
        img_path =dir1 +images[i]
        #print(img_path)
        img = cv2.imread(img_path,0)
        cv2.imwrite('D:/academic/homework&assignment/senior design/data/edgedetection/val2/img%s.jpg'% i,img)


#val_remake()
#def ano_writer():
 #   f = open('D:/academic/homework&assignment/senior design/data/edgedetection/ano.txt','w')
  #  for i in range(1,50):

if __name__ == '__main__':

    #director_maker()
    #r_resizer()
    p_resizer()
    n_resizer()
    #triple_generator()