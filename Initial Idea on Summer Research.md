# 结合大规模语言模型的智能汽车安全预警

王杰

2023年6月1日

## 背景

在人机共驾场景中利用大规模语言模型实现风险检测与安全预警。

- 可选，非必要条件：了解或应用过自动驾驶领域相关算法，如计算机视觉、多模态等相关算法

- 可延长，不可线上

- 专业技能：Python, C/C++, x86, GPT-4, ROS, Carla



## 对暑研的想法和期望

具体的项目认识比较浅显，比较粗糙的记录在下面了

- 直白来讲：个人期望是希望做有关LLM + 自动驾驶的研究，然后能在大四上时参与工作发paper好用于申请美研

- 兴趣上来看，个人对自动驾驶比较看好，兴趣浓厚希望未来能投身相关事业，因此也想借暑研的机会提前准备知识

- 自动驾驶最难搞的就是各种稀奇古怪的corner case，而LLM可以做到few shot learning的能力还是很令人惊叹的

  - 需要算法能自行分析新的情况，并且做出 **符合普通人常识**的应对策略

  - 不存在100%完美的驾驶，但可以避免穷举，利用推理去分析新的问题

    

    **做结合llm能力的算法，应用点是交互系统**



## 项目认识：

面对复杂的驾驶环境，传统的自动驾驶算法如RL等可能难以完全实现安全的自动驾驶，但是在LLM 多模态的常识推理能力辅助下，有可能实现真正的L4自动驾驶

- 面对复杂的驾驶环境，传统的自动驾驶算法可能难以完全实现安全的路线规划。多种corner case 如鬼探头等是极难完美预计的，但是在LLM 多模态的常识推理能力辅助下，或许可以实现zero-shot learning, 规避更多复杂的情况。
- 考虑到现有的LLM以文本处理为本，或许需要实现一些将图像信息转化为文本信息的tool。
- 同时，手机导航的提示信息也可以在LLM的加持下有更好的效果，比如高速路上对事故可能性的实时分析，结合天气系统等进行个性化的预测与提示。

因此，我认为这个项目或许需要以下资源：
- 多模态数据集：对于自动驾驶系统，最常见的输入数据通常来自雷达、激光雷达(LiDAR)、摄像头等设备。这些设备提供了丰富的环境信息，包括但不限于交通信号、行人、车辆、路线等。因此，我们需要一套高质量的多模态数据集作为模型训练和验证的基础。这点或许可以先从Waymo等开源数据集先试着分析，再结合国内实际情况考虑

- LLM 训练资源：如果是finetuning训练一个大规模的语言模型需要强大的计算能力，包括但不限于大量的GPU或TPU资源，以及足够的存储空间
  而通过API的方式或许可以利用向量数据库的形式呈现更高效的信息反馈
- 图像转文本工具：由于现有的LLM主要以处理文本为主，我们需要工具将视觉信息转化为文本描述，或者开发新的模型，使LLM能够直接处理视觉输入、

### [多模态](https://www.zhihu.com/column/c_1145035792891166720)

目前GPT4看report可以处理visual input, 但是目前依旧尚未发布试用，目前的plugins 也多是基于文本输入交互，本质上仍是text based model。

比较常见的思路跟 **项目认识** 部分大致相同：级联不同的模型，用LLM去驱动其他的AI模型，因为LLM具有推理能力，可以更合理的快速设置模型参数及效果

