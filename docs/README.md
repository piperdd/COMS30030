# COMS30030: Image Processing and Computer Vision  (TB1) 25-26

## Introduction

This is the teaching unit for the 3rd year CS option Image Processing and Computer Vision. The unit covers all the content needed to take the minor option as part of COMS30081 Topics in CS and the major option COMS30087.

Broadly speaking, Image Processing (IP) refers to techniques that transform images into other images, whilst Computer Vision (CV) concerns extracting information about the scene captured in an image. Examples of IP include filtering, spatial transformation, enhancement, compression, denoising and restoration, and of CV, include detection and recognition of objects, activities, people, places, etc, extraction of 3-D structure and motion, visual navigation and general scene understanding. However, there is considerable overlap between the two areas and thus a strict definition neither exists nor is especially useful, e.g. some techniques can be viewed as either IP or CV and CV often uses IP techniques as a starting point.

Both the minor and major options provide an introduction to both topics, with the major option providing additional practical experience of converting theory into practice. The focus is on covering the fundamental principles and ideas and their use in example techniques. The latter includes edge detection, filtering, segmentation, object detection, stereo and motion estimation. The content is divided into two parts, the first covering techniques applied to still images (Majid) and the second covering techniques applied to multiple images and video (Andrew).

Finally, a word about deep learning. It is probably fair to say that both IP and CV have been changed dramatically by the advent of deep learning techniques, which has revolutionised and facilitated great strides in both topics. For example, the vast majority of papers at the major conferences describing state of the art techniques will be based on deep learning. However, it is also true to say that to contribute to or make use of this work requires a good understanding of the fundamentals that are covered in this unit. With this, you will be well prepared to take 4th year units in deep learning that cover techniques and applications in IP and CV, i.e. COMSM0045 Applied Deep Learning and COMSM0159 Advanced Visual AI.

## Unit Materials and Textbooks

Lectures slides and related material can be found under Weekly Unit Materials below.  The material is not taught strictly along the lines of a textbook. However, often it is useful to read around a topic to get a different perspective and the many textbooks on image processing and computer vision can be helpful for this. It is also worth looking on the web for material, but you should always refer back to the content covered in lectures as your definitive source. You are also encouraged to ask questions about any aspects you do not understand or want clarifying - either ask at the end of a lecture or message on the unit's Team page. Your question is most likely something others may ask too and by putting it on Teams, our response will potentially benefit many others.

## Staff

