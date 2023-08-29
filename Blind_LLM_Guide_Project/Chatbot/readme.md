# Background Info 

### Original TEXT Format

这是上周生成的文字，这周在做人-人对齐的工作，但是没有非常好的输出（服务器被占了， 我没完全跑通数据）

可以看到原始的frame-frame 信息比较冗余，可以写脚本读取并合并相同的内容（比方说P0,P1,P2 在R1,S1上）

- 包含bbox, 更多的有效信息
- 包含depth value [具体的]
- ZQ: 人在边缘的检测

```
INFO of 0001:
road 0 is at middle_down
sidewalk 1 is at left_down
person 0 is at left_down
The [distance,angle] from person 0 to our dashcam is: [medium,None]
person 1 is at left_down
The [distance,angle] from person 1 to our dashcam is: [medium,None]
person 2 is at middle_down
The [distance,angle] from person 2 to our dashcam is: [medium,None]
person 3 is at left_down
The [distance,angle] from person 3 to our dashcam is: [very close,-89.9914061020488]
person 4 is at left_down
The [distance,angle] from person 4 to our dashcam is: [very close,-89.98546767864163]
person 5 is at middle_down
The [distance,angle] from person 5 to our dashcam is: [very close,89.9819186537081]
Person 0 is on the road 0, sidewalk 1
Person 1 is on the road 0, sidewalk 1
Person 2 is on the road 0, sidewalk 1
Person 3 is on the road 0, sidewalk 1
Person 4 is on the road 0, sidewalk 1
Person 5 is on the road 0, sidewalk 1
number of Surface mask, Road&sidewalk, People 's mask, actural people: (6, 2, 6, 14)
Labels: [road 0 0.61, sidewalk 1 0.34]
Person Labels: [person 0 0.76, person 1 0.66, person 2 0.64, person 3 0.59, person 4 0.53, person 5 0.49, person 6 0.48, person 7 0.45, person 8 0.44, person 9 0.35, person 10 0.32, person 11 0.30, person 12 0.26, person 13 0.25]

INFO of 0002:
road 0 is at middle_down
sidewalk 1 is at middle_down
person 0 is at left_down
The [distance,angle] from person 0 to our dashcam is: [close,-89.97957223601979]
person 1 is at right_down
The [distance,angle] from person 1 to our dashcam is: [close,89.97384565008956]
person 2 is at left_down
The [distance,angle] from person 2 to our dashcam is: [close,-89.98345055432092]
person 3 is at left_down
The [distance,angle] from person 3 to our dashcam is: [very close,-89.99239717135345]
person 4 is at right_down
The [distance,angle] from person 4 to our dashcam is: [very close,89.98988228524068]
person 5 is at middle_down
The [distance,angle] from person 5 to our dashcam is: [very close,89.98195300606184]
Person 0 is on the road 0, sidewalk 1
Person 1 is on the road 0, sidewalk 1
Person 2 is on the road 0, sidewalk 1
Person 3 is on the road 0, sidewalk 1
Person 4 is on the road 0, sidewalk 1
Person 5 is on the road 0, sidewalk 1
number of Surface mask, Road&sidewalk, People 's mask, actural people: (6, 2, 6, 19)
Labels: [road 0 0.65, sidewalk 1 0.29]
Person Labels: [person 0 0.81, person 1 0.76, person 2 0.76, person 3 0.73, person 4 0.60, person 5 0.60, person 6 0.58, person 7 0.58, person 8 0.57, person 9 0.55, person 10 0.54, person 11 0.53, person 12 0.53, person 13 0.45, person 14 0.37, person 15 0.29, person 16 0.29, person 17 0.28, person 18 0.27]

INFO of 0003:
road 0 is at middle_down
sidewalk 1 is at left_down
person 0 is at right_down
The [distance,angle] from person 0 to our dashcam is: [close,89.97303327786075]
person 1 is at middle_down
The [distance,angle] from person 1 to our dashcam is: [close,-89.95962486607642]
person 2 is at left_down
The [distance,angle] from person 2 to our dashcam is: [close,-89.98592063141345]
person 3 is at left_down
The [distance,angle] from person 3 to our dashcam is: [very close,-89.99222362568385]
person 4 is at right_down
The [distance,angle] from person 4 to our dashcam is: [very close,89.99033594417592]
person 5 is at right_down
The [distance,angle] from person 5 to our dashcam is: [very close,89.99325181022742]
Person 0 is on the road 0, sidewalk 1
Person 1 is on the road 0, sidewalk 1
Person 2 is on the road 0, sidewalk 1
Person 3 is on the road 0, sidewalk 1
Person 4 is on the road 0, sidewalk 1
Person 5 is on the road 0, sidewalk 1
number of Surface mask, Road&sidewalk, People 's mask, actural people: (6, 2, 6, 19)
Labels: [road 0 0.76, sidewalk 1 0.29]
Person Labels: [person 0 0.80, person 1 0.79, person 2 0.77, person 3 0.76, person 4 0.62, person 5 0.58, person 6 0.58, person 7 0.57, person 8 0.55, person 9 0.54, person 10 0.48, person 11 0.46, person 12 0.45, person 13 0.44, person 14 0.38, person 15 0.36, person 16 0.31, person 17 0.29, person 18 0.28]

INFO of 0004:
road 0 is at middle_down
sidewalk 1 is at left_down
person 0 is at left_down
The [distance,angle] from person 0 to our dashcam is: [close,-89.9865609676287]
person 1 is at middle_down
The [distance,angle] from person 1 to our dashcam is: [close,89.906805367841]
person 2 is at middle_down
The [distance,angle] from person 2 to our dashcam is: [close,89.95318287368713]
person 3 is at left_down
The [distance,angle] from person 3 to our dashcam is: [very close,-89.9922027625112]
person 4 is at right_down
The [distance,angle] from person 4 to our dashcam is: [very close,89.99004660267973]
person 5 is at right_down
The [distance,angle] from person 5 to our dashcam is: [very close,89.99263701131177]
Person 0 is on the road 0, sidewalk 1
Person 1 is on the road 0, sidewalk 1
Person 2 is on the road 0, sidewalk 1
Person 3 is on the road 0, sidewalk 1
Person 4 is on the road 0, sidewalk 1
Person 5 is on the road 0, sidewalk 1
number of Surface mask, Road&sidewalk, People 's mask, actural people: (6, 2, 6, 18)
Labels: [road 0 0.74, sidewalk 1 0.27]
Person Labels: [person 0 0.78, person 1 0.78, person 2 0.77, person 3 0.76, person 4 0.69, person 5 0.66, person 6 0.66, person 7 0.61, person 8 0.60, person 9 0.59, person 10 0.59, person 11 0.58, person 12 0.58, person 13 0.55, person 14 0.50, person 15 0.50, person 16 0.33, person 17 0.33]

INFO of 0005:
road 0 is at middle_down
sidewalk 1 is at left_down
sidewalk 2 is at right_down
person 0 is at left_down
The [distance,angle] from person 0 to our dashcam is: [close,-89.98703889704926]
person 1 is at middle_down
The [distance,angle] from person 1 to our dashcam is: [close,-89.95166737055446]
person 2 is at left_down
The [distance,angle] from person 2 to our dashcam is: [close,-89.98419407662341]
person 3 is at right_down
The [distance,angle] from person 3 to our dashcam is: [very close,89.9910932811934]
person 4 is at right_down
The [distance,angle] from person 4 to our dashcam is: [very close,89.98622152472241]
person 5 is at right_down
The [distance,angle] from person 5 to our dashcam is: [very close,89.9924198755062]
person 6 is at middle_down
The [distance,angle] from person 6 to our dashcam is: [very close,-89.96770024821033]
person 7 is at right_down
The [distance,angle] from person 7 to our dashcam is: [very close,89.99291758410028]
person 8 is at right_down
The [distance,angle] from person 8 to our dashcam is: [very close,89.98972865489513]
Person 0 is on the road 0, sidewalk 1, sidewalk 2
Person 1 is on the road 0, sidewalk 1, sidewalk 2
Person 2 is on the road 0, sidewalk 1, sidewalk 2
Person 3 is on the road 0, sidewalk 1, sidewalk 2
Person 4 is on the road 0, sidewalk 1, sidewalk 2
Person 5 is on the road 0, sidewalk 1, sidewalk 2
Person 6 is on the road 0, sidewalk 1, sidewalk 2
Person 7 is on the road 0, sidewalk 1, sidewalk 2
Person 8 is on the road 0, sidewalk 1, sidewalk 2
number of Surface mask, Road&sidewalk, People 's mask, actural people: (9, 3, 9, 17)
Labels: [road 0 0.76, sidewalk 1 0.29, sidewalk 2 0.25]
Person Labels: [person 0 0.78, person 1 0.77, person 2 0.76, person 3 0.75, person 4 0.67, person 5 0.64, person 6 0.64, person 7 0.59, person 8 0.56, person 9 0.54, person 10 0.48, person 11 0.47, person 12 0.43, person 13 0.43, person 14 0.36, person 15 0.34, person 16 0.27]
```



