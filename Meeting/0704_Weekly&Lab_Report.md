# 0704 Weekly Report + 组会

## Dataset 

### JAAD

video clips的形式，数据集聚焦在人车交互的behavior 上

1. - [ ] python script: 
     - [x] 秒级分割clips，
     - [x] 随机选取一部分用于初步测试
     - [x] 分类视频：短中长，
       - [ ] 黑夜，雨天等场景
2. - [ ] JAAD2.0: 自带的一个Label工具，用起来“高度定制化”
     - [x] paper reading and usage understanding
     - [ ] 视频标注
3. 缺点：segment 之后看不清楚了，像素太低

#### Info

noting some of the clips are consective, well the length is unrelated to the id

- short(0~5s): 99 
- median(6~10s): 199
- long(11s+): 54

​	based on short + id343 clips: 共100个视频

  - 清晰车道线  	25%
  - 不清晰车道线  28%
  - 只有斑马线/马路牙子 27 % (以我的理解能力为基准) 
  - 没有明确界限 20% (雪天，雨天，天黑，地下车库场景等) -> 建议先不使用，视觉难度过大

### New dataset

1. A Dataset of Synthetic Images of Outdoor Scenes Taken from Sidewalks, for Temporal Semantic Segmentation Applications

   https://zenodo.org/record/6802655#.YuGrnRzP1Ea

   比较大（46G）用carla搭的，会比较清晰，有标注道路类别，备选

2. 

## SAM(building code)

- [x] Implementation
- [x] python script pipeline seg images

similar project :

[license_plate_recognition/grounded_sam_plate.py at main · ZhengJun-AI/license_plate_recognition · GitHub](https://github.com/ZhengJun-AI/license_plate_recognition/blob/main/grounded_sam_plate.py)

Based on his pipeline, I construct a tool using 

- [ ] DINO + Seg to find the road and people

#### Architecture:

1. dino find road √ （Regieon of interest)

2. use road's bbox as prompt to use SAM

   text: person, sidewalk, road, vehicle

3. rule base 

   - comparing pixel relationship betweeen person and road, sidewalk
   - other VQA method to generate text

4. analyze image sequence, predict behavior

   - question: can I try LLM to do this?
     - 一些想法，之后会议解释

5. overall must use video & image





## Other's focus on sidewalk

1. online model, 一个小数据集，用B4 微调的，效果较差

https://huggingface.co/nickmuchi/segformer-b4-finetuned-segments-sidewalk

2. 读了好几篇论文，都没有source code 的情况
3. github 关键词: sidewalk segementation, 7个repository 都试过，无效
4. 分析了一下原因，可能是因为都是2021年前的工作，当时没有“大模型”的概念，zeroshot 泛化能力比较弱，不能很好应对没处理过的情况

## Course & Reading

1. Complete ChatGPT Prompt Engineering for Developers
2. Read and study some basic model in CV and Mult-Modality field
3. 



## Lab Meeting Record

> Some insightful idea heard in meeting

### 日常

1. 内部资料保密，present需要小心
2. 鼓励小组配人，避坑（所以不承诺挂名，之前出过事故）
3. 预期：时间，投入，产出
4. 4L有一个空间，工作效率提高

### 驾驶

1. 如何描述驾驶中的风险

2. ADHD是一个比较有趣的方向

   - 其实有一个点，自动驾驶之后大家都容易注意力涣散

   - 注意力不一定是眼动，可能是别的方向
   - 场景的聚焦？Context Problem Solution

3. CHI paper ! 得考虑合作问题

4. Q: hardware input and output? 两个如果merge在一起怎么办

   A: CHI 只要不超过时代就好

   - 提出没人做的
   - 提出新的想法
   - 改进现有想法

   

   


## Other

1. AI agent

   sounds really interesting, similar to Voyager task I read these days

   https://lilianweng.github.io/posts/2023-06-23-agent/