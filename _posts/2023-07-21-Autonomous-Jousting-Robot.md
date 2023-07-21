---
title: "Team Dopey - Autonomous Jousting Robot"
date: 2023-07-21 00:00:00 -0700
image: /assets/images/Dopey.png
categories: [Grad School Projects]
tags: [robotics,python,c++,raspberry pi,arduino,computer vision,opencv]     # TAG names should always be lowercase
---
# Autonomous Robotic Design and Execution: Project Report for Mechatronics & Robotics I
## Team Dopey
**Contributors:** Charles Callahan, Shane Cho, Reid Glaze, Mayank Pant

## Table of Contents
1. [Project Overview](#Project-Overview)
2. [Subsystems Division](#Subsystems-Division)
3. [Design Philosophy](#Design-Philosophy)
4. [Chassis Design](#Chassis-Design)
5. [Navigation System](#Navigation-System)
6. [Jousting Mechanism](#Jousting-Mechanism)
7. [Performance in Competition](#Performance-in-Competition)
8. [Improvements and Next Steps](#Improvements-and-Next-Steps)

## Project Overview <a name="Project-Overview"></a>
Our team was tasked with the design and construction of an autonomous robot capable of navigating within an 8’ x 12’ field, designed to resemble an obstacle course. The primary objective for our robot was to pop the balloons corresponding to the color of opposing teams.

The playing field was defined by boundaries indicated with 1” yellow vinyl tape. At intersections, 1” purple vinyl tape was used. The designed robot had to abide by the rule that crossing the yellow tape was prohibited, while crossing the purple tape was permitted.

Our robot design had to adhere to several constraints:
- The maximum size allowed was a 12” x 12” square and could not exceed a height of 15”.
- The robot was permitted to have a maximum of four wheels, each with a diameter of 6”.
- The robot could include a single lance, not exceeding a 6” horizontal extension from the robot's footprint.
- The design could incorporate a maximum of three microprocessors or microcontrollers and two camera systems.

## Subsystems Division <a name="Subsystems-Division"></a>
To efficiently distribute work amongst team members, we divided the project into several subsystems:

1. **Chassis:** The robot's exterior shell was designed to ensure the protection of internal components, facilitate wire routing, and enhance the overall aesthetic appeal of the robot.
2. **Navigation:** This system was responsible for the robot's ability to maneuver through the course. We further divided navigation into two subsections:
   - *Tape/Line Detection:* To facilitate tape or line detection, RGB sensors were mounted on the chassis' underside. These sensors triggered the relevant motor codes to avoid tape.
   - *Object Detection:* The Pi-camera, which was governed by OpenCV and situated at the front of the chassis, was responsible for identifying and tracking balloons on the course.
3. **Jousting Mechanism:** This system was designed to handle the task of bursting the balloons.

## Design Philosophy <a name="Design-Philosophy"></a>
When it came to the design of the robot, our main objective was to maintain simplicity while ensuring compactness. These features were crucial in ensuring the robot's ability to navigate effectively through the obstacle course.

We aimed to minimize mass and avoid unnecessary additions of components and sensors. Rather than creating a complex design that could potentially complicate the project due to the sheer number of components, we decided to aim for a more simplistic approach. We sought to create a robot that utilizes a minimal number of components to function properly and effectively meet the overall objectives of the project.

## Chassis Design <a name="Chassis-Design"></a>
The chassis served as the base for all the robot's components. The design took into account the number of motors and boards that would be needed. The initial design included two Raspberry Pis, an Arduino Uno board, two navigational motors, and one motor for a linear jousting mechanism. However, as we proceeded with the project, we realized that only one Raspberry Pi and one Arduino were sufficient, alongside only the navigational motors.

## Navigation System <a name="Navigation-System"></a>
The navigation system of our robot was designed to incrementally move towards a target balloon while "bouncing" off the yellow tape to remain within the game area. Additionally, it randomly navigated the course when no balloon was in view. The system was composed of two subroutines that handled boundary line avoidance and balloon tracking.

1. **Line Following Subroutine:** This subroutine was responsible for managing the robot's movement to avoid crossing the course boundaries. It worked by continuously monitoring the two color sensors mounted on the front left and right sides of the robot.

![Alt Text](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzM0ZjA3cDk5ZWpwN3RmdWU3NjJybGxydnhpcHYwczAza2p5OTEyMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/r5uWhXa9UBjiMBSZ3p/giphy.gif)

2. **Balloon Following Routine:** This subroutine handled the detection of balloons and directed the robot towards the target balloons while moving away from friendly balloons when too close. When no balloon was visible, this subroutine commanded the robot to move randomly within the course boundaries.

![Alt Text](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2pqYWp3aG1oaThwemd2ZHA1cGV1YXZ4Nmd6NDJqZDhlejR2czZhZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mYodNXlSpfvkiUjreq/giphy.gif)

## Jousting Mechanism <a name="Jousting-Mechanism"></a>
The jousting mechanism was initially designed to extend and retract using a rack and pinion format, with a servo motor driving the movement. After running a practice course, we decided to keep the joust stationary and instead move the robot closer to a balloon to pop it.

## Performance in Competition <a name="Performance-in-Competition"></a>
In the competition, our robot displayed varying degrees of success. Despite facing some challenges and struggles, our robot managed to score points by successfully popping the balloons of the opposing teams. However, we identified certain areas where improvements could be made, such as more strategic navigation, especially considering the extra space occupied by the attached balloon.

![Alt Text](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWt0cmx0MzFnaWlkcWJqOHB4b2U5aWVmOW5hdWtjd3Jtcmk3aWRzNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/sLhdCFNBkImhaCEYYT/giphy.gif)

![Alt Text](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExejdmeW9vamh5dWlhMTl2aG1lY3RpbXJqMGFkMTNocmgweDAzczhncCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/W8dVsaCha11yaowFV2/giphy.gif)

## Improvements and Next Steps <a name="Improvements-and-Next-Steps"></a>
During the competition, we noted that one area of our robot's design that could be improved was the navigation strategy. The robot was efficient at staying within the boundaries of the course; however, it lacked a sense of direction. We suggest the addition of an extension to the line-following subroutine to consider the purple vinyl tape, enabling the robot to position itself better towards alleyways and thus improving its navigation strategy.

![Alt Text](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3M0NWU2aGNnd2QydXc3ZnZzbHFsczZyeXVycDViOG8zZWh2b2dqbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/0GFhOCxqE8iw5yKhLf/giphy.gif)

[See the Python (Raspberry Pi) and C++ (Arduino) Code Here!](https://github.com/ReidGlaze/Mechatronics)
