# Mission 3

## Assistive.prediction_draft

I expect occasional false-safe decisions near the warehouse safety boundary, but low delay because it stops after one confirming reading

## Warehouse.prediction_draft

I expect the larger threshold and margin to stop sooner in assistive scenarios without increasing unnecessary stops in these tests.

## context_comparison

The final warehouse policy used a 0.80 m stopping threshold and 0.15 m caution margin, while the assistive policy used a higher 1.05 m threshold and 0.25 m margin. Both final policies used Sensor A weight 0.25, a median filter with window 3, one confirmation, and STOP for missing readings. The warehouse revision produced 0% false-safe decisions, 3.06% unnecessary stops, 0.00 s maximum delay, and 0 dangerous commands. The assistive revision produced 0% false-safe decisions, 2.03% unnecessary stops, 0.00 s maximum delay, and 0 dangerous commands. The larger assistive buffer is appropriate because a false-safe decision can harm a nearby person.

## error_costs

In the warehouse baseline, the false-safe rate was 0.62%, the unnecessary-stop rate was 3.06%, the maximum detection delay was 0.10 s, and there were 0 dangerous-command events. The revised warehouse policy reduced false-safe rate to 0% and delay to 0.00 s while keeping unnecessary stops at 3.06%. False-safe movement can endanger workers or equipment, while unnecessary stops slow workers and deliveries. In the assistive baseline, false-safe rate was 0%, unnecessary stops were 2.03%, and delay was 0.05 s. The revised assistive policy kept both rates at 0% and 2.03% while reducing delay to 0.00 s. Here, unsafe movement risks injury, while unnecessary stops can reduce a person’s independence.

## limitations

These seven simulated scenarios show that the final policies met the specified numerical limits for false-safe rate, unnecessary stops, delay, and dangerous commands under the modeled sensor noise and dropouts. They do not prove safety with real people, varied lighting, changing floors, different robot speeds, or unexpected sensor failures. I would consult warehouse workers and safety staff, plus assistive-technology users and caregivers. Before deployment, I would run supervised trials with real sensor dropouts, different approach speeds, and people at varying distances.
