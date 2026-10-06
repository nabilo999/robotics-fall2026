# Mission 2

## comparison

The 7-reading moving average had the best overall RMSE at 0.1390 m, while the 11-reading window had the lowest MAE at 0.0747 m. However, the larg er window also had more delay: 0.05 s for 3 readings, 0.15 s for 7, and 0.25 s for 11. The matched 3-reading median performed slightly better than the 3-reading moving average, with RMSE of 0.1463 m versus 0.1548 m, because the median is less affected by Sensor A's outliers.

## fusion_choice

The 0.25 weight on Sensor A was the best choice because it had the lowest MAE (0.0775 m) and lowest RMSE (0.1374 m). Sensor A is fast but noisy and prone to outliers, while Sensor B is steadier but biased. Giving A only 25% of the weight reduces the effe ct of its noise and outliers while still allowing its faster readings to contribute.

## manual_average

4.17

## manual_fusion

2.25

## manual_median

2.3

## prediction_draft

A larger moving-average window reduces noise more, but it will respond more slowly to changes in the target. A median filter should handle outliers better because extreme readings have less effect on the result. Raw/hold-last should respond fastest but will be the most affected by noise and outliers. A higher α should respond faster to changes in the target, but it will allow more noise and outliers into the estimate. lllllllllllllllllllllll

## responsiveness

Larger windows smooth the noisy sensor readings more effectively, which generally reduces random fluctuations and error, but they also make the r obot slower to respond to changes.

## selected

3
