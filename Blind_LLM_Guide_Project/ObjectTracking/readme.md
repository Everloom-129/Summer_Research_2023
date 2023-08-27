# Object tracking module

How do we realize mix-precision analysis in driving scenario?

- [x] car following
- [x] video folder output
- [ ] run the program with bash again
- [x] txt -> json
- [x] confirm MOT form
- [x] Try aot tracking
  - [x] mask based, hard to adopt into our task
- [ ] merge workflow into other module
  - [ ] selective input for data?
  - [ ] how to let gpt understand current scene?
  - [ ] person id is most important




HZ

> **track_id, current frame bounding box and confidence score**. The original implementation only tracks humans, and hence is class agnostic.

> MOT 2D challenge
>
> The file format contain one object instance per line. Each line must contain 10 values:
>
> ```
> <frame>, <id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <-1>, <-1>, <-1>
> ```
>
> The `conf` value contains the detection confidence in the `det.txt` files. 
>
> The world coordinates `x,y,z` are ignored for the 2D challenge and can be filled with -1,
>
> 
>
> All frame numbers, target IDs and bounding boxes are 1-based. Here is an example from b1c9c847-3bda4659.txt:
>
> 0,1,831.32,311.15,76.97,151.58,0.84,-1,-1,-1
> 0,2,805.86,309.67,27.24,62.76,0.80,-1,-1,-1
> 1,1,831.83,310.38,80.06,157.74,0.86,-1,-1,-1
> 1,2,811.74,309.93,26.78,61.74,0.81,-1,-1,-1
> 2,1,833.53,309.79,80.09,157.90,0.86,-1,-1,-1



format commonly used in Multi-Object Tracking (MOT) benchmarks, especially the MOTChallenge format. Each row represents an object's state in a particular frame.

Here's a breakdown of the encoding:

1. **Frame Number**: The first column denotes the frame number. This tells you in which frame the object was detected.
2. **Object ID**: The second column denotes the unique ID assigned to each object. This allows for tracking the same object across multiple frames.
3. **Bounding Box Coordinates**: The next four columns provide the bounding box's top-left corner's x and y coordinates, followed by the bounding box's width and height.
   - �*x* (3rd column): x-coordinate of the top-left corner of the bounding box.
   - �*y* (4th column): y-coordinate of the top-left corner of the bounding box.
   - �*w* (5th column): Width of the bounding box.
   - ℎ*h* (6th column): Height of the bounding box.
4. **Confidence Score**: The seventh column provides the confidence score or detection score of the object. A higher score typically means the model is more confident about the detection.
5. **Object Class, Visibility, and Other Features**: The last three columns often represent additional features like object class, visibility ratio, etc., but in the given data, these are set to `-1`, which could mean they are not used or are placeholders.

Based on the provided data:

- There are two objects being tracked (with IDs `1` and `2`).
- The data provides their bounding boxes in consecutive frames (from frame `0` to frame `10`).

For instance, the line:

```
Copy code
0,1,831.32,311.15,76.97,151.58,0.84,-1,-1,-1
```

Can be interpreted as:

- Frame number: 0
- Object ID: 1
- Bounding Box: Top-left corner at (831.32, 311.15) with a width of 76.97 and height of 151.58.
- Confidence Score: 0.84
- Other features: Not provided (all -1)

This format is useful for evaluating the performance of tracking algorithms as it provides consistent information about objects' locations and identities across frames. If you have any more questions or need further insights into ByteTrack, MOT, or the data format, feel free to ask!
