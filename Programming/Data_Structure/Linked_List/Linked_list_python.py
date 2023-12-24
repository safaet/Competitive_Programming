# define a class named Node
class Node:
	# define the constructor with parameters
	def __init__(self, data):
		#assign the parameters to the attribute
		self.data = data
		self.next = None

# define a class named LinkedList
class LinkedList:
	#define the constructor with an optional parameter
	def __init__(self, head=None):
		#initialize the head attribute with the given parameter
		self.head = head

	# define a method to insert a node at the end of the list
	def append(self, data):
		# create a new node with the given data
		new_node = Node(data)
		# if the list is empty, make the new node as the head
		if self.head is None:
			self.head = new_node
			return
		# otherwise, traverse the list until the last node
		current = self.head
		while current.next:
			current = current.next
		# link the last node with the new node
		current.next = new_node

	# define a method to print the list
	def print_list(self):
		# create a pointer to traverse the list
		current = self.head
		# loop until the end of the list
		while current:
			#print the data of the current node
			print(current.data)
			# move to the next node
			current = current.next

# create an object of type LinkedList with an optional head node
llist = LinkedList(Node("red"))

# append some nodes to the list
llist.append("blue")

llist.print_list()
