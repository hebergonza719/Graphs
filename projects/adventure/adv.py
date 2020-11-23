from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

visited_dict = {}

# gets random unvisited exit
def get_random_exit(room_visited_dict):
    unvisited_exits = []
    for k, v in room_visited_dict.items():
        if v == '?':
            unvisited_exits.append(k)

    for i in range(0, len(unvisited_exits)):
        random_index = random.randint(i, len(unvisited_exits) - 1)
        unvisited_exits[random_index], unvisited_exits[i] = unvisited_exits[i], unvisited_exits[random_index]

    if len(unvisited_exits) > 0:
        return unvisited_exits[0]
    else: 
        return None

def convert_to_coor(dictionary, next_room):
    for k, v in dictionary.items():
        if v == next_room:
            return k

def traverse_all_rooms():
    s = Stack()

    q = Queue()

    s.push(player.current_room.id)


    # start from here loop
    while len(visited_dict) < 500:

        previous_room = 0

        previous_move = ''

        while s.size() >= 1:
            # initialize room item in dictionary
            current_room = s.pop()
            if current_room not in visited_dict:
                current_room_exits = player.current_room.get_exits()
                visited_dict[current_room] = {}
                for exit in current_room_exits:
                    visited_dict[current_room][exit] = '?'

            if previous_move == 'n':
                visited_dict[current_room]['s'] = previous_room
            elif previous_move == 's':
                visited_dict[current_room]['n'] = previous_room
            elif previous_move == 'e':
                visited_dict[current_room]['w'] = previous_room
            elif previous_move == 'w':
                visited_dict[current_room]['e'] = previous_room


            # get random unvisited exit
            random_exit = get_random_exit(visited_dict[current_room])
            if random_exit is None:
                break

            # add new move to path[]
            traversal_path.append(random_exit)

            # save current room to be used as previous
            previous_room = current_room

            # save random_exit to be used as pervious_move
            previous_move = random_exit

            # move character to new random room
            player.travel(random_exit)

            # adds discovered room to previous room's graph
            visited_dict[previous_room][random_exit] = player.current_room.id

            # adds new room to the stack
            s.push(player.current_room.id)

        q.enqueue([player.current_room.id])

        visited = {}

        while q.size() > 0:
            # current_room = q.dequeue()
            current_path = q.dequeue()
            current_room = current_path[-1]
                        
            if current_room not in visited:
                visited[current_room] = current_path

                if '?' in visited_dict[current_room].values():
                    coor_path = []
                    for i in range(len(visited[current_room]) - 1):
                        coor = convert_to_coor(visited_dict[visited[current_room][i]], visited[current_room][i + 1])
                        coor_path.append(coor)
                    for coor in coor_path:
                        player.travel(coor)
                    for coor in coor_path:
                        traversal_path.append(coor)
                    break

                neighbors = list(visited_dict[current_room].values())

                for neighbor in neighbors:
                    neighbor_path = list(current_path)
                    neighbor_path.append(neighbor)
                    q.enqueue(neighbor_path)
            
        q.queue = []
        s.push(player.current_room.id)        
    
traverse_all_rooms()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
