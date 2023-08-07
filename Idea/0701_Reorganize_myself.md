# 0701 Reorganize the terminology and understanding

## Terminology

There exists some unaligned language translation in our project, here I gonna list the correct and official bijection relationship between English and Chinese.(Which is quite important to the prompt engineering!)

| English                            | Chinese          |
| ---------------------------------- | ---------------- |
| curb(also kerb)                    | 马路牙子，路缘石 |
| sidewalk(US) ,pavement(EN) footway | 人行道，小路     |
| road, street                       | 马路             |
| dual carriageway, two-lane road    | 双车道           |
| lane                               | 车道             |
| lane line, road marking            | 车道线           |
| zebra crossing                     | 斑马线           |
| one-way street, one-way road       | 单行线           |
| No Entry sign                      | 禁行标志         |
| rear-end collision                 | 追尾事故         |
| crossing the road or jaywalking    | 横穿马路         |
| drunken man, drunkard              | 醉汉             |
|                                    |                  |
|                                    |                  |



1. 马路牙子, 路缘石 (Mǎlù yázi, lùyuán shí) - These two terms are quite similar, both referring to what's known in English as "curb" or "kerb". 马路牙子 is more colloquial, literally meaning "road teeth", it's a vivid metaphor referring to the raised edge along the road. 路缘石 is more formal and technical, meaning "road edge stone".

2. 人行道, 小路 (Rénxíngdào, xiǎolù) - 人行道 means "sidewalk" or "pavement", a path designated for people to walk along the side of a road. 小路 is a "path" or "lane", a smaller, often more narrow road or track, usually not intended for heavy traffic like main roads.

3. 马路 (Mǎlù) - This word translates directly to "road" or "street" in English. 马路 can refer to any kind of road that vehicles can drive on, but it is most often used to refer to larger, busier roads.

4. 车道 (Chēdào) - 车道 translates to "lane" in English. In the context of roads and transportation, a lane is a part of the road or a track designated for a single line of vehicles. For example, a highway may have multiple 车道 to accommodate heavy traffic.



## Schedule myself

After long conversation with my mentor, I get much deeper understanding on the current task and the method to reorganize the whole pipeline. First of all, is my target during this research month:

### Target

1. 各种方式识别行人是否on the road 准确率，量化
   - grounded SAM : 看看行不行
     - [x] 阅读论文 
     - [ ] 文书总结
   - SAM + grounding DINO: 分析自己组装可行性
2. 看SAM 对道路区域识别准确性（能否区分行车区域和行人区域）

- 视觉 pipeline ，不需要做拆分，保证accuracy 输出

- Pedestrians 落脚点rule 分析是否是road



无标签的情况下：random 后取平均，需要人工肉眼看一下



BEST: road boundary detection( 车道线少的场景)

车道线多的场景 ：车道线检测比较成熟

试试看 SAM + rule based 

目标检测的论文 ! 在找找直接detect road

看他们的图，高被引，有没有detect，

有的话，demo, api, 部署

可行性测试，全局测试





### 总结

多读读论文，多想想，培养科研能力