### JSON format

Generated by ChatGPT-4, the input and output is too long, beyond its IO limit

Try to use it with API later

### Approach 1



```JSON

{
    "frames": [
        {
            "id": "0001",
            "surfaces": {
                "road 0": {"location": "middle_down"},
                "sidewalk 1": {"location": "left_down"}
            },
            "persons": {
                "0": {"location": "left_down", "distanceToCam": "medium", "angleToCam": null, "on": ["road 0", "sidewalk 1"], "label": 0.76},
                "1": {"location": "left_down", "distanceToCam": "medium", "angleToCam": null, "on": ["road 0", "sidewalk 1"], "label": 0.66},
                "2": {"location": "middle_down", "distanceToCam": "medium", "angleToCam": null, "on": ["road 0", "sidewalk 1"], "label": 0.64},
                "3": {"location": "left_down", "distanceToCam": "very close", "angleToCam": -89.9914061020488, "on": ["road 0", "sidewalk 1"], "label": 0.59},
                "4": {"location": "left_down", "distanceToCam": "very close", "angleToCam": -89.98546767864163, "on": ["road 0", "sidewalk 1"], "label": 0.53},
                "5": {"location": "middle_down", "distanceToCam": "very close", "angleToCam": 89.9819186537081, "on": ["road 0", "sidewalk 1"], "label": 0.49}
            },
            "statistics": {
                "surfaceMaskCount": 6,
                "roadAndSidewalkCount": 2,
                "peopleMaskCount": 6,
                "actualPeopleCount": 14
            },
            "labels": {
                "surfaces": {
                    "road 0": 0.61,
                    "sidewalk 1": 0.34
                }
            }
        },
        ...
        {
            "id": "0005",
            "surfaces": {
                "road 0": {"location": "middle_down"},
                "sidewalk 1": {"location": "left_down"},
                "sidewalk 2": {"location": "right_down"}
            },
            "persons": {
                "0": {"location": "left_down", "distanceToCam": "close", "angleToCam": -89.98703889704926, "on": ["road 0", "sidewalk 1", "sidewalk 2"], "label": 0.78},
                "1": {"location": "middle_down", "distanceToCam": "close", "angleToCam": -89.95166737055446, "on": ["road 0", "sidewalk 1", "sidewalk 2"], "label": 0.77},
                "2": {"location": "left_down", "distanceToCam": "close", "angleToCam": -89.98419407662341, "on": ["road 0", "sidewalk 1", "sidewalk 2"], "label": 0.76},
                "3": {"location": "right_down", "distanceToCam": "very close", "angleToCam": 89.9910932811934, "on": ["road 0", "sidewalk 1", "sidewalk 2"], "label": 0.75},
                "4": {"location": "right_down", "distanceToCam": "very close", "angleToCam": 89.98622152472241, "on": ["road 0", "sidewalk 1", "sidewalk 2"], "label": 0.67},
                "5": {"location": "right_down", "distanceToCam": "very close", "angleToCam": 89.9924198755062, "on": ["road 0", "sidewalk 1", "sidewalk 2"], "label": 0.64},
                "6": {"location": "middle_down", "distanceToCam": "very close", "angleToCam": -89.96770024821033, "on": ["road 0", "sidewalk 1", "sidewalk 2"], "label": 0.66},
                "7": {"location": "right_down", "distanceToCam": "very close", "angleToCam": 89.99291758410028, "on": ["road 0", "sidewalk 1", "sidewalk 2"], "label": 0.61},
                "8": {"location": "right_down", "distanceToCam":"very close", "angleToCam":89.98972865489513], "on": ["road 0", "sidewalk 1", "sidewalk 2"], "label": 0.56"}

}

```





