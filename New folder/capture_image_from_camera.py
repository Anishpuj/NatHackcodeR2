from cv2 import *
cam_port = 1
cam = VideoCapture(cam_port)
# reading the input using the camera

inp = input('Enter person name')
# If image will detected without any error,
# show result
while(1): 
        result,image = cam.read()
        imshow(inp, image)
        if cv2.waitKey(0):
         imwrite(inp+".png", image)
         print("image taken")

# If captured image is corrupted, moving to else part
else:
	print("No image detected. Please! try again")
