# mission_2

## comparison
In the normal condition, the classical detector had 0 correct boxes, 2 false boxes and 2 missed mugs, while the learned detector had 1 correct box, 0 false boxes and 1 missed mug. In dim lighting, classical had 0 correct, 1 false and 2 missed, while learned had 0 correct, 0 false and 2 missed. The occluded condition had the same counts as dim. The learned detector therefore reduced false boxes, but it still missed every mug in the dim and occluded conditions at the 0.50 threshold. In normal_1, the classical box includes too much desk. The learned detector produces no accepted box because its best cup score is approximately 0.41.

## choice
I recommend the learned detector for further testing with a detection threshold of 0.50 and the current duplicate-suppression setting of 0.45. Across these three conditions, it produced one correct box and no false boxes, compared with zero correct boxes and four false boxes for classical. However, it still missed five mugs, so I would also investigate lower acceptance thresholds. 
For normal_1, the foreground mask had an IoU of 0.5756 and Dice of 0.7306. It included 4,453 extra pixels and missed 1,852 mug pixels. A detailed foreground mask does not identify the requested mug because it marks foreground regions without assigning a cup label. One important limitation is that this small image collection cannot establish reliable performance in new real-world scenes.
