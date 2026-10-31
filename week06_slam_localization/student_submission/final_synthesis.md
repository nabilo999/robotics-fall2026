# Final synthesis

From my two maps, the robot can estimate where walls, obstacles, and open space are in the areas its LiDAR scanned. It cannot assume it knows the full layout of the house if it never scanned parts of it. Unknown space may mean there is a wall or that it is safe to drive through.

My first route covered more of the house but that is due to issues I had with my second run. My original plan of one route from the left and one route starting from the right wouldn't have made a big difference. A better comparison would have been going into the rooms verses just looking through the doors. The first map would have showed recognizable walls and rooms, while the second would have barely showed any useful info inside of the rooms.&#x20;

Even then, with both runs I would've missed spots around the table and two rooms after the robot bumped into a wall and got stuck. Furniture can block the LiDAR, so just scanning from a doorway is not enough.

The robot’s motion estimate can also build up error, which could make walls appear shifted or doubled. Revisiting an area can help SLAM correct that, but that takes time and many runs to make sure everything is correct.

I would trust the first map more for a later task because it has more visible structure and coverage. Still, I would want to finish scanning the missing rooms and check the rough edges before relying on it for navigation.
