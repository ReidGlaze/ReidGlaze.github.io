---
title: "Hand Segmentation"
date: 2023-07-04 00:00:00 -0700
image: /assets/images/CVCanva.png
categories: [Grad School Projects]
tags: [computer vision,python,opencv]     # TAG names should always be lowercase
---


On this project, I worked with Rohit Kharat, a fellow mechanical engineering student in my MS program. As students in the Computer Vision instructed by Dr. Iona Fleming, we embarked on a fascinating project with the goal of creating a program that could detect the number of fingers a user was holding up in front of a webcam. The aim was to create a program that was as robust as possible, capable of functioning in different lighting environments, and adaptable to various skin colors. The primary tool used for this project was OpenCV, while TensorFlow, Mediapipe and similar libraries were intentionally avoided.

## Tools Used
* Python was used along with Jupyter Notebook
* Time library was used when measuring the weighted background
* OpenCV library was used for a variety of thresholding techniques
* OS library was used for system-specific functions
* Numpy used for the count function
* Sklearn used for euclidean distance (green circle)
* Tensorflow and Mediapipe were NOT allowed

## The Project

The project was divided into two main stages. The first stage was to correctly segment the hand. Initially, I thought binary thresholding would make this a relatively simple task. However, the variable lighting and texture of the hand made it a more complex challenge than anticipated. The second stage was to count the number of segments, each representing a finger. This required clear segmentation within the fingers and a distinct separation of finger segmentation. This proved to be a much more difficult problem than anticipated because segmentation includes the wrist and other parts of the hand.

Despite the challenges, the project was largely successful. The program can detect the number of fingers a user is holding up, ranging from 0 to 5. It works in variable lighting and with different skin colors. However, it's not without its flaws. It doesn't always segment the number of fingers correctly and may require the user to move their hand for the segmentation to work. Additionally, the hand segmentation doesn't always appear like a normal hand due to the blurring, contrasting, smoothing, and thresholding techniques used. However, the program provides visual cues that can help the user diagnose the problem easily.

![Alt Text](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHhudDV6azVka25iZWtteGpmb2J1Z2VvODYxMGNpY244eGEzcm96YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Q8eGVoW4yWxO0bd3T3/giphy.gif)

## Methods Used for Segmentation

A variety of computer vision methods were used for segmentation. The program takes the weighted average for the region of interest, which is bounded by a red box. This is done over time and warns the user. This allows a variety of backgrounds to be used, but it's important that the user keeps the background in the region of interest consistent over this time. The difference between the user’s hand and the measured weighted background is taken to account for different colors and lighting.

![Some Title](/assets/images/bg.png){: width="300" }


A small amount of noise was added at the very beginning to make the texture in the hand less significant. Median and Gaussian blurring were applied several times to the color image to make the texture in the hand less significant. When fingers cross over the palm, this often causes problems with the segmentation. However, too much blurring can make segmentation more difficult. The kernel size and frequency of blurring were experimented with to minimize both problems.

The bilateral filter was found to be a very important tool in performing segmentation and was used three times. This filter is effective at blurring an image while keeping the edges sharp. However, it slows down the program significantly. Despite this, the improvement in segmentation that resulted from this filter was worth the downsides.

![Some Title](/assets/images/twofingers.png){: width="300" }

A very small increase in contrast was applied to the region of interest twice. The increase in contrast was done in between the times when the bilateral filter was used. The point of this was to increase the contrast of the edges. It was found that a large adjustment in contrast caused problems with segmentation inside of the hand. Therefore, this was used sparingly.

Color to grayscale conversion is done before applying the binary threshold. This is a necessary task for performing binary thresholding. Additionally, it was important to use various image processing methods before performing the conversion because the inside of the hand can be complicated and difficult to segment.

OTSU binary thresholding was used to finally segment the grayscale image into a binary image. This method sets a custom threshold for each kernel used. The size of the kernel used was 11 by 11. This method was used to account for different colors and levels of brightness. It also helps segment variability inside of the hand. Finger counting and segmentation in a dark environment is shown. Although the segmentation of the hand looks much different, it is still able to count all 5 fingers.

![Alt Text](/assets/images/darkfingers.png){: width="300" }


## Methods used for Finger Counting

After binary thresholding, the find contours function is used to segment the hand. The contours are depicted with the blue lines shown inside the region of interest. To count the fingers, the convex hull is found, using the most extreme points that lie to the right, left, top, and bottom of the hand. The averages between the right and left points as well as the top and bottom points are taken to find the center. The center is marked by the green dot in the hand.

