# robot-mesero
Codes for my waiter robot.

MOVEMENT FIRST PART*******************************************************************************************

---DONE: 
---The agent needs to go to all the people and then go back to its spot
---It chooses the order in which to go to all the people by looking at the euclidean distance that it would 
---travel in each permutation possible.
---and choosing the permutation with the lowest overall distance.

706qlearning. The agent walks to the first person without crashing into other people or objects.
It has a Q matrix for the target person.

1306qlearning. The agent goes to the first person and then returns to its spot without crashing into other 
people or objects.
It has a Q matrix for the target person and for its spot.

1706qlearning. The agent goes to all the people and then returns to its spot without crashing into other 
people or objects. 
It has a Q matrix where it learnt how to go to each person, and one for its spot.

SIMULATION MOVEMENT FOR THE REAL WORLD IMPLEMENTATION COMING*************************************************
---CURRENTLY WORKING ON: 
---A Voronoi algorithm will be fused with a modified version of the previous movement algorithm.

MOVEMENT REAL WORLD******************************************************************************************
---COMING UP:
---Mapping with a Lidar and sensors
---Using this map with its necessary adaptation of the algorithm of movement for the real world.

IMAGE PROCESSING********************************************************************************************
---COMING UP:
---Reading QR codes to detect the waiter is needed and to know in what table the person that is calling the 
robot is seated on.

MOVEMENT AND IMAGE PROCESSING FUSION*************************************************************************
---COMING UP:
---