- [Andrew Calway](http://people.cs.bris.ac.uk/~andrew/) [a.calway@bristol.ac.uk] (unit director)
- [Majid Mirmehdi](https://majidmirmehdi.github.io/) [m.mirmehdi@bristol.ac.uk]  



## Schedule:

The unit consists of two lectures per week in weeks 1-5 and 7-8 (Week 6 is reading week):

    Monday 2-3, PHYS BLDG G12 MOTT
    Thursday 11-12, FRY BLDG LG.02

The exception is week 8, in which there will only be one lecture on the Monday.

The lecture schedule is as follows:

    Weeks 1-3: Majid (6)
    Week 4, Monday: Majid (1)
    Week 4, Thursday: Andrew (1)
    Weeks 5 and 7: Andrew (4)
    Week 8, Monday: Andrew (1)
    Week 8, Thursday: No lecture



## Teams:
* The unit is on [Teams](https://teams.microsoft.com/l/team/19%3An35qiHInXDHOy9VFZwldDwchJNSb7BcvzpLTNPWIX6A1%40thread.tacv2/conversations?groupId=5ebc2a58-b6aa-4600-8422-b28912b2c07b&tenantId=b2e47f30-cd7d-4a4e-a5da-b18cf1a4151b).  You should have access already through the "Teams" panel.  If not, please get in touch with the COMS Student Enquiries Mailbox at coms-student-enquiries@bristol.ac.uk. Please make sure you set NOTIFICATIONS to ON for this channel.

* You should use the Teams channel for raising queries on any aspects of the COMS30030 unit - such queries will not normally be answered via email or via personal Teams messages. Please do not get upset if your issue is not answered by email or Teams when sent on a one-to-one basis. Post your query on the unit's Teams channel for the benefit of others who may have the same query.

---

## MAJOR option

Major option COMS30087 materials

Note that the laboratory sessions for the major option COMS30087 are timetabled to take place in weeks 1-5 and 7-8 on Thursdays at 15:00-17:00 in Queens Building 1.80. The major option assignment will then be done during weeks 9-11.

There are six 2-hour laboratory sessions. Each consists of a task sheet which you are expected to complete during the session. help will be available in the form of 6 post-graduate Teaching Assistants (TAs), all of whom are completing a PhD in image processing or computer vision.

The lab sessions are designed to prepare you for undertaking the assignment in weeks 9-11. You are therefore expected to attend every session, complete the tasks on the lab sheet and make full use of the help available. Solutions to lab sheets will be released following each session (when applicable). The TAs have bveen instructed to be available at all times during each session to offer help and advice. However, it is important that before asking for help you make a serious attempt to understand and complete a task. If you need help, then try to ask specific questions, whether that relates to the theory behind the task or how to implement something. If you find that you are not getting sufficient help from the TAs, then please contact the unit director.

## Labs:
- Week 1 - OpenCV Intro and Image Representation - [Introduction and Mandrill Challenge](https://github.com/cs-uob/COMS30030/tree/main/Lab1-Intro-MandrillChallenge)
- Week 2 - Convolution and Image Filtering -  [Numberplate Challenge](https://github.com/cs-uob/COMS30030/tree/main/Lab2-Number-Plate-Challenge)
- Week 3 - Edge and Hough Transform - [Coin Counter Challenge](https://github.com/cs-uob/COMS30030/tree/main/Lab3-Coin-Counter-Challenge)
- Week 4 - Real-time Object Detection - [Face Detection Challenge](https://github.com/cs-uob/COMS30030/tree/main/Lab4-Face-Detection)
- Week 5 - Stereo I
- Week 7 - Stereo II



---

## MINOR option

Minor option COMS30081 materials

## Exam info:
* The exam is closed-book (so no additional materials are allowed).

---

## Lecture recordings:
All lecture recordings eventually appear on Blackboard a few hours after the event. Click on Re/Play on the left menu bar on the BB course webpage to find them.

## Weekly Unit Materials

#### Week 1: 22/09/2025

  | ------- | ------- |     
  | MM01. Introduction, Image Acquisition | [pdf](https://github.com/cs-uob/COMS30030/tree/main/Slides/MM01-Intro-Acquisition.pdf) | -- |
  | MM02. Image Filtering | [pdf](https://github.com/cs-uob/COMS30030/tree/main/Slides/MM02-Filtering.pdf) |  [online play](https://setosa.io/ev/image-kernels/)|
  | Problem Sheet 01 (Self/Group study) | [pdf](https://github.com/cs-uob/COMS30030/tree/main/ProblemSheets/ProblemSheet-IPCV-MM01.pdf) | -- |
  | Problem Sheet 01 (Solutions) | [pdf](https://github.com/cs-uob/COMS30030/tree/main/ProblemSheets/ProblemSheet-IPCV-MM01-Solutions.pdf)  | -- |

#### Week 2: 29/09/2025

  | ------- | ------- |   ------ |  
  | MM03. Fourier Analysis | [pdf](https://github.com/cs-uob/COMS30030/tree/main/Slides/MM03-Fourier.pdf) | [online play](https://bigwww.epfl.ch/demo/ip/demos/FFT-filtering/) |
  | Problem Sheet 02 (Self/Group study) | [pdf](https://github.com/cs-uob/COMS30030/tree/main/ProblemSheets/ProblemSheet-IPCV-MM02.pdf) | -- |
  | Problem Sheet 02 (Solutions) | [pdf](https://github.com/cs-uob/COMS30030/tree/main/ProblemSheets/ProblemSheet-IPCV-MM02-Solutions.pdf)  | -- |
  | MM04. Edges & Shapes | [pdf](https://github.com/cs-uob/COMS30030/tree/main/Slides/MM04-EdgesShapes.pdf) | [online play](https://www.aber.ac.uk/~dcswww/Dept/Teaching/CourseNotes/current/CS34110/hough.html)  |

#### Week 3: 06/10/2025

  | ------- | ------- | ------ |
  | Problem Sheet 03 (Self/Group study) | [pdf](https://github.com/cs-uob/COMS30030/tree/main/ProblemSheets/ProblemSheet-IPCV-MM03.pdf) |  -- |
  | Problem Sheet 03 (Solutions) | [pdf](https://github.com/cs-uob/COMS30030/tree/main/ProblemSheets/ProblemSheet-IPCV-MM03-Solutions.pdf)| -- |
  | MM05. Segmentation | [pdf](https://github.com/cs-uob/COMS30030/tree/main/Slides/MM05-Segmentation.pdf) | [online play](https://www.naftaliharris.com/blog/visualizing-k-means-clustering/) |
  | MM06. Object Detection  | [pdf](https://github.com/cs-uob/COMS30030/tree/main/Slides/MM06-ObjectDetection.pdf) | -- |

#### Week 4: 13/10/2025

  | ------- | ------- | ------ |
  | MM07. Viola-Jones Face Detection | [pdf](https://github.com/cs-uob/COMS30030/tree/main/Slides/MM07-ViolaJones.pdf) | [online play](https://demo.ipol.im/demo/104/) |
  | Problem Sheet 04 (Self/Group study) | [pdf](https://github.com/cs-uob/COMS30030/tree/main/ProblemSheets/ProblemSheet-IPCV-MM04.pdf) |  
  | AC01. Stereo Lecture 1 | [pdf](https://github.com/cs-uob/COMS30030/tree/main/Slides/COMS30030_2526_stereo_lec1_6up.pdf) | -- |
