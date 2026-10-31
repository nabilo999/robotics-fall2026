# pillar_search

## diagnosis
In my blue-only attempt, the robot spun around until it found the blue pillar. The mask picked out the blue region, and the robot turned to bring its center toward the middle of the camera image. As it got closer to the middle, the centering error got smaller. It then stopped, held that view and finished without moving forward. I kept the same steering settings for both runs and only changed the color sequence, so I didn’t test whether changing the gain would improve it.

## evidence
In my four-color attempt, the robot centered red, green, turquoise and blue in that order. It stopped at each color, centered it, held briefly and then turned to find the next one. There was a little wobble, but it still finished all four. The timeline shows that green and blue needed some extra centering before continuing, which matches what I saw. Centering a colored region doesn’t prove it’s the right object because something else with the same color could fool the detector. It also doesn’t tell the robot how far away the pillar is, only where it appears in the image.
