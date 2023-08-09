# Prompt Engineering 



## custum instruction part

```
I'm a researcher focus on the combination of ChatGPT and autonomous driving.
I  construct a tool for ChatGPT, so they can understand the road situation in text form.  The LLM will be able to play as a co-pilot and help the driver estimate the intention of pedestrians. 
```





```
Based on the given frame information, think step by step,
1. summarize current key frame information into nature language
2. identify the potential risk of current key frame on the road.
3. In the end, provide a risk evaluation of [low, medium, high] output for each person. 
for instance: 
frame 0 : 
person 0, low
 person 1 , high
person 2, medium



```

- 



## user starting prompt

```

I now have the following data obtained from video_0194 shot by dashcam. 

- the geometric central positions of people and roads are divided into six parts on average:
  Upper left, upper middle, upper right, lower left, lower middle, lower right
- the angles are measured with respect to the image plane, which serves as a parallel plane to the dashcam lens. Analyzing these angles provides insights into the spatial relationships between the vehicle and pedestrians.  
  - The left most pedestrian is -90 degree, while the right most to be 90, the man in front of the camera is 0 degree

I will upload the key frame file for your analysis 
```

based on th









### json handling

```
{Frame0:{
Time: 0.0s,
Text: {
A crowded urban environment with at least 6 visible pedestrians, all very close to the vehicle, mainly positioned in the middle and left_down sections of the view.
Two identifiable roads are labeled, both in the middle_down area, and several pedestrians are standing on them.
The combination of distances, angles, and bounding boxes offers a multi-dimensional view of the scene, reflecting a mix of positions, orientations, and sizes.
The proximity of multiple pedestrians requires careful attention and navigation, particularly considering the complexity and potential unpredictability of human behavior in such a densely populated space.
}


Pedestrian: {
  Person 0 :{ 3, [x y x y], (xmid,ymid)}
  Person 1 :{ 1, [x y x y], (xmid,ymid), }
  Person 2 :{ 2, [x y x y], (xmid,ymid) }
  },

},
  {Frame1:{
  Time: 0.1s, 
  Text: {
  ...
  }
  
  
  Pedestrian: {
    Person 0 :{ 3, [x y x y], (xmid,ymid)}
    Person 1 :{ 2, [x y x y], (xmid,ymid), }
    Person 2 :{ 2, [x y x y], (xmid,ymid) }
    },

},
  ...
}
```

