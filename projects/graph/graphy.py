# Singly Linked List
class ListNode:
    def __init__(self, value):
        self.value = value
​
       self.next = None 
​
       # self.prev if DLL
​
## LL Traversal
current = node
while current is not None:
    current = current.next
​
class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
​
        self.left = None
        self.right = None
​
# BST Traversal
## DFT, BFT
### Stack, Queue
​
while node is not None:
    recurse(self.left)
    recurse(self.right)
​
        
class GraphNode:
    def __init__(self, value):
        self.value = 'B'
​
        # options: dictionary, array, set
        # B's connections
        self.connections = set('a', 'c', 'd')
​
        # A's connections
        self.connections = set('B')
​
        # D's connections - Billy no mates
        self.connections = set()
​
        
# outbound vs inbound connections?
​
# Graph terminology for 2-way vs 1-way connections
## undirected graph vs directed graph
## (FB, LinkedIn) vs (Instagram, Twitter, TikTok)
​
## Graph Traversals
​
## DFT, stack
### Check every node once, check every connection once
​
# make a stack
stack = Stack(3, 6, 8, 9)
# make a set to track visited
visited = set(1, 2, 4)
​
# put the start node into the stack
​
# while the stack isn't empty
​
## pop off the top of the stack, this is our current node
current_node = 7
​
## check if we have visited this node yet
### if not, add it our visited set
### and add each of its neighbors to our stack
​
## Time complexity?
### How many times did we visit each node? once
### How many times did we check each connection? once
​
## O(number of nodes + number of connections)
### O(n + m)
## so linear!
​
# BFT, queue
#        --->>>>>
q = Queue()
​
# make a set to track visited
visited = set('A', "B", "C", "D", 'E', "F", "G")
​
# enqueue the start node
​
# while our queue isn't empty
​
## dequeue from front of line, this is our current node
current_node = "A"
​
## check if we've visited here yet
### if not, add to visited
### get its neighbors, for each, add to queue
neighbors = set("A", "F")
​
# Time complexity?
## visit every vertex once, visit every edge once
## O(n + m)
## O(node + edge)
​
​
# DFT vs. BFT
## same time complexity, each just as fast
## DFT can be done recursively
