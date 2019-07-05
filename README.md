# robot-mesero
Codes for my waiter robot.

<h3>MOVEMENT FIRST PART</h3>

<strong>DONE:</strong> 
<em>-The agent needs to go to all the people and then go back to its spot. <br>
-It chooses the order in which to go to all the people by looking at the euclidean distance that it would travel in each permutation possible. And chooses the permutation with the lowest overall distance.</em>

<p>706qlearning. The agent walks to the first person without crashing into other people or objects.
It has a Q matrix for the target person.<br>

1306qlearning. The agent goes to the first person and then returns to its spot without crashing into other 
people or objects.
It has a Q matrix for the target person and for its spot.<br>

1706qlearning. The agent goes to all the people and then returns to its spot without crashing into other 
people or objects.
It has a Q matrix where it learnt how to go to each person, and one for its spot.</p>

<h3>SIMULATION MOVEMENT FOR THE REAL WORLD IMPLEMENTATION COMING</h3>
<strong>CURRENTLY WORKING ON: </strong>
<em>-A Voronoi algorithm will be fused with a modified version of the previous movement algorithm.</em>

<h3>MOVEMENT REAL WORLD</h3>
<strong>COMING UP:</strong>
<em>-Mapping with a Lidar and sensors
-Using this map with its necessary adaptation of the algorithm of movement for the real world.</em>

<h3>IMAGE PROCESSING</h3>
<strong>COMING UP:</strong>
<em>-Reading QR codes to detect the waiter is needed and to know in what table the person that is calling the 
robot is seated on.</em>

<h3>MOVEMENT AND IMAGE PROCESSING FUSION</h3>
<strong>COMING UP:</strong>
<em> </em>



