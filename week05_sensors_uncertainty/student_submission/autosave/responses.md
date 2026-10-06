# Week 5: Sensors, Noise, and Uncertainty

- course_id: CSCI 39536 01
- email: nabil.said54@myhunter.cuny.edu
- name: Nabil Said

## concepts.observation

Increasing noise made the measurements more spread out around the true value. Increasing bias shifted the line of the measurements away from the true value, this changed the mean and created a larger difference between the mean and the true value.

## final.course_reflection

This activity I feel Really made an emphasis on how robotics is so connected to real decisions than. when you usually think of robotics you think of programming, sensors, and getting the system to work, but this lab focused on the risk of robots making choices that are unsafe or frustrating for people. It was cool to see how small changes to a threshold, filter, or sensor weight changed the robot’s behavior. It made me think more about robotics work that combines software with testing and safety.

## final.synthesis

This lab showed that a robot cannot and should not treat a sensor reading as real world truth. In mission 1, Sensor A was fast but noisy and vulnerable to outliers, while Sensor B was steadier but biased and updated less often. In Mission 2, filtering and fusion changed the tradeoff between accuracy and responsiveness. When we selected a median configuration with a window of three, it produced relatively low error and reliable availability, but its response delay showed why accuracy alone is not enough. A delayed estimate can still be risky near people or equipment. In Mission 3, the warehouse changes reduced unsafe decisions and avoided dangerous commands while maintaining a low number of unnecessary stops. The assistive policy used a higher threshold of caution because the cost of unsafe motion near a person is more serious than the cost of an unnecessary stop. Overall, the lab connected estimation, filtering, and policy design.

## mission_1.bias

0.01

## mission_1.bias_vs_variance

basically correct. The bias is very small, mean is almost exactly the true distance of 2.00 m. Bias tells us whether the sensor is consistently shifted away from the truth.  while Variance tells us how much the readings jump around.  

## mission_1.dropouts

3

## mission_1.mean

2.0

## mission_1.median

2

## mission_1.more_samples

No. More samples would make the mean more close but they would not remove the sensor's noise.   

## mission_1.outliers

4

## mission_1.prediction

a consistently biased sensor will have a mean that is different from the true value of 2.00 m. Its readings will be shifted in the same direction and the bias will be large. A noisy sensor will have readings spread widely around 2.00 m although Its mean should stay closer to 2.00 m, and its bias should be small.

## mission_1.prediction_draft

a consistently biased sensor will have a mean that is different from the true value of 2.00 m. Its readings will be shifted in the same direction and the bias will be large. A noisy sensor will have readings spread widely around 2.00 m although Its mean should stay closer to 2.00 m, and its bias should be small.

## mission_1.profile

noisy

## mission_1.robot_consequence

For example, a robot using this sensor to decide whether it is 2 m from an obstacle  might think it is closer or farther away than it really is. The consequence for someone affected could be that the robot stops too early or too late.

## mission_1.variance

0.0368

## mission_2.comparison

The 7-reading moving average had the best overall RMSE at 0.1390 m, while the 11-reading window had the lowest MAE at 0.0747 m. However, the larg er window also had more delay: 0.05 s for 3 readings, 0.15 s for 7, and 0.25 s for 11. The matched 3-reading median performed slightly better than the 3-reading moving average, with RMSE of 0.1463 m versus 0.1548 m, because the median is less affected by Sensor A's outliers.

## mission_2.fusion_choice

The 0.25 weight on Sensor A was the best choice because it had the lowest MAE (0.0775 m) and lowest RMSE (0.1374 m). Sensor A is fast but noisy and prone to outliers, while Sensor B is steadier but biased. Giving A only 25% of the weight reduces the effe ct of its noise and outliers while still allowing its faster readings to contribute.

## mission_2.manual_average

4.17

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.3

## mission_2.prediction_draft

A larger moving-average window reduces noise more, but it will respond more slowly to changes in the target. A median filter should handle outliers better because extreme readings have less effect on the result. Raw/hold-last should respond fastest but will be the most affected by noise and outliers. A higher α should respond faster to changes in the target, but it will allow more noise and outliers into the estimate. lllllllllllllllllllllll

## mission_2.responsiveness

Larger windows smooth the noisy sensor readings more effectively, which generally reduces random fluctuations and error, but they also make the r obot slower to respond to changes.

## mission_2.selected

3

## mission_3.Assistive.prediction_draft

I expect occasional false-safe decisions near the warehouse safety boundary, but low delay because it stops after one confirming reading

## mission_3.Warehouse.prediction_draft

I expect the larger threshold and margin to stop sooner in assistive scenarios without increasing unnecessary stops in these tests.

## mission_3.context_comparison

The final warehouse policy used a 0.80 m stopping threshold and 0.15 m caution margin, while the assistive policy used a higher 1.05 m threshold and 0.25 m margin. Both final policies used Sensor A weight 0.25, a median filter with window 3, one confirmation, and STOP for missing readings. The warehouse revision produced 0% false-safe decisions, 3.06% unnecessary stops, 0.00 s maximum delay, and 0 dangerous commands. The assistive revision produced 0% false-safe decisions, 2.03% unnecessary stops, 0.00 s maximum delay, and 0 dangerous commands. The larger assistive buffer is appropriate because a false-safe decision can harm a nearby person.

## mission_3.error_costs

In the warehouse baseline, the false-safe rate was 0.62%, the unnecessary-stop rate was 3.06%, the maximum detection delay was 0.10 s, and there were 0 dangerous-command events. The revised warehouse policy reduced false-safe rate to 0% and delay to 0.00 s while keeping unnecessary stops at 3.06%. False-safe movement can endanger workers or equipment, while unnecessary stops slow workers and deliveries. In the assistive baseline, false-safe rate was 0%, unnecessary stops were 2.03%, and delay was 0.05 s. The revised assistive policy kept both rates at 0% and 2.03% while reducing delay to 0.00 s. Here, unsafe movement risks injury, while unnecessary stops can reduce a person’s independence.

## mission_3.limitations

These seven simulated scenarios show that the final policies met the specified numerical limits for false-safe rate, unnecessary stops, delay, and dangerous commands under the modeled sensor noise and dropouts. They do not prove safety with real people, varied lighting, changing floors, different robot speeds, or unexpected sensor failures. I would consult warehouse workers and safety staff, plus assistive-technology users and caregivers. Before deployment, I would run supervised trials with real sensor dropouts, different approach speeds, and people at varying distances.
