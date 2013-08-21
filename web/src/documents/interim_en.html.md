---
title: "Interim report"
layout: "default"
modified:
---

This report aims to describe the task being solved and the data that will be used. Also, we present here our proposed approach to solve the task. Additionaly, we provide an overview of several preprocession techniques and feature construction techniques that we will be using.

## 1. Requirement specification ##

The goal of the “Recognizing numbers in a videorecording” project is to apply machine learning methods to the task of processing previously recorded clips of a display of a digital voltmeter in such a way, that the temporal change in the value displayed can be easily visualized in a plot.

## 2. Data ##

The video clips were recorded at 352x288 pixels, 15 fps with a hand held cell phone. The container format is 3GP, the video codec is H.263. The recording was done by Jiří Daněk. About 15 minutes of video was recorded.

## 3. State-of-the-art ##

The problem of applying machine learning to classification of unstructured data like text or images requires some preprocessing that would result in creation of feature vectors that cn be used as the input of the clasification algorithm. Two broad classes of such preprocession techniques regarding image data can be distinguished. The first one is manual feature construction which makes use of standard processing techniques. For textual data this may be for example a bag-of-words. For images, many algorithms have been developed in the field of image processing. One example may be the SIFT features algorithm. The other approach aims to automatize the process of attribute creation by employing unsupervised machine learning.

For this project, we will be using only the manual methods. Methods using the unsupervised learning approach to extract atributes are currently in the center of scientific research, so we will describe them too.

### 3.1. Hand-crafted features ###

“The vast majority of all the creative work in the field of Artificial Intelligence was done not by machines, but by people”

Preprocessing and attribute construction is performed by an human educated in techniques from the field of image processing. The succes of this approach is highly determined by the quality of the preprocessing. The crucial role of human inventive process in creation in such attributes is reflected in the name.

The task of extracting features can be divided into following subtasks

preprocessing (tresholding, filtering)
(segmentation)
feature construction

such division allows to experiment independently with different methods for solving each of those subtasks.

#### 3.1.1. Preprocessing ####

Possible operations include tresholding, blurring or mathematical morphology techniques. In case of video we can mention digital image stabilization.

#### 3.1.2. Segmentation ####

The goal of segmentation is to find relevant parts of the image to extract attributes from.

#### 3.1.3. Feature construction ####

There are some robust universal techniques for creating features, for example SIFT/HOG or SURF. (In case the SIFT algorithm is unavailable due to patent restrictions, HOG algorithm is often used instead). Other less sophisticated techniques exist, for example taking all the pixels of the image as a bit vector is possible.

#### 3.1.4. Classification ####

Classification aims to classify the segments based on the attributes constructed.

### 3.2. Unsupervised learning ###

One might argue that Hand-crafted attributes are labour intensive to construct and it is hard to adapt them to changing requirements. With unsupervised learning, we may be able to create the attributes automatically directly from raw data or with minimal human help. This approach used to be prohibitively computationally expensive, but today its use is increasing. There exists a specific variant of this approach called Deep Learning that takes the idea even further.

The example of using unsupervised learning for constructing features to recognize handwritten digits in areacodes at postcards is provided in article [10].

#### 3.2.1. Deep Learning ####

Deep learning constitutes of repeated and layered application of unsupervised learning techniques. The outputs of the previous run of the unsupervised learning algorithm constitute the input of the following run. This creates an hierarchy from which the name of the method came to be derived. Often artifitial neural network are used. This reflects the suposed organization of the human brain which is believed to be an hierarchical conglomeration of relatively simple classifiers. After algorithms and the hierarchy construction is defined, the process can be completely automatic.

The final classifier is the uppermost layer which can classify based on outputs from any of the lower layers.

##### Building High-level Features Using Large Scale Unsupervised Learning #####

“After a training period one neuron in the network had learned to respond strongly to cats.”

In the study [9] the authors attempted to use Deep learning to create attributes for clasifiing photographies of natural scenes regarding the objects that are contained in them. Unsupervised learning of the attributes was performed on a set of 10 million still images taken from YouTube videos. The system that was created achieved twice the accuracy of the previous best system. One interesting thing that was interesting also to news reporters is that one of the attributes that were created was direct indication of the presence of a cat head in the picture.

To perform this experiment, 16000 computers were utilized for three days.


### 3.3. Previous work  ###

The task of Character optical recognition is well known and it can be solved with high accuracy. The task of finding text in a natural scene image is called “text detection” and it is still an open research problem. There is a competition called ICDAR that compares the best known text detection algorithms.

Our task of detecting numerals is greatly simplified by the fact that we do not need to be able to detect arbitrary text, but we can limit ourselves to digital numerals of a particular color.

From the available literature we have chosen these articles with similar topic to ours

#### 3.3.1. Speed limiting traffic sign recognision  ####

We have studied articles [1] and [2]. Article [1] aims at recognizing Norviegan traffic signs, the system in [2] was targeted to recognize Danish traffic sign. The methods used in both articles significantly overlap with the methods we are proposing for the solution of our task.

In article [1] the authors process the images such that first they identify a red circle which is a characteristic element of the sign using a template. Then they perform OCR on the numerals inside the circle.

