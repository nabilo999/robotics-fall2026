# mission_1

## diagnosis
Comparing normal_1 and dim_1 we see that in normal_1, the green box overlaps the mug but includes a large amount of the desk, so it does not locate the mug accurately. The mask includes both mug and desk pixels. In dim_1, the box shifts to the right and mostly covers the desk and handle area, missing most of the mug’s body. More of the dark mug is excluded by the brightness rule. Both are not accurately detected. 

## limitations
During practice, I experimented mainly with hue and saturation, although I also tried other settings, changing only one parameter at a time. My final hue range was 0–179, which allows every hue, and my saturation range was 83–255. The final mask included both mug and desk pixels, causing the selected box to include background. Because I changed several settings, I cannot confidently say that one parameter had more sway. A limitation is that a different cup with different colors might be excluded by these thresholds, while a background with similar colors could still be selected.
