import cv2
import os
from mtcnn import MTCNN
from mtcnn.utils.images import load_image
class FaceCap:
    def train(self):
        pass
    def pred(self):
        pass
    def __init__(self):
        self.detector = MTCNN(device="CPU:0")
        #os.chdir('img/')
    def train(self):
        os.chdir('img/')
        self.files=[]
        self.m=os.listdir()
        for self.file in self.m:
            if self.file.endswith(".jpg"):
                self.files.append(self.file)
        for self.file in self.files:
            self.a=cv2.imread(self.file)
            print(self.file)
            self.location=self.detector.detect_faces(self.a)
            if len(self.location)>0:
                    for self.face in self.location:
                        self.score = self.face["confidence"]
                        if self.score >= 0.90:
                            self.x1,self.y1,self.width,self.height=self.face['box']
                            self.b=self.a[int(self.y1):int(self.y1+self.height), int(self.x1):int(self.x1+self.width)]
                            cv2.imwrite("ext/extract_"+self.file,self.b)
    def pred(self):
        self.Out_img=0
        self.cap = cv2.VideoCapture(0)
        self.detector = MTCNN(device="CPU:0")
        self.count=0
        while True:
            self.ret, self.frame = self.cap.read()
            if self.ret == True:
                self.a=self.frame.copy()
                self.location=self.detector.detect_faces(self.frame)
                if len(self.location)>0:
                    for self.face in self.location:
                        self.score = self.face["confidence"]
                        if self.score >= 0.90:
                            self.x1,self.y1,self.width,self.height=self.face['box']
                            self.x2=self.x1+self.width
                            self.y2=self.y1+self.width
                            cv2.rectangle(self.a, (int(self.x1), int(self.y1)), (int(self.x2), int(self.y2)), (0, 0, 255), 2)
                            #cv2.imwrite("captured_image.jpg",self.frame[int(self.y1):int(self.y1+self.height), int(self.x1):int(self.x1+self.width)]) #The cropped output image
                cv2.imshow("capture",self.a)
                if self.count>=1:
                    break
                self.key=cv2.waitKey(1)
        
                if self.key==ord('s'):
                    cv2.imwrite("captured.jpg",self.frame[int(self.y1):int(self.y1+self.height), int(self.x1):int(self.x1+self.width)]) #The cropped output image
                    break
        
                if self.key==ord('q'):
                    break 
            else:
                break
        self.cap.release()
        cv2.destroyAllWindows()
        return 
