import random

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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name) # adding User class with name to dictionary with last_id as key
        self.friendships[self.last_id] = set() # adds empty set() as it's dictionary value and last_id as key

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships

        total_friendships = avg_friendships * num_users

        friendship_combos = []

        for user_id in range(1, num_users + 1):
            for friend_id in range(user_id + 1, num_users + 1): # begin after index which is user_id
                friendship_combos.append((user_id, friend_id))
        
        self.fisher_yates_shuffle(friendship_combos)

        friendship_to_make = friendship_combos[:(total_friendships // 2)]

        for friendship in friendship_to_make:
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        def bfs(starting, destination):
            visited1 = set()
            q_list = Queue()
            first_path = [starting]
            q_list.enqueue(first_path)
            if starting == destination:
                return first_path
            else:
                while q_list:
                    path = q_list.dequeue()
                    current_node = path[-1]
                    if current_node not in visited1:
                        friendships = self.friendships[current_node]
                        for friend in friendships:
                            new_path = list(path)
                            new_path.append(friend)
                            q_list.enqueue(new_path)
                            if friend == destination:
                                return new_path
                        visited1.add(current_node)


        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        q = Queue()

        q.enqueue(user_id)

        while q.size() > 0:

            current_friend = q.dequeue()

            if current_friend not in visited:
                visited[current_friend] = bfs(user_id, current_friend)
                friendships = self.friendships[current_friend]
                for friend in friendships:
                    q.enqueue(friend)
        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)