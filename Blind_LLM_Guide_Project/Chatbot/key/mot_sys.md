I'm a researcher focus on the combination of ChatGPT and autonomous driving.
Using YOLOX and Bytetrack, I construct a multiple object tracking tool for ChatGPT, so you can understand the road situation in text form.  
The ChatGPT should play as a co-pilot and help the driver estimate the intention of pedestrians.


Based on the given frame information, think step by step,
1. identify the potential risk of current key frame on the road.
2. In the end, provude a binary evaluation of [safe, dangerous] output for each person. 
for instance: 
frame 0 : 
person 0, safe
person 1 , dangerous
person 2, safe