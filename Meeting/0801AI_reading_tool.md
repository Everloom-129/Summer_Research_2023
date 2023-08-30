之所以有“技巧“，或者prompt engineering, 本质上是因为当今的LLM输出能力是有限的，我们需要用合适的方式，以coding的思维去获得更好的结果。我们在使用这些乃至所有GPT-based 工具时，其实只需要记住一些基本原则就好：

#### LLM本质缺陷/shortcoming

- 脑容量有限，in-context learning可以记忆的短时记忆很少（约5k token）
  - 1 token ~= 1 word / character eg: "I have a pen" => 4 token
- 对于”非常识“的逻辑推理会比较困难，可能需要提前对应
  - 比方说，”熊喜欢吃蜂蜜，你手上有蜂蜜，所以熊可能会__“ => ”来追你“
  - 但是如果经过抽象：”A like to do B, C have a B, then A might___” => "???"
  - 论文中的缩写，都是新概念，很可能会



- ChatGPT4_Plugin: 付费，但论文阅读效果比较粗糙



| 避免AI在阅读文献时出现的幻觉（hallucination）问题            | “一种减少幻觉的策略是先要求模型获取来源于该文本的所有引用信息（任何相关引用，any relevant quotes），然后要求它基于所引用的信息来回答问题，这使得我们能根据答案追溯源文档，通常对减少幻觉非常有帮助” | Conclude the paper's experimental design: you should find the corresponding content from the paper and use quotes to answer. |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 总结文字太长，阅读困难                                       | 限制输出的总字数                                             | Your answer should be less than 100 words.                   |
| 希望更规范的输出，避免”为了方便我阅读轮文，我需要阅读更多的论文“ | 改变输出的格式注意一定程度上，现行的gpt针对markdown语法有刻意pretrain 和 finetuning, 输出的逻辑和整齐度会更好 | Print the answer in a list.Or markdown formatOr json format  |
| 希望将当前总结的内容制表，方便记录笔记/ 展示给他人           | Markdown语法渲染建议学习一点这种轻量级的渲染语言，非常强大的格式支持可以生成泳道图, 流程图等Ask gpt to generate a mei | Print the answer in a table. *: sider可以输出表格，但没有内置Markdown 语法渲染。但ChatGPT可以；也可以考虑把结果复制粘贴到如Typora 等markdown 阅读器里 |
| 复杂任务：例如，需要从全文范围对某个内容进行提取，总结，并以清晰的方式展现 | 给AI思考的时间：Do it in steps可以让AI先自己提出一个100字的论文阅读框架，然后根据框架再去分析文章内容 | 目的：希望总结出完整的实验计划，包括实验的设计、收集的数据及对应的评估方法Prompt示例： I want you to conclude the complete experimental design for me, and do the task in the steps: Step 1: Find the content about experimental design, specifically, the steps of the experiment, the data collected from the experiment, and the analysis methods used  for the data; Step 2: Arrange the result of step 1, including the steps, data, and analysis methods corresponding to each other; Step 3: Print the result in the table. The columns should be step, data, and analysis methods |







| 类别     | 角色           | 用户类型 | 使用方式                         |
| -------- | -------------- | -------- | -------------------------------- |
| 游戏角色 | 角色           | 专业用户 | 游戏内NPC, AI配配音NPC角色制作   |
| 游戏角色 | 角色           | 普通玩家 | 角色自拟角色Bot玩法测试          |
| 怪物BOSS | 8055           | 专业用户 | AI怪物BOSS怪物8055               |
| 怪物BOSS | 8055           | 普通玩家 | 怪物8055自R                      |
| 道具     | 道具/武器/装甲 | 专业用户 | RI道风生成游戏研发道具/武器/装甲 |
| 道具     | 道具/武器/装甲 | 普通玩家 | AI道风自院                       |
| 地图     | 地图/家材      | 专业用户 | 游戏内地图/家材地图/家材         |
| 地图     | 地图/家材      | 普通玩家 | 地图/素材自拟                    |
| ………      | ……             | ……       | ………                              |