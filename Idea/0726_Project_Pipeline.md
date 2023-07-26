# 0726: Project Pipeline
## Intro and feedback 
Today is a bad day, for I may catch a cold, and feeling quite bad these days. However, after spending some valuable time wondering and rethinking my path, I get to recognize the correct path again. 

On 0725 lab meeting, our group firstly seriously considered the whole project pipeline for the final demo and further experiment, which is important and fundamental.

I felt exhausted because I lost passion for a while. However, as the saying goes, a shitty draft is better than any dreamy draft. 
The first goal I should set while I am on a favor, is to get plan set up and resist on it each day. 

It should be acknowledged that research is challenging and unclear, but I should still find the interest in it. Fortunately, while I was taking the shower, I found my "euraka moment".

## Data pipeline
It is data, rather than the programming architecture matters. Because in the end, you only need to deal with data. 

![my hand draft]()
<!-- todo -->
Video -> image sequence --[MYMODEL]-> original data text 
-> parsed text -> LLM -> report text [json format]
-> read by real-time prorgam & eye-tracking job
-> ARHUD generation

Yes, I should consider how to generate the colorful HUD design on the screen. However, it is NOT MY TASK NOW. I should trust my teammate, let them go and do their job. 

The only thing I need to consider: is whether can LLM understand the scene. 

## Project Assumption 
Based on pipeline overview and my experience in MCM, creating necessary assumption is of necesscity to a good outcome. 

1. Ignore time delay, for the module can be deployed by other model 
- DPT depth can be realized by radar sonar
- grounding DINO can be replaced by in-car real time algorithm
- Do DPT only once, save mem

- most important is to prove the functionality of current model  
2. Pretrained experiment
- We are posting to CHI, NOT CVVR!
- Do job dirty, at least it works


## Coding Task 
don't get frustrated when there is no GPU to use. 
Writing code really don't need much. 

### Pedestrian name alignment
[LINUX]
1. continue the ugly diff, let the ret_dict can modify the obj_dict based on bbox
2. refactor detect_road, seperating to necessary part. 
3. write a readme to claim the object tracking model 

### JAAD data
[WIN10]
-  Get hands dirty! Rely on existing dataset is quite important and natural!
- ego car info!
- temperature, weather
- Human bbox tracking as ground truth!
- Refactor the whole code, pull request and update their code!
- read the code before asking gpt, use original human brain

### System Prompt Engineering
[WIN10]
- Enhance the current Chatbot
- View others' design,
- Ask young man to help me! -> wonderful idea
- 


### Random stuff (for next week)
- Update readme?
- 
