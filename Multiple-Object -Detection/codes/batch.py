import cv2,glob

images=glob.glob("*.PNG")

for image in images:
	img=cv2.imread(image,0)
	re=cv2.resize(img,(28,28))
	#cv2.imshow("checking",re)

	#cv2.waitKey(1)
	#cv2.destroyAllWindows()
	cv2.imwrite("0."+image,re)
