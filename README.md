# Auto-Grade
[![](https://img.shields.io/badge/Made_with-Python3-blue?style=for-the-badge&logo=python)]()
[![](https://img.shields.io/badge/Made_with-Flask-red?style=for-the-badge&logo=Flask)](https://flask.palletsprojects.com/en/1.1.x/)
[![](https://img.shields.io/badge/Made_with-Tensorfolw-green?style=for-the-badge&logo=Tensorflow)](https://www.tensorflow.org/)

Converting handwritten answers to text using Handwriting recognition technique and grading them accordingly.

# Model
Dataset: MNIST dataset was used.

Architecture:

![Model Architecture](architecture.PNG)

**Training accuracy : 98%**

**Test accuracy :  99.01%**

# Answer Detection

- First we convert the pdf to image
- Then using opencv we detect the rectangles in which the answers should be given.
- Cropping out the answers and processing it before passing it to the model for prediction.
- Prediction
 
![Rectangle Detection](rectangle.PNG)

# To run files on the website check out the format or use :
Data/answers-multipage.csv
Data/answers-multipage.pdf