但问题在于，类似AutoGPT的实现方式无法越过所有的“common sense problem”，比方说LLM可能因为依赖库有问题而陷入local optimum, 局部纠结浪费大量算力。 同时，也无法验证LLM推理结果的ground truth。若要进行监督学习，或许可以参考这篇语言转化的多模态分析： [SpeechGPT: Empowering Large Language Models with Intrinsic Cross-Modal Conversational Abilities](https://arxiv.org/pdf/2305.11000.pdf)

> The paper introduces SpeechGPT, a large language model with **intrinsic cross-modal conversational abilities,** capable of perceiving and generating multi-modal content. The model performs **speech discretization with a self-supervised trained speech model to unify the modality between speech and text.** The discrete speech tokens are then expanded into the vocabulary of the large language model (LLM), thus endowing the model with an inherent competence to perceive and generate speech.
>
> The paper also presents the first speech-text cross-modal instruction-following dataset, SpeechInstruct. This dataset is used to provide the model with the capacity to handle multi-modal instructions. The authors construct hundreds of instructions for diverse tasks with GPT-4 to simulate actual user instructions.
>
> SpeechGPT undergoes a three-stage training process: modality-adaptation pre-training, cross-modal instruction fine-tuning, and chain-of-modality instruction fine-tuning. The first stage enables speech comprehension for SpeechGPT with the discrete speech unit continuation task. The second stage employs the SpeechInstruct to improve the model’s cross-modal capabilities. The third stage utilizes parameter-efficient LoRA (Hu et al., 2021) fine-tuning for further modality alignment.
>
> The effectiveness of SpeechGPT is evaluated through a wide range of human evaluations and case analyses to estimate the performance of SpeechGPT on textual tasks, speech-text cross-modal tasks, and spoken dialogue tasks. The results demonstrate that SpeechGPT exhibits a strong ability for unimodal and cross-modal instruction following tasks as well as spoken dialogue tasks.
>
> The authors' contributions include the construction and release of SpeechInstruct, the first large-scale speech-text cross-modal instruction-following dataset, and the development of the first multi-modal large language model that can perceive and generate multi-modal contents.

值得思考的是，能否用类似finetuning的方式，直接微调图像等其他维度输入的效果？考虑到LLM的token 是离散化的，很难做到比较理想的效果，不知道OpenAI究竟如何实现visual GPT的， 难不成是直接训练大量的图像文本数据？（毕竟那些Dataset里包含的文章应该是含有图片的）

- [ ] 调查：OpenAI训练的pipeline, 思考与多模态的关系
- [ ] 阅读相关论文

参考：

[多模态系列-LLM - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/614152221)

**“利用LLM作为理解中枢调用多模态模型”**可以方便快捷地基于LLM部署一个多模态理解和生成系统，难点主要在于prompt engineering的设计来调度不同的多模态模型；

*这是比较符合本次暑研的，基于提示词工程的情况下，可以比较轻松的实现一些推理工作，但上限并不高*

**“将视觉转化为文本，作为LLM的输入”**和“**利用视觉模态影响LLM的解码”**可以直接利用LLM做一些多模态任务，但是可能上限较低，其表现依赖于外部多模态模型的能力；

**“训练视觉编码器等额外结构以适配LLM”**具有更高的研究价值，因为其具备将任意模态融入LLM，实现真正意义多模态模型的潜力，其难点在于如何实现较强的in-context learning的能力。

[利用LLM做多模态任务 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/616351346)

> mPLUG-Owl, MiniGPT4, LLaVA三篇工作的目标都是希望在已有LLM的基础上，通过较少的训练代价达到GPT4技术报告中所展示多模态理解效果。他们都证明第一阶段的**图文预训练对于建立图文之间的联系十分关键**，第二阶段的**多模态指令微调对于模型理解指令以及生成详细的回复十分必要**。三个工作都通过样例展示了不错的效果，**mPLUG-Owl进一步构建一个公平比较的多模态指令评测集**，虽然还不够完善（例如测试指令数量还不够多，依赖人工评测等），但也是为了该领域标准化发展的一个探索和尝试。

## Corner Case 问题

边缘场景不只是多RL就能解决的，长尾效应导致需要考虑的因素实在太多了



1. 极端天气条件：例如，大雾、雪、冰雹、暴风雨等天气条件可能会严重影响传感器的性能，使得自动驾驶车辆难以识别周围环境。

2. 低照度或夜间驾驶：在夜间或低照度条件下，自动驾驶车辆需要能够通过其传感器有效地检测和识别路面上的障碍物。

3. 不规则交通规则：比如，临时道路工程、警察手势指挥或者交通事故等情况都可能导致交通规则的临时改变。

4. 与行人和非机动车辆的互动：例如，行人突然冲出人行道，自行车和摩托车驶入车道，或者遇到动物穿越道路。

5. 高速驾驶和复杂的交通环境：例如，在高速公路上，自动驾驶车辆需要处理高速行驶中的车辆更替和合流等问题；在城市环境中，车辆需要处理交通拥堵、复杂的交叉口和大量的行人和骑行者。

6. 道路标记模糊或缺失：当路面的标记模糊或者缺失时，自动驾驶车辆可能会难以正确识别驾驶轨迹。

7. GPS或其他传感器信号丢失或干扰：例如，在隧道、大楼下或其他导致信号干扰的地方，自动驾驶车辆可能需要依赖其他传感器或预先存储的地图数据来导航。




### Q： 假设在不考虑联网延迟，计算机处理性能的情况下，一台搭载了LLM作为推理内核的CAV，能否做到L4级的自动驾驶？

[Edge Cases in Autonomous Vehicle Production (datagen.tech)](https://datagen.tech/blog/how-synthetic-data-addresses-edge-cases-in-production/)

[自动驾驶中的边缘场景（corner case） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/545395724)

TODO， 查找有没有相关的论文证明可行性

虽然都说是比较热门的可能路径，但是并没有例子或者可靠的论证



## 幻觉问题

LLM虽然具有强大的处理和理解语言的能力，但也存在着误解和错误推理的可能性。这在普通的对话场景中可能只会导致混淆或不准确的回答，但在自动驾驶这样的安全至关重要的环境中，可能会引发严重的安全问题。

- 例如，在需要提示如何切换车道时，错误理解成如何切换音频，导致错过高速出口等
- 或者，幻觉认为前面的应急车道是正确的更优路径，LLM干预导航算法导致车辆冲上错误车道

1. **词汇歧义**：在您的第一个例子中，"切换"这个词在不同的上下文中可能有不同的含义。LLM可能无法完全理解上下文，错误地将"切换车道"理解为"切换音频"。为了解决这个问题，我们可能需要对LLM进行更多的上下文敏感训练，或者使用更准确、无歧义的词汇。
2. **错误的路径推理**：LLM可能误认为应急车道是一个有效的驾驶路径。这可能是因为LLM缺乏对交通规则和驾驶规范的理解，或者在处理多模态数据（如图像、雷达和激光雷达数据）时出现错误。解决这个问题可能需要更强大的多模态数据处理能力，以及更全面的交通规则和驾驶规范训练。
3. **系统交互问题**：在LLM被集成到车机系统进行实际操作时，可能会出现新的问题。例如，LLM可能无法正确理解或执行如"调整仪表盘亮度"或"关闭车窗"等指令。解决这个问题可能需要更好的系统集成，以及对LLM进行更多的特定任务训练。
4. **系统混乱**：LLM的错误操作或误导可能导致车载系统出现混乱，例如频繁无效的切换操作，引起系统资源的浪费。
5. **增加驾驶员压力**：如果驾驶员需要频繁地纠正LLM的错误决策或操作，这可能增加驾驶员的压力和疲劳，甚至影响驾驶员的注意力。
6. **信任度下降**：如果LLM频繁出现幻觉问题，用户可能会对其产生怀疑，导致对自动驾驶系统的信任度下降。
7. **法律责任**：在某些情况下，LLM的错误决策或操作可能引起法律责任问题，例如导致交通事故或违反交通规则。
8. **破坏品牌形象**：频繁的幻觉问题可能破坏车辆制造商的品牌形象，导致销售下滑或客户流失。

如果只是语音助手或许没有太大危害，但是若需要接入车机交互系统，比方说控制仪表盘亮度，控制车窗关闭，则可能引起不必要的麻烦

系统包装了LLM的情况下变得更复杂而不稳定

## 模拟环境

在训练LLM用于自动驾驶系统时，仿真是基础

假设使用我比较熟悉的Carla搭建平台，有几个问题：

- 人机交互需要考虑的是车内驾驶员视角，Carla略去了这个问题
  - 但是游戏：欧洲卡车模拟似乎可以做到非常强大的仿真。。。
- 似乎不能考虑GPS干扰，卡尔曼滤波等问题

### 游戏作为模拟环境有什么问题

- 对具体实验需要，比如要记录的物理量（转向角航向角）难以提取
- 以及要设置的交通事件（比如旁车并道，几辆车，在哪儿生成在哪儿并
- 地图的可编辑性，可以内置的自动驾驶的算法
- 和一般专门做赛车游戏的侧重点不同，欧卡游戏真实性可能更高点，但是可编辑性和数据可记录性会差一些

GPT的建议：

1. **创建逼真的驾驶环境**：仿真环境应尽可能地模拟真实世界的驾驶环境，包括各种天气条件、路况、车流以及各种意外情况。这有助于模型更好地理解和应对实际驾驶中可能遇到的各种复杂情况。

2. **利用多模态数据**：在仿真环境中，我们可以生成和收集各种模态的数据，包括视觉、雷达、激光雷达、GPS等。通过对这些多模态数据的处理和理解，LLM可以更好地理解和描述车辆的周围环境，进行更准确的决策。

3. **进行边缘案例的训练**：在仿真环境中，我们可以反复模拟各种边缘案例，如临时的路线变更、突发的道路障碍等。这些情况在真实世界中可能很难遇到，但在仿真环境中，我们可以通过大量的重复和变异，训练模型对这些边缘案例有更好的理解和应对。

4. **进行幻觉问题的训练**：通过在仿真环境中插入各种可能的幻觉问题，我们可以训练模型识别和处理这些问题，从而提高其在实际驾驶中的稳定性和可靠性。

5. **进行持续的反馈和优化**：在仿真环境中，我们可以获取模型的详细性能数据，包括正确率、错误率、响应时间等。通过这些数据，我们可以持续地对模型进行反馈和优化，使其在实际驾驶中达到最佳性能。

