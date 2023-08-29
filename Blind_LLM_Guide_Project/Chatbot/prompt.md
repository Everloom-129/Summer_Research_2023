# Prompt Engineering 1.0



## custum instruction part
> system message part [more detail can be seen under key/sys_prompt,md]
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
> user message part [more detail can be seen under key/usr_prompt,md]

```

I now have the following data obtained from video_0194 shot by dashcam. 

- the geometric central positions of people and roads are divided into six parts on average:
  Upper left, upper middle, upper right, lower left, lower middle, lower right
- the angles are measured with respect to the image plane, which serves as a parallel plane to the dashcam lens. Analyzing these angles provides insights into the spatial relationships between the vehicle and pedestrians.  



```

### read raw data from folder

Now I want to collect the vision part information within folder DINOmasked
the processed Info_Video_xxxx.txt is contained in each subfolder, for instance:
- DINOmasked/input/video_0001/Info_Video_0001.txt
- DINOmasked/input/video_0002/Info_Video_0002.txt
OR
- DINOmasked/HZ2/video_0003/Info_Video_0003.txt
- DINOmasked/HZ2/video_0001/Info_Video_0001.txt
etc...
I want to get all these txt and zip into single file named 'Vision_Output_0813.zip', where 0813 is the date of today. Write a script for me


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

非常好，那么让我们处理另外一个问题

我现在需要将另外一个名为：all_video_name.json转化为自然语言，但是我只需要其中每个帧的行人数据，不需要汽车和卡车

转化的方式我希望是首先读取json作为一个dict，之后再写入输出文件



例如：

### frame 0012

people detected: [0 1 5 9]

0 is at [ bbox ], 1 is at [ bbox ], 5 is at [ bbox ] 9 is at [ bbox ]

On right of our car, there are: [0 2 ], 

On the left of our car, there are [5 9 ].

 high confidence list: 0, 1 # bigger than 0.8

low confidence list: 5,9 

### frame 0013

people detected: [0 2 5 9]

0 is at [ bbox ], 2 is at [ bbox ], 5 is at [ bbox ] 9 is at [ bbox ]

On right of our car, there are: [0 2 ], 

On the left of our car, there are [5 9 ].

 high confidence list: 0, 2 # bigger than 0.8

low confidence list: 5,9  # lower than 0.4

你可以从这个代码作为原型

```

def read_and_translate_mot_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            print(filename)
            file_path = os.path.join(input_folder, filename)
            lines = []
            with open(file_path, 'r') as file:
                lines = file.readlines()
            if not lines:
                print(f"no detected obj in current video:{file_path}")
                return
                
            parsed_data = []
            for line in lines:
                frame, object_id, bb_left, bb_top, bb_right, bb_bottom, conf, class_id, _, _ = map(float, line.strip().split(","))
                parsed_data.append({
                    'Frame': int(frame),
                    'Object_ID': int(object_id),
                    'BB_Left': bb_left,
                    'BB_Top': bb_top,
                    'BB_Width': bb_right,
                    'BB_Height': bb_bottom,
                    'Class_ID': int(class_id),
                    'Confidence' : float(conf)
                })
                
            df_mot = pd.DataFrame(parsed_data)
            translated_text = translate_to_natural_language(df_mot)


            output_file_path = os.path.join(output_folder, f"mot_{filename}")
            with open(output_file_path, 'w') as file:
                file.write(translated_text)

read_and_translate_mot_files("./","mot_archive/")
```



