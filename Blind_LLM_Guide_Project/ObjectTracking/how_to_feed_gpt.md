# how to feed gpt with object tracking data

王杰

2023年8月26日

### proceedure

0. 视频分成很多段，以150 帧（5s)为单位为一个batch

1. 把数据交给gpt, 让他用自然语言描述视频（给它几个例子）
2. 每个描述拼接在一起，在5s前让GPT判断这5s中最可能有危险的id
3. 每5s执行一次，获得一系列 数字id, 输入给zq他们做风险判断



## 自然语言描述部分

这个部分也可以用GPT提供的算法实现

```prompt
I want you to do MOT 2D challenge format translation 

The file format contain one object instance per line. Each line must contain 10 values: ``` <frame>, <id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <-1>, <-1>, <-1> ``` The `conf` value contains the detection confidence in the `det.txt` files.  The world coordinates `x,y,z` are ignored for the 2D challenge and are filled with -1, All frame numbers, target IDs and bounding boxes are 1-based.

Here is an example from video_0001.txt: 0,1,831.32,311.15,76.97,151.58,0.84,-1,-1,-1 0,2,805.86,309.67,27.24,62.76,0.80,-1,-1,-1 1,1,831.83,310.38,80.06,157.74,0.86,-1,-1,-1 

this means:
At frame 0, person 1 is at [831.32,311.15,76.97,151.58] 

person 2 is at [805.86,309.67,27.24,62.76,0.80]

At frame 1, person 1 is at [831.83,310.38,80.06,157.74]



translate user's input into natural language, you must include all the person id in the sentence. 

for example:

{{{0,1,129.23,237.29,49.44,91.33,0.70,-1,-1,-1 2,2,732.14,244.04,35.88,81.15,0.63,-1,-1,-1 3,2,731.76,245.35,34.97,79.06,0.61,-1,-1,-1 4,2,731.64,244.84,35.63,80.48,0.65,-1,-1,-1}}}

can be transfered into 

{{{At frame 0, person 1 is located at coordinates [129.23, 237.29] with a bounding box of width 49.44 and height 91.33, and a detection confidence of 0.70.

At frame 2, person 2 is located at coordinates [732.14, 244.04] with a bounding box of width 35.88 and height 81.15, and a detection confidence of 0.63.

At frame 3, person 2 is located at coordinates [731.76, 245.35] with a bounding box of width 34.97 and height 79.06, and a detection confidence of 0.61.

At frame 4, person 2 is located at coordinates [731.64, 244.84] with a bounding box of width 35.63 and height 80.48, and a detection confidence of 0.65.}}}
```



例子

```
- At frame 0, person 1 is located at coordinates [129.23, 237.29] with a bounding box of width 49.44 and height 91.33, and a detection confidence of 0.70.
- At frame 2, person 2 is located at coordinates [732.14, 244.04] with a bounding box of width 35.88 and height 81.15, and a detection confidence of 0.63.
- At frame 3, person 2 is located at coordinates [731.76, 245.35] with a bounding box of width 34.97 and height 79.06, and a detection confidence of 0.61.
- At frame 4, person 2 is located at coordinates [731.64, 244.84] with a bounding box of width 35.63 and height 80.48, and a detection confidence of 0.65.
- At frame 5, person 2 is located at coordinates [731.64, 245.65] with a bounding box of width 35.78 and height 80.84, and a detection confidence of 0.55.
- At frame 6, person 2 is located at coordinates [731.76, 246.02] with a bounding box of width 35.59 and height 80.43, and a detection confidence of 0.56.
- At frame 21, person 2 is located at coordinates [731.42, 250.28] with a bounding box of width 34.05 and height 78.13, and a detection confidence of 0.28.
- At frame 22, person 2 is located at coordinates [730.79, 250.63] with a bounding box of width 33.66 and height 77.61, and a detection confidence of 0.14.
- At frame 23, person 2 is located at coordinates [731.00, 251.43] with a bounding box of width 34.20 and height 78.89, and a detection confidence of 0.33.
- At frame 24, person 2 is located at coordinates [731.69, 251.52] with a bounding box of width 34.75 and height 80.35, and a detection confidence of 0.36.
- At frame 25, person 2 is located at coordinates [730.55, 250.38] with a bounding box of width 35.43 and height 82.26, and a detection confidence of 0.52.
```





## 问题行人分析部分

### custom instruction

#### role

```
I'm a researcher focus on the combination of ChatGPT and autonomous driving.

I  construct a tool for ChatGPT, so they can understand the road situation in text form.  The LLM will be able to play as a co-pilot and help the driver estimate the most dangerous pedestrian in current section
```

### task

```prompt
Based on the given frame information, think step by step,


1. identify the potential risk of current key frame on the road.

2. provide a risk evaluation of [low, medium, high] output for each person. 

for instance: 

frame 0 : 
person 0, low
person 1 , high
person 2, medium


```

效果：

```
To evaluate the risk, we should consider factors like movement direction, speed, and distance to the road, although some of these factors are not provided in your dataset. But based on the given data (coordinates and bounding box sizes), we can make a rough risk assessment.

#### Observations:

- **Person 1**: The coordinates suggest that the person is moving generally in the positive X-direction, which could mean they are moving away from or parallel to the road. The bounding box is increasing in both width and height, suggesting the person might be coming closer to the camera or simply standing up or expanding their posture.
  
- **Person 2**: The coordinates suggest that the person is generally stationary or slowly moving in the negative X and Y-direction. The bounding box fluctuates but does not show significant change, indicating that the person's distance from the camera is relatively constant.

#### Risk Evaluations:

- **Frame 0**:
  - Person 1: Low
  - Person 2: Low

- **Frame 1**:
  - Person 1: Low
  - Person 2: Low

- **Frame 5**:
  - Person 1: Low
  - Person 2: Low
  
- **Frame 10**:
  - Person 1: Low
  - Person 2: Low
  
- **Frame 15**:
  - Person 1: Medium (The bounding box size is increasing more rapidly)
  - Person 2: Low

- **Frame 20**:
  - Person 1: Medium
  - Person 2: Low

- **Frame 25**:
  - Person 1: High (The bounding box is quite large, and the person has moved significantly in the X-direction)
  - Person 2: Low

The risk level for Person 1 gradually increases to High by Frame 25 as they are moving and their bounding box is enlarging (which could indicate they are moving towards the road). Person 2 remains at Low risk throughout the frames as they appear relatively stationary and show less variation in the bounding box dimensions.
```

使用方法：

打开Custom instruction, 设置好role 和task
之后丢数据就好（GPT处理好的数据）

- [ ] 五秒间隔那个我还没想好怎么实现，过1h给你们

