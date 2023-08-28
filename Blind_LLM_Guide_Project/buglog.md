
                # ### my code ------
                # for _, confidence, class_id, tracker_id in detections:
                #     x1, y1, x2, y2 = detections.xyxy[0]  # BUG, all the instance share for same xyxy
                #     line = f"{frame_number},{tracker_id},{x1},{y1},{x2},{y2},{confidence},{class_id},-1,-1\n"
                #     f.write(line)
