# Week 6: SLAM and Mapping

- email: NABIL.SAID54@login.cuny.edu
- name: Nabil Said

## final.course_reflection

It was cool seeing the difference between how I saw the world while moving through it and how the robot saw it. Some things were clear to me, like where a room started or what was behind a table, but in the robot's view they looked completely different or were missing. It made me realize how much information I take for granted and how much the robot depends on what it can actually scan.

## final.synthesis

From my two maps, the robot can estimate where walls, obstacles, and open space are in the areas its LiDAR scanned. It cannot assume it knows the full layout of the house if it never scanned parts of it. Unknown space may mean there is a wall or that it is safe to drive through.

My first route covered more of the house but that is due to issues I had with my second run. My original plan of one route from the left and one route starting from the right wouldn't have made a big difference. A better comparison would have been going into the rooms verses just looking through the doors. The first map would have showed recognizable walls and rooms, while the second would have barely showed any useful info inside of the rooms.&#x20;

Even then, with both runs I would've missed spots around the table and two rooms after the robot bumped into a wall and got stuck. Furniture can block the LiDAR, so just scanning from a doorway is not enough.

The robot’s motion estimate can also build up error, which could make walls appear shifted or doubled. Revisiting an area can help SLAM correct that, but that takes time and many runs to make sure everything is correct.

I would trust the first map more for a later task because it has more visible structure and coverage. Still, I would want to finish scanning the missing rooms and check the rough edges before relying on it for navigation.


## mission_1.drift_and_revisit

When I returned to an area I had already scanned, I didn't really notice any major changes in the walls. I couldn't tell if the walls shifted or doubled because I wasn't paying too much attention to that. 

## mission_1.limitations

It missed a couple of spots under the table. I think that is because of the lighting or because of how it went around the table, and the legs kind of blocked some of the way. Also, I couldn't finish mapping out the room because the robot got stuck and couldn't move any further. I bumped into a wall by accident, and then the robot kind of did something weird where it couldn't progress correctly, so I couldn't finish mapping out the two rooms left.

## mission_1.route.original_prediction

I would move straight. I would turn left. I would turn left again. I would keep going straight. I would turn right to see the entire room. Then I would go to the middle of the room, going straight, and then I would turn left. Then I would go ahead until I'm in the middle of the next room. I would look left and then right. Then I would continue moving forward to the right. I would go to the end of the room, and then I would turn around. Then I would go straight, go straight, and then I would turn right. And then I would turn right again, and then I would go straight ahead. Just before I hit the wall, I would turn left 90 degrees, and all these turns are 90 degrees. I would go ahead, go straight, and then I would turn left and go straight, and then I would turn another left and go straight, and then I would turn another left and go straight. Then I would turn right, and then go straight, and then turn another way, and then go straight, and then go straight, and then turn right, and then go straight, go straight, go straight, and then I would be in the last room. Then I would turn around just to map it fully.

This should give us full coverage of all the rooms because we pass fully through them and we made sure to cover everything. The only thing that we would have to worry about is how far the LiDAR can see. If the LiDAR can see far enough into the room, like a longer distance, then we should have full coverage. Otherwise, we might have some issues.

## mission_1.route.prediction_draft

I would move straight. I would turn left. I would turn left again. I would keep going straight. I would turn right to see the entire room. Then I would go to the middle of the room, going straight, and then I would turn left. Then I would go ahead until I'm in the middle of the next room. I would look left and then right. Then I would continue moving forward to the right. I would go to the end of the room, and then I would turn around. Then I would go straight, go straight, and then I would turn right. And then I would turn right again, and then I would go straight ahead. Just before I hit the wall, I would turn left 90 degrees, and all these turns are 90 degrees. I would go ahead, go straight, and then I would turn left and go straight, and then I would turn another left and go straight, and then I would turn another left and go straight. Then I would turn right, and then go straight, and then turn another way, and then go straight, and then go straight, and then turn right, and then go straight, go straight, go straight, and then I would be in the last room. Then I would turn around just to map it fully.

This should give us full coverage of all the rooms because we pass fully through them and we made sure to cover everything. The only thing that we would have to worry about is how far the LiDAR can see. If the LiDAR can see far enough into the room, like a longer distance, then we should have full coverage. Otherwise, we might have some issues.

## mission_2.comparison

I had an issue with rerunning the simulation where the robot couldnt connect to the keyboard so the courage of the first run was better but if I were to compare the coverage would have probably been the same starting from the left or right and in bothe you would have to go inside the rooms to scan everything and due to obstructions inside the rooms you cant just scanat the door frame

## mission_2.map_choice

the first but ideally there wouldnt be the big of a diffrence if, scaning room be room is not time efficient but is the most accurate. we are comparing between detail and  speed.

## mission_2.strategy.original_prediction

I will go ahead and go through the door. This time, I will go towards the right. I will explore the room on the bottom first. I will leave that room, and then I will go up to the room on the bottom right. After that, I will go back through the hallway towards the left of the door entrance. I will try to pass under the table, and then I will go into the last room.

## mission_2.strategy.prediction_draft

I will go ahead and go through the door. This time, I will go towards the right. I will explore the room on the bottom first. I will leave that room, and then I will go up to the room on the bottom right. After that, I will go back through the hallway towards the left of the door entrance. I will try to pass under the table, and then I will go into the last room.