###  Approach 2

```JSON
{
    "frames": [
        {
            "frameId": "0001",
            "locations": {
                "road0": "middle_down",
                "sidewalk1": "left_down"
            },
            "people": [
                {
                    "personId": "0",
                    "position": "left_down",
                    "distanceToDashcam": "medium",
                    "angleToDashcam": null,
                    "labels": 0.76,
                    "surfaceMask": "road0",
                    "surfaceMask2": "sidewalk1"
                },
                ...
            ],
            "numMasks": {
                "surfaceMask": 6,
                "roadAndSidewalk": 2,
                "peopleMask": 6,
                "actualPeople": 14
            },
            "labels": {
                "road0": 0.61,
                "sidewalk1": 0.34
            }
        },
        {
            "frameId": "0002",
            "locations": {
                "road0": "middle_down",
                "sidewalk1": "middle_down"
            },
            "people": [
                {
                    "personId": "0",
                    "position": "left_down",
                    "distanceToDashcam": "close",
                    "angleToDashcam": -89.97957223601979,
                    "labels": 0.81,
                    "surfaceMask": "road0",
                    "surfaceMask2": "sidewalk1"
                },
                ...
            ],
            "numMasks": {
                "surfaceMask": 6,
                "roadAndSidewalk": 2,
                "peopleMask": 6,
                "actualPeople": 19
            },
            "labels": {
                "road0": 0.65,
                "sidewalk1": 0.29
            }
        },
        ...
    ]
}
```

