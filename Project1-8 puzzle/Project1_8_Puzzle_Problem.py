#!/usr/bin/env python
# coding: utf-8

# # Planning Project 1:
# 
# Implement a BFS algorithm to solve the 8 puzzle problem
# # Data Structures to be used : List, Dictionaries
# List: Update Nodes (Parent and Child)
# Dictionaries: Update Node information 
# To keep track of the node information, maintain a list of dictionaries
# #Author : Aditya Khopkar | 116911627

import numpy as np
import time
import os

#Accept input from the user and store it in matrix form
def take_input_():
    while True:
        print("Please Load the initial puzzle matrix from 0-8. Do not exceed the range, No repetition allowed")
        in_puzzle = []
        for i in range(9):
            in_puzzle.append(int(input())) 
        if check_input_(in_puzzle) == True:
            initialNode = np.array(in_puzzle).reshape(3,3)
            break
    return initialNode

#Check validity of the input
def check_input_(mat):
    for i in range(len(mat)):
        if mat[i]>8 or mat[i]<0:
            print("Invalid input, re-enter matrix")
            return False
    for i in range(len(mat)):
        counter = 0
        for j in range(i,len(mat)):
            if mat[i] == mat[j]:
                counter+=1
        if counter >= 2:
            return False
    else:
        return True

#Swap operation to be used in the action functions
def swap(a,b):
    return b,a

#Find the index of the 0 element in the puzzle
def find_index_(arr):
    i,j=np.where(arr==0)
    i = int(i)
    j = int(j)
    return i,j

# # Action set definition
#
def move_up_(arr):
    i,j = find_index_(arr)
    if i == 0:
        return None
    else:
        move_arr =  np.copy(arr)
        move_arr[i-1,j],move_arr[i,j]=swap(arr[i-1,j],arr[i,j])
        return move_arr

def move_down_(arr):
    i,j = find_index_(arr)
    if i == 2:
        return None
    else:
        move_arr =  np.copy(arr)
        move_arr[i+1,j],move_arr[i,j]=swap(arr[i+1,j],arr[i,j])
        return move_arr

def move_left_(arr):
    i,j = find_index_(arr)
    if j == 0:
        return None
    else:
        move_arr =  np.copy(arr)
        move_arr[i,j-1],move_arr[i,j]=swap(arr[i,j-1],arr[i,j])
        return move_arr

def move_right_(arr):
    i,j = find_index_(arr)
    if j == 2:
        return None
    else:
        move_arr =  np.copy(arr)
        move_arr[i,j+1],move_arr[i,j]=swap(arr[i,j+1],arr[i,j])
    return move_arr

#Check if goal node is reached
def goalReached(current_node,goal_node):
    if np.array_equal(current_node,goal_node):
        return True

#Moving the tiles    
def action_(action,arr):
    if action == "Up":
        return move_up_(arr)
    if action == "Down":
        return move_down_(arr)
    if action == "Left":
        return move_left_(arr)
    if action == "Right":
        return move_right_(arr)

#Check if the element is in the list: boolean function
def inList(arr,lst):
    counter = 0
    for element in lst:
        if np.array_equal(element,arr):
            counter+=1
    if counter > 0:
        return True
    return False

#Check solvability of the input
def check_solvable_(arr):
    arr = np.reshape(arr,9)
    invCount = 0
    for i in range(9):
        if not arr[i] ==0:
            for j in range(i+1,9):
                if not arr[j] == 0:
                    #continue
                    if arr[j]>arr[i]:
                        invCount+=1
    if invCount%2 == 0:
        print("Solvable input")
        return True
    else:
        print("Insolvable input, re-enter puzzle")
        return False

#Manipulate data to be in a linear 1D format
def arr_manipulation(arr):
    manArr = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            manArr.append(arr[j,i])
    return manArr

#Write .txt file for nodePath and Nodes
def write_file_(data,flag):
    if flag == -1:
        if os.path.exists("nodePath.txt"):
            os.remove("nodePath.txt")
        file1 = open("nodePath.txt","a")
        for node in data:
            file1.write(str(arr_manipulation(node))+"\n")
        file1.close()
    if flag == 0:
        if os.path.exists("Nodes.txt"):
            os.remove("Nodes.txt")
        file2 = open("Nodes.txt","a")
        for element in data:
            file2.write(str(arr_manipulation(element))+"\n")
        file2.close()

