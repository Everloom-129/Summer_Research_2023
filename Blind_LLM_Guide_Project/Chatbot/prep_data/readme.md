# Integral Frame Analysis

09/03/2023
How to integrate different llm output together?


```markdown
### frame 0002
people detected: 2,3,4,5,7
2 is at [809.1, 345.3, 828.5, 390.9] 
3 is at [997.6, 340.4, 1019.9, 399.1] 
4 is at [1087.1, 326.4, 1112.3, 392.4] 
5 is at [831.9, 341.6, 849.1, 388.1] 
7 is at [1137.4, 325.5, 1165.6, 405.3] 
On the right of our car, 3,4,7
On the left of our car,2,3,4,5,7
high confidence: 2,3,4,7
low confidence: none 
```

## Todolist

- [ ] 分析，综合出一个比较好的混合分析框架 【30min】
- [ ] 确认好帧率，重新跑程序，测试一下2Hz， 3Hz的差异，效果
- [ ] 写一个提取，重命名的程序【15min】
- [ ] 写一个程序跑代码
- [ ] 放轻松，跑通几个框就可以证明我们的有效性，代码之后可以再分析 【3天】
- [x] 最终交付形式保持不变，因此ok 【done】
- [ ] Prompt 梳理放在附录里 【15min】
- [ ] 运动，周期性拉伸身体 【5 min】
- [ ] 每日20分钟分给代码 


### key frame structure
problem: it's too long

```markdown
INFO of frame 0001:
road 0 is at middle_down
sidewalk 1 is at right_down
sidewalk 2 is at right_down
person 0 is at right_up
The [distance,angle] of person 0 is: [very far,to the right]
person 1 is at right_down
The [distance,angle] of person 1 is: [very far,to the right]
person 2 is at right_up
The [distance,angle] of person 2 is: [very far,to the right]
car 3 is at left_down
<V> car 3 is at [106.77429 332.78278 315.79926 431.91656] <VE> 
car 4 is at middle_down
<V> car 4 is at [395.33957 272.01056 786.4114  574.58813] <VE> 
Person 0 is on the road 0, sidewalk 1, sidewalk 2, his/her bbox is[885.3138  124.45031 920.14496 169.71994]
Person 1 is on the road 0, sidewalk 1, sidewalk 2, his/her bbox is[870.71326 308.15866 932.34875 442.80905]
Person 2 is on the road 0, sidewalk 1, sidewalk 2, his/her bbox is[851.098  305.8598 873.3556 366.9618]

INFO of frame 0002:
road 0 is at middle_down
sidewalk 1 is at right_down
sidewalk 2 is at right_down
sidewalk 3 is at right_down
person 0 is at right_up
The [distance,angle] of person 0 is: [very far,to the right]
car 1 is at left_down
<V> car 1 is at [2.9354095e-01 3.3813638e+02 2.1041583e+02 4.6418906e+02] <VE> 
person 2 is at right_up
The [distance,angle] of person 2 is: [very far,to the right]
person 3 is at right_down
The [distance,angle] of person 3 is: [close,to the right]
Person 0 is on the road 0, sidewalk 1, sidewalk 2, his/her bbox is[886.86926 309.72824 919.254   367.9113 ]
Person 2 is on the road 0, sidewalk 1, sidewalk 2, his/her bbox is[900.85736 117.71495 937.33466 164.52339]
Person 3 is on the sidewalk 3, his/her bbox is[ 932.44434  310.22064 1010.20044  447.78735]
```

```

### frame 1 to 5
people detected: 2,3,4,5,7
high conf: 2,3,4,7
low conf: none 
### On left sidewalk 
2 is moving from near right to near left quickly
3 is moving backward quickly
4 is moving left slowly
5 is moving right quickly
7 is standing alone

### on the right sidewalk
3,4,7
On the left of our car,2,3,4,5,7

```





灵：像是有一个蜘蛛在信息之网上爬行

思考 key 的排布方式


| ------              | -----                | ------               |
| ------------------- | -------------------- | -------------------- |
| interval frame 0-14 | interval frame 15-29 | interval frame 30-34 |
|                     |                      |                      |
|                     |                      |                      |
|                     |                      |                      |