## GPT 生成结果

### Video 0310

> GPT4 Online ver, 通过JSON文件输入（以上面两个为例）
>
> https://chat.openai.com/share/4e4eb2fe-bb79-4c51-9af1-a70772b6d8a2

System: Act as the blind copilot, describe the road situation, analyze the complexity of current crossroad, giving the possible potential risk person name.

GPT: Sure, let's take an example from the given JSON format. Suppose we have a scenario as follows:

```text
Frame ID: 1
Locations:
- Crossroad: [200, 300]
People:
- Person ID: 1, position: [180, 290], distance to dashcam: 20 meters
- Person ID: 2, position: [220, 310], distance to dashcam: 25 meters
Number of masks:
- mask_1: 2
- mask_2: 1
Labels:
- Traffic light: green
- Speed limit: 30 km/h
```

Acting as the co-pilot:

We're currently approaching a crossroad, with its center approximately 200 meters eastward and 300 meters northward from our current location. This is a moderate complexity crossroad, given the presence of multiple individuals and traffic conditions.

There are two pedestrians in the vicinity of the crossroad. Person 1 is closer to us, about 20 meters away in the direction slightly left of the crossroad center. Person 2 is slightly further, around 25 meters away and a bit to the right of the crossroad center.

Notably, both pedestrians are wearing masks. Person 1 and Person 2 are wearing mask_1, while Person 2 is additionally wearing mask_2, which may indicate heightened health concerns or increased susceptibility to airborne particles.

In terms of traffic conditions, the light is currently green, indicating we have the right of way. However, we should still exercise caution due to the proximity of pedestrians. The speed limit is 30 km/h, ensuring a safer environment for both vehicles and pedestrians. 

