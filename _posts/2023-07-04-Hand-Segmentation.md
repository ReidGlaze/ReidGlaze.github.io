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