# Write .txt file for nodes_info
def write_node_info(cid,pid):
    if os.path.exists("NodesInfo.txt"):
        os.remove("NodesInfo.txt")
    cost = []
    f = open("NodesInfo","a")
    f.write("Child Id"+"\t"+"Parent Id"+"\t"+"Cost"+"\n")
    for i in range(len(cid)):
        f.write(str(cid[i])+"\t"+str(pid[i])+"\t"+"\n")
    f.close()
    

#Generate valid nodes
def generate_nodes_(initialNode,goalNode):
    print("Solving...")
#initialize the data structures
    queue_ =[]
    action = ["Up","Down","Left","Right"]
    child_ = np.zeros((3,3),dtype=int)
    parent_ = []
    queue_.append(initialNode)
    parent_nodes_ =[]
    final_nodes_=[]
    Valid_Nodes = []
    node_count = 0
    level = 0
    while queue_:
#initialize the dictionary data structure
        node = {
     "Parent": [],
    "Child" : [],
    "node_id_parent": 0,
    "node_id_child" : 0
}
        child_nodes_ =[]
        current_node = queue_.pop(0) #update current node
        parent_ = np.array2string(current_node)
        parent_nodes_.append(parent_) #update parent node to keep track of the visited node
        node["Parent"] = current_node #update node information
        node["node_id_parent"] = level
        #print("Level = ", level)
        level += 1 #maintain index of parent
        for moves in action:
            if action_(moves,current_node) is not None: #for all valid actions
                child_ = action_(moves,current_node)  
                if np.array2string(child_) not in parent_nodes_: #check if the node is previously visited
                            queue_.append(child_) #Update the queue
                            child_nodes_.append(child_)
                            node["Child"] = child_nodes_
                            node_count += 1
                            node["node_id_child"] = node_count
                            #print("Child Node = ",node_count)
                            final_nodes_.append(child_)
                            if goalReached(child_,goalNode): #Check if goal position is reached
                                Valid_Nodes.append(node)
                                print("Goal is Reached")
                                return Valid_Nodes, child_, final_nodes_
	#Update the list of dictionaries
        Valid_Nodes.append(node)
    return None, None, None

#Implement Backtracking
def generate_path_(valid,child):
    p = []
    cid = []
    pid = []
    valid = valid[::-1]
    print("Generating Path..")
    for i in range(len(valid)):
        node = []
        node = valid[i].copy()
        if inList(child,node["Child"]):
            p.append(child)
            child = node["Parent"].copy()
            cid.append(node["node_id_child"])
            pid.append(node["node_id_parent"])
    path_ = p[::-1]
    child_id = cid[::-1]
    parent_id = pid[::-1]
    return path_,child_id, parent_id

#Implement BFS algorithm
def solve_BFS_(initialNode,goalNode):
    valid_nodes, current_node, finalnodes = generate_nodes_(initialNode,goalNode)
    path, cid, pid = generate_path_(valid_nodes,current_node)
    print("Number of steps taken: ",len(path))
    return path,cid,pid, finalnodes

#MAIN FUNCTION:
initialNode = take_input_()
if check_solvable_(initialNode) is not True: 
    initialNode = take_input_()

# #initialNode = np.array([[2,3,6],[7,1,4],[5,8,0]]).reshape(3,3)
# #No. of levels = 12
# #No of parents: 1210, No. of child: 2063

goalNode = np.array([[1,2,3],[4,5,6],[7,8,0]]).reshape(3,3)

t1 = time.time()
path,cid,pid, f = solve_BFS_(initialNode,goalNode)
print("Path followed:", path)
t2 = time.time()
TIME = (t2-t1)/60

#write the data into the file
#pass argument of flag to suggest, which file needs to be updated
#Dont change this: can taken only -1 and 0 as argument for flag
write_file_(path,-1)
write_file_(f,0)
write_node_info(cid,pid)

print("Child ID node: ", cid)
print("Parent ID node: ", pid)
print("Time taken to solve = ", TIME)

