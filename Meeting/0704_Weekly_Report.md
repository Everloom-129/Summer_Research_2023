# 0704 Weekly Report

## Dataset 

### JAAD

video clips的形式，数据集聚焦在人车交互的behavior 上

1. - [ ] python script: 
     - [x] 秒级分割clips，
     - [x] 随机选取一部分用于初步测试
     - [ ] 分类视频：短中长，黑夜，雨天等场景
2. - [ ] JAAD2.0: 自带的一个Label工具，用起来“高度定制化”
     - [x] paper reading and usage understanding
     - [ ] 视频标注
3. 缺点：segment 之后看不清楚了，像素太低



### New dataset

1. A Dataset of Synthetic Images of Outdoor Scenes Taken from Sidewalks, for Temporal Semantic Segmentation Applications

   https://zenodo.org/record/6802655#.YuGrnRzP1Ea

   比较大（46G）用carla搭的，会比较清晰，有标注道路类别，备选

2. 

## SAM

- [x] Implementation
- [x] python script pipeline seg images
- [ ] 