Four Euclidian distances are taken, measuring the distance in between the center and each of these 4 extreme points in the convex hull. The maximum of these Euclidian distances is taken before determining the radius of the circle. A radius value of 0.85 times the maximum Euclidian distance is used to determine the size of the circle. It is drawn around the center of the convex hull. The 0.85 value was taken after experimentation but can be modified for different results.

The find contours function is used to find how many segmentations lie on the circle. The circular region of interest is used as a mask. Each of the segmentations are outlined by blue boxes in the images. Since the wrist lies outside of the circle, it is important to exclude the contour region that lies at the bottom of the image. Additionally, forming a fist can cause a segmentation at the top of the hand when no fingers are being raised. This segmentation is excluded by dropping all segmentations that exceed 15 percent of the circumference. Exclusion of these segmentations is shown.

![Alt Text](/assets/images/exclude.png){: width="300" }


There were several methods that did not work as expected. For example, excessive blurring was initially used many times with large kernel sizes. It was theorized that this blurring would minimize dark and light spots on the hand and therefore make thresholding and segmentation easier. However, this level of blurring made the edges harder to detect and did not work well when lighting conditions were changed. When little to no blurring was used, the segmentation of the hand was patchy. This can result in problems because a single finger could result in two or more segmentations. It is important to use enough blurring so that the black patches are limited to parts of the hand that are not counted for segmentation.

When a single constant was used for segmentation, there were a few problems. This constant needed to be modified for variable levels of brightness and skin colors. Segmentation worked well when there was a large amount of contrast in between the background and the hand. However, it did not work well in other conditions. The segmentations were much patchier, which causes problems with finger counting.

It was theorized that more contrast would help improve the accuracy of the contours. While this may have been accurate in some areas, the higher use of contrasting caused patchiness inside of the hand. For this reason, contrasting was used very sparingly.

While the bilateral filter is used 3 times in this program, it was not used as the sole method of blurring in this program. This is because the bilateral filter can cause the program to run slowly. This program does run slowly but not excessively so. It was important to find a balance in using this filter so that the hand would segment well, and the program would run without crashing or being obnoxiously slow.

A factor that was multiplied by the maximum Euclidian distance was tested at different values. A value that was too high resulted in segmentations that were not counted. A value that was too low resulted in counting segmentations that were not represented by fingers. These segmentations would come from other parts of the hand. Ultimately, a value of 0.85 was chosen.

## Limitations & Possible Future Extensions

The program has known limitations and possible future extensions. One problem is that the fingers must be clearly separated to segment correctly. When the Star Trek symbol is held up, the program shows only two fingers. We are unsure how to solve this problem and it could be rather difficult to solve without using more advanced libraries.

![Alt Text](/assets/images/startrek.png){: width="300" }

Sometimes, segmentations can be inaccurate due to watches or other wearables. The segmentation of the watch changes the size of the circle and can result in problems. Shadows can also alter the segmentations and cause the size of the circle to change. In this example, the circle is made to be too large and one of the fingers is not counted.

Inaccurate segmentations can be caused for a variety of reasons including lighting, angle and proximity of the hand, hand shape. This program is far from perfect and has lots of room for improvement. Visual cues can be used to help the user position the hand correctly, but this program may not be reliable without such feedback. However, it provides nice insight into how the program is implemented and strives to improve robustness and adaptability to variable conditions.

## Contributions

In terms of contributions, I worked on the implementation of different methods and visual demonstration of the segmentation and finger counting. I worked on the CVproject.py file. My colleague, Rohit, worked on testing thresholding methods, blurring methods, morphological operations, and evaluation of distance measures. He worked on the Capstone_BlurSmooth.py, Capstone_DistMeas.py, Capstone_Moropho.py, and Capstone_Threshold.py files.

## Conculsion

Through this project, I learned the advantage of using OTSU binary thresholding over regular binary thresholding. I learned the significance of this tool by experimenting with variable lighting conditions. I also learned how a bilateral filter can be useful for segmentation of an object from a background. This was discovered by using the tool in place of other forms of blurring. Lastly, I learned how the use of a mask can be used to count segmentations. This was done by utilizing the circle. In conclusion, this project was a great learning experience and provided great insight into the opencv library.

### [See the Code on Github!](https://github.com/ReidGlaze/Computer_Vision/blob/main/Final_Project/CVProject.py)
