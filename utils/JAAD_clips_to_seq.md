# Transform JAAD Clips into Image Sequence

JAAD is a dataset for studying joint attention in the context of autonomous driving. The focus is on pedestrian and driver behaviors at the point of crossing and factors that influence them. To this end, JAAD dataset provides a richly annotated collection of 346 short video clips (5-10 sec long) extracted from over 240 hours of driving footage. These videos filmed in several locations in North America and Eastern Europe represent scenes typical for everyday urban driving in various weather conditions.

## Task

In window 10 system, based on the following input and output requirement, write a python program to Transform JAAD Clips into Image Sequence divide by seconds. 

For example: 

- 10.2s clips transform into 10 images

- 7.7s clips transform into 7 images

## Input

a series of mp4 form video clips named "video_0xxx", from 0001 to 0346. 

- the code should be flexible to match different mode, with single video 

## Output

the image should be stored in ".\output\video_0xxx", a folder holding corresponding image sequence.

- the program should create the folder automatically if there is no folder, otherwise it should append in the folder