Potential risks include the possibility of either pedestrian stepping into the roadway unexpectedly. Person 1 is particularly a concern due to their closer proximity. Please remain aware of their movements and prepare to adjust speed or direction as necessary. 

Again, while we have the right of way, the presence of pedestrians near the crossroad calls for increased vigilance and slower speeds. As always, safety is our top priority.

### Video 0045

> GPT4 Online ver 以original context data 输入
>
> link 同上

Alright, here's the copilot analysis of the information you provided:

**Frame 0001:** We're at a mid-down section of Road 0 and Road 1. There are five individuals in the vicinity, three of them (Persons 0, 1, and 2) are close to us on the left side of the car, with angles of approximately -90 degrees, suggesting they are practically parallel to us. Their close proximity necessitates caution. All three of these individuals are on Roads 0 and 1. 

The other two people (Persons 3 and 4) are quite far from us, one ahead and one to the right. They are not on any detected surfaces. Persons 0, 1, and 2 are potential risks due to their proximity and location on the roads. The road labels suggest a stronger presence of Road 0.

**Frame 0002:** We're at a mid-down section of Road 0. There are ten individuals detected, with three of them (Persons 0, 1, and 2) in close proximity. Persons 0 and 1 are on our left side, while Person 2 is on the right side. The angles suggest they are parallel to us. All three individuals are on Road 0. Due to their close proximity and presence on the road, Persons 0, 1, and 2 are potential risks.

**Frame 0003:** Again, we're at a mid-down section of Road 0. Seven individuals are present, with three (Persons 0, 1, and 2) being closer to us. Person 0 is to our left and at a medium distance, while Person 2 is closer and also on the left. All three individuals are on Road 0. Person 2 is a potential risk due to their proximity.

**Frame 0004:** We're at a mid-down section of Road 0, with a sidewalk detected to the right. There are eleven individuals detected. Six of them (Persons 0, 1, 2, 3, 4, and 5) are at various distances on the left, middle, and right relative to us. All these individuals are on both Road 0 and Sidewalk 1. The close proximity of Persons 3, 4, and 5 makes them potential risks. 

**Frame 0005:** We're at a mid-down section of Road 0, with a sidewalk detected in the middle. Seven individuals are detected, three of them (Persons 0, 1, and 2) are close and located on our left, middle, and right respectively. All three are on both Road 0 and Sidewalk 1. Persons 0, 1, and 2 are potential risks due to their proximity and presence on the road and sidewalk. The other four individuals (Persons 3, 4, 5, and 6) are further away and not on any detected surfaces.

In all frames, the relative positions of pedestrians and their proximity to the vehicle mean the driver should maintain a lower speed and heightened awareness. The presence of pedestrians on the roads calls for defensive driving and preparation to stop or slow down if necessary.

## S0710

> GPT3.5 turbo 16k
>
> https://chat.openai.com/share/6db37b1a-617f-47d1-9305-4bd96007d246

让他把场景描述转换为 **自然语言** 时，出现了帧数错乱的问题

Frame 0003:
Two roads are visible in the middle and downward direction. There are six people detected, with medium distances and no specific angles from the dashcam. All six people are on both roads. Surface masks indicate six detected objects, including two roads, and six people with a total count of ten individuals. The confidence labels for the roads are 0.49 and 0.44, while for the people, they range from 0.76 to 0.25.

Frame 0001:
Two roads are visible in the middle and downward direction, and a sidewalk is on the left side. There are six people detected, with medium distances and no specific angles from the dashcam. All six people are on both roads and the sidewalk. Surface masks indicate nine detected objects, including three roads and two sidewalks, with a total of nine people. The confidence labels for the roads are 0.44 and 0.42, while for the sidewalk, it is 0.25. The confidence labels for the people range from 0.72 to 0.26.

Frame 0002:
Three roads are visible, one in the middle and two on the right side, and a sidewalk is on the right side as well. There are seven people detected, with medium to close distances and no specific angles from the dashcam. Six people are on the three roads and the sidewalk, while one person is not on any detected surface. Surface masks indicate twelve detected objects, including four roads and one sidewalk, with a total of seven people. The confidence labels for the roads are 0.34, 0.33, and 0.28, while for the sidewalk, it is 0.25. The confidence labels for the people range from 0.51 to 0.26.

