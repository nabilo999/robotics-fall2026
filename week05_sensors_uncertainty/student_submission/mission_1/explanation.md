# Mission 1

## bias

0.01

## bias_vs_variance

basically correct. The bias is very small, mean is almost exactly the true distance of 2.00 m. Bias tells us whether the sensor is consistently shifted away from the truth.  while Variance tells us how much the readings jump around.  

## dropouts

3

## mean

2.0

## median

2

## more_samples

No. More samples would make the mean more close but they would not remove the sensor's noise.   

## outliers

4

## prediction

a consistently biased sensor will have a mean that is different from the true value of 2.00 m. Its readings will be shifted in the same direction and the bias will be large. A noisy sensor will have readings spread widely around 2.00 m although Its mean should stay closer to 2.00 m, and its bias should be small.

## prediction_draft

a consistently biased sensor will have a mean that is different from the true value of 2.00 m. Its readings will be shifted in the same direction and the bias will be large. A noisy sensor will have readings spread widely around 2.00 m although Its mean should stay closer to 2.00 m, and its bias should be small.

## profile

noisy

## robot_consequence

For example, a robot using this sensor to decide whether it is 2 m from an obstacle  might think it is closer or farther away than it really is. The consequence for someone affected could be that the robot stops too early or too late.

## variance

0.0368