The system in [2] is more general and it can detect all traffic signs that are related to speed limits, be it the signs that delimit highways or the beginning and end of a city.

Article [1] only works with the RGB color space and the techniques that are used are more basic. Article [2] tries to compare several different approaches to every step of the processing pipeline. For example, tresholding is tried in RGB and also in HSV color spaces and the tresholds are tried both static and dynamicaly adapted using collor intensity histograms.

Practical application: This capability is already available in the best equipped high class automobliles. The cars can recognize several different kinds of traffic signs, not just speed limits.

#### 3.3.2. Number plate recognition ####

Practical application: checking whether a car can park on a private parking lots, granting permission to drive through restricted gates, interval speed measurements in cities.

#### 3.3.3. Text recognition in real scenes ####

Article [4] is interesting because it contains a good introduction that introduces the unsupervised learning approach to feature construction. Articles [5.6.7] each proposes an hand-designed method for text detection. One of them for example detect text based on the presumption of uniformity of the stroke width.

Practical application: allows to apply OCR to a common photography image. This enables for example automatic extraction of shop signs. This technology is employed in Google StreetView. Another interesting thing about StreetView is that the recognition of identified house numbers is not done with OCR but it is done by people which are prezented with it as a CAPTCHA problems.

#### 3.3.4. Automated power meter inspection and reading ####
Patent [8] describes a technique for processing of static photographs of household power meters which is able to extract the power meter readings. This is very closely related to the topic of this project.

### 3.3.5. List of literature ###

[1] Efﬁcient Recognition of Speed Limit Signs
http://heim.ifi.uio.no/jimtoer/ITSC04_Torresen.pdf

[2] Automated Speed Limit Sign recognition
http://www.vip.aau.dk/wp-content/uploads/2011/12/sign11.pdf

[3] Advanced Intelligent Computing Theories and Applications
Donald C. Wunsch, Daniel S. Levine, ISBN 3540859306

[4] Text Detection And Character Recognition In Scene Images With Unsupervised Feature Learning
http://www.learningace.com/doc/2857414/e28bbaaf886b617095f8907c8a542f5c/textdetectionandcharacterrecognitioninsceneimageswithunsupervisedfeaturelearning

[5] Detecting Text in Natural Scenes with Stroke Width Transform
http://yoni.wexlers.org/papers/2010TextDetection.pdf
https://sites.google.com/site/roboticssaurav/strokewidthnokia

[6] Real-Time Scene Text Localization and Recognition
http://cmp.felk.cvut.cz/~neumalu1/neumann-cvpr2012.pdf

[7] ROBUST TEXT DETECTION IN NATURAL IMAGES WITH EDGE-ENHANCED MAXIMALLY STABLE EXTREMAL REGIONS http://www.stanford.edu/~dmchen/documents/ICIP2011_RobustTextDetection.pdf

[8] Automated meter inspection and reading
US patent číslo 5559894 vydaný dne 24 srpna 1996

[9] Building High-level Features Using Large Scale Unsupervised Learning http://arxiv.org/abs/1112.6209

[10] Sparse Feature Learning for Deep Belief Networks  Marc’Aurelio Ranzato1 Y-Lan Boureau2,1 Yann LeCun1
http://books.nips.cc/papers/files/nips20/NIPS2007_1118.pdf

### 4. Proposed solution ###

The solution we propose can be described in three steps. The first step is finding rectangular areas in the picture that bound individual numerals. Then, features are constructed from each of the rectangular bound. Finally, classification is performed and each numeral is recognized.

#### 4.1. Finding rectangular areas ####

We will now demonstrate our proposed pipeline using the image processing tools from the package ImageMagic. The following four images illustrate it. For the project, we plan to implement this processing in the Python programming language.

#### 4.1.1. Raw image ####

![Neupravený obrázek](images/1.png)

#### 4.1.2. Tresholding in the HSV color space ####

The HSV color space better preserves the human conception of distance between colors than RGB does. The greenish color of the numerals can be easily specified in HSV to formulate the treshold. The foreground is set in white and the background in black.

![Obrázek po prahování](images/2.png)

#### 4.1.3. Filtrování ####

This particular image does not suffer from this problem, but some other images might contain small green areas that can be confused for numerals. To remove such small areas, we have chosen to employ an operation from mathematical morphology called parametrized opening.

![Obrázek po filtrování](images/3.png)

#### 4.1.4. Segmentation ####

Every individual numeral forms a connected component of white pixels. Therefore, to separate the numerals we find the connected components. In the following pictures, each thus found image patch containing a numeral is highlighted by a green bounding box.

![Obrázek po segmentaci](images/4.png)

### 4.2. Feature construction ###

Before we move to creating attributes, we rescale each image patch to 5x7 pixels. That will allow us to create fixed length feature vectors
bit vector created by taking all the pixels of the rescaled patch
vector of integers where each element corresponds to a border pixel of the patch and its value is the number of neighboring background pixels in the same row or collum.

### 4.3. Classification ###

We want to try the following three classification algorithms: Naive bayes, Decision tree and Nearest neighbour. We believe that algorithms that can provide a probability estimate of an example belonging to each of the clases can be advantageous here, because we could combine that information with our background knowledge of the system and update such probability to also incorporate such knowledge. This should result in better accuracy of the solution.