import pdf2image
from pdf2image import convert_from_path
import numpy as np
import cv2
from PIL import Image 
import numpy as np

from keras.models import load_model
model = load_model('./Model/cnn5.h5')

def get_answers(file):
  # pages = convert_from_path(file)
  pages = convert_from_path(file)
  answers = []
  for page in pages:
      page.save('out.jpg', 'JPEG')
      image = cv2.imread('out.jpg')
      cim = cv2.imread('out.jpg')
      imgGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      _, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
      contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
      count=0
      rectangles = []
      for contour in contours:
          approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
          cv2.drawContours(image, [approx], 0, (0, 0, 0), 5)
          x = approx.ravel()[0]
          y = approx.ravel()[1] - 5
          if len(approx) == 4:
              x1 ,y1, w, h = cv2.boundingRect(approx)
              aspectRatio = float(w)/h
              if aspectRatio >= 0.95 and aspectRatio <= 1.05:
                pass
              else:
                if(x1!=0 and h>30):
                  rectangles.append([x1 ,y1, w, h])
                  count=count+1

      px1 ,py1, pw, ph = rectangles[0]
      final = [rectangles[0]]

      for rectangle in rectangles:
        if(py1-ph>rectangle[1]):
          px1 ,py1, pw, ph = rectangle
          final.append(rectangle)
      for i in final:
        cv2.rectangle(image,(i[0],i[1]),(i[0]+i[2],i[1]+i[3]),(0,255,0),6)
      # cv2_imshow(image)
      # print(final)
      page_answers=[]
      for i in final:
        img = cim[i[1]:i[1]+i[3], i[0]:i[0]+i[2]]
        # cv2_imshow(img)
        img = Image.fromarray(img) 
        x=img.convert("L") 
        x = x.resize((28,28))
        # x.show()
        #compute a bit-wise inversion so black becomes white and vice versa
        x = np.invert(x)
        #convert to a 4D tensor to feed into our model
        x = x.reshape(1,28,28,1)
        x = x.astype('float32')
        x /= 255
        out = model.predict(x)
        # print(np.argmax(out[0][1:5])+1)
        page_answers.append(np.argmax(out[0][1:5])+1)
      answers.extend(page_answers[::-1])
  return answers

# [2, 1, 3, 4, 3, 4, 1, 1, 1, 2, 3, 2, 2, 3, 3]