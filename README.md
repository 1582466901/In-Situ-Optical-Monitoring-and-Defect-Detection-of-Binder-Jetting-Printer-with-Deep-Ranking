# In-Situ-Optical-Monitoring-and-Defect-Detection-of-Binder-Jetting-Printer-with-Deep-Ranking
An image collecting system is developed to capture optical images of printed pattern in a X1 innovent+ printer. Then, segementation methods are applied to the images and the segmented images are compared with a reference image by deep ranking model.

The image collecting system includes a RaspberryPi 3B computer, a Raspberry Pi HD camera, a pair of beam-break sensors and a desktop computer. It also includes some mounting structures to fix the electronics to the printer. 
The diagrams showns the mounting structure and the electronics. 

For the segmentation method, canny edge detection is applied to transfer the RGB image to a black and white photo. Use the 'canny2.py' file for segmentation. More info can be seen here  https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123, the dataset we collected in our lab is also uploaded. 

After segmentation, the deep ranking model need to be trained with manually labeled datasets. We creats our datasets and labeled it already. You may download the data_lite.rar file. 
One more step is required before the images can be fed in model for training. A txt file includes sampled triplets need to be generated. The code for sampling is "samplegena.py"
The deep ranking model we use is a revised version from this project:
https://github.com/Zhenye-Na/image-similarity-using-deep-ranking, 
the mechanism are described in this paper: 
https://medium.com/@akarshzingade/image-similarity-using-deep-ranking-c1bd83855978
To train the model, run main.py 

After training finished, the model is stored as a .tar file, the best model we trained is uploaded as 'model_best.pth.tar'
To test the model, another dataset is used (also included in the 'data_lite.rar' A program for testing is uploaded as ‘’test_model.py.' It will update the overall accuracy. 




