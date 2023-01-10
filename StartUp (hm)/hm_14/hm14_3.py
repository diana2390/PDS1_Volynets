from binarytree import build
class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

# Insert method to create nodes
    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    def insert_list(self, list):
        for node in list:
            self.insert(node)

# findval method to compare the id_node with nodes
    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
        else:
            print(str(self.id_node) + ' is found')

# Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node),
        if self.right:
            self.right.print_tree()

# Mix and max value in binary search tree
    def min_value(self):
        if self.left:
            self.left.min_value()
        else:
            print(f"The min value is: {self.id_node}")

    def max_value(self):
        if self.right:
            self.right.max_value()
        else:
            print(f"The max value is: {self.id_node}")

# Function for deleting element
    def _search(self, first_iter):
        if first_iter:
            self.left._search(first_iter=False)
        elif self.right:
            self.right._search(first_iter=False)
        else:
            return self.id_node

# Deleting element in binary tree
    def delete_node(self, node):
        if node < self.id_node:
            self.left.delete_node(node)
        elif node > self.id_node:
            self.right.delete_node(node)
        else:
            if not self.left and not self.right:
                self.id_node = None
            elif self.right and not self.left:
                self.id_node = self.right
            elif self.left and not self.right:
                self.id_node = self.left
            elif self.left and self.right:
                self.id_node = self._search(True)

t1 = Tree(8)
my_list = [8, 3, 10, 2, 6, 9, 13, 1, 7, 5, 12]
t1.insert_list(my_list)
# t1.print_tree()
binary_tree = build(my_list)
print("Binary tree from list:\n",
        binary_tree)
t1.delete_node(6)
t1.print_tree()