Frame 0006:
One road is visible in the middle and downward direction, and a sidewalk is on the right side. There is one person detected, with a medium distance and no specific angle from the dashcam. The person is on both the road and the sidewalk. Surface masks indicate six detected objects, including two roads and one sidewalk, with a total of one person. The confidence labels for the road and sidewalk are 0.41 and 0.25, respectively. The confidence label for the person is 0.82.

Frame 0004:
Two roads are visible in the middle and downward direction. There are four people detected, with medium distances and no specific angles from the dashcam. All four people are on both roads. Surface masks indicate six detected objects, including two roads, with a total of four people. The confidence labels for the roads are 0.49 and 0.30. The confidence labels for the people range from 0.37 to 0.26.

Frame 0005:
Two roads are visible, one in the middle and one on the left side, and two sidewalks are on the right and left sides. There are five people detected, with medium distances and no specific angles from the dashcam. All five people are on both roads and sidewalks. Surface masks indicate fifteen detected objects, including five roads and two sidewalks, with a total of five people. The confidence labels for the roads are 0.36 and 0.36, while for the sidewalks, they are 0.28 and 0.27. The confidence labels for the people range from 0.38 to 0.27.

Frame 0008:
Two roads are visible in the middle and downward direction, and a sidewalk is on the right side. There is one person detected, with a medium distance and no specific angle from the dashcam. The person is on both roads and the sidewalk. Surface masks indicate twelve detected objects, including four roads and one sidewalk, with a total of one person. The confidence labels for the roads are 0.45 and 0.32, while for the sidewalk, it is 0.27. The confidence label for the person is 0.30.

Frame 0007:
One road is visible in the middle and downward direction, and a sidewalk is on the right side. There are two people detected, with medium to far distances and specific angles from the dashcam. Both people are on the road and the sidewalk. Surface masks indicate nine detected objects, including three roads and one sidewalk, with a total of two people. The confidence labels for the road and sidewalk are 0.43 and 0.32, respectively. The confidence labels for the people are 0.35 and 0.27.

Frame 0009:
One sidewalk is visible on the right side, and three roads are visible, one in the middle and two on the right side. There are seven people detected, with medium to close distances and specific angles from the dashcam. Four people are on the sidewalk, two on one road, and one person on another road, while two people are not on any detected surface. Surface masks indicate fifteen detected objects, including five roads and four sidewalks, with a total of seven people. The confidence labels for the sidewalk and roads range from 0.37 to 0.25, while for the people, they range from 0.43 to 0.26.

Frame 0011:
Two roads are visible, one in the right and one in the middle, and two sidewalks are visible, one on the right and one in the middle. There are three people detected, with close to medium distances and specific angles from the dashcam. All three people are on the sidewalk. Surface masks indicate twelve detected objects, including four roads and two sidewalks, with a total of three people. The confidence labels for the roads are 0.43 and 0.33, while for the sidewalks, they are 0.29 and 0.28. The confidence labels for the people range from 0.37 to 0.25.

Frame 0012:
Three roads are visible, one in the middle, one on the left, and one on the right. There are no specific distances or angles for the two people detected. Both people are on the road and the sidewalk. Surface masks indicate nine detected objects, including three roads, with a total of one person. The confidence labels for the roads are 0.52, 0.37, and 0.31. The confidence label for the person is 0.76.

Frame 0010:
One road is visible in the middle and downward direction, and a sidewalk is on the left side. There are three people detected, with medium distances and no specific angles from the dashcam. All three people are on both the road and the sidewalk. Surface masks indicate six detected objects, including two roads, with a total of three people. The confidence labels for the road and sidewalk are 0.57 and 0.47, respectively. The confidence labels for the people range from 0

.74 to 0.25.

I hope these natural and concise summaries of each frame help with your project, Tony. If you need further assistance or have any other questions, feel free to ask!
