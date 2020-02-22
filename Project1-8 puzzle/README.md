# 8-Puzzle-Problem
Solving an 8 puzzle problem using BFS algorithm in Python
8 puzzle problem is a famous puzzle problem where in we have to move in the tiles to reach the final goal node.
The valid actions of the tiles are as follows:
+ Horizontal Motion 
+ Vertical Motion

However, to solve this puzzle using a software, we break down the action set into 4 classes. We identify these action sets depending on the 0th tile in the puzzle and are defines as follows:
+ Move up 
+ Move down
+ Move left
+ Move right

I have implemented BFS algorithm to solve the puzzle. However, BFS is not an optimum algorithm.
To optimize I have used some optimizing techniques such as converted the array to check the visited nodes into string.

To execute the file:
+ Open terminal
+ type command - cd "/enter the location of the saved file"
		 python3 Project1_8_Puzzle_Problem.py

The code generates 3 text files:
+ nodePath.txt = Suggests the path taken to solve the problem, i.e., the final output. Format of the file :
For an array entry of the following way:

$$
\left[\begin{array}
1 & 3 & 5\\
6 & 7 & 8\\
4 & 5 & 0
\end{array}\right]
$$ 

The file generates text format as: [1,6,4,3,7,2,5,8,0]
+ Nodes.txt - All the explored nodes in the program (follows similar format)
+ NodesInfo.txt - ID of the child nodes and the corresponding Parent nodes. Cost is not considered in this program as BFS doesn't work on cost.
 
