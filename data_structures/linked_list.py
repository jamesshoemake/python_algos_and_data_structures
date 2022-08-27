class Node:
  """
    Object for storing single node of a linked list
    Models two attributes - data and the link to next node in list
  """
  data = None
  next_node = None

  def __init__(self, data):
    self.data = data

  def __repr__(self):
    return "<Node data: %s>" % self.data
"""
  # Testing in command line
  # python -i linked_list.pyrun # repl with linked_list.py loaded
  # N1 = Node(10)
  # N1 = Node(10)
  # N1
  # N2 = Node(20)
  # N1.next_node = N2
  # N1.next_node
"""

class LinkedList:
  """
    Singly linked list
  """
  def __init__(self):
    self.head = None
  
  def is_empty(self):
    return self.head == None

  def size(self):
    """
      Return number of nodes in list using a linear opperation O(n)
    """
    current = self.head
    count = 0

    while current:
      count += 1
      current = current.next_node
    return count

  def add(self, data):
    """
      Add new node with data at head of list in constant time O(1)
    """
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node

  def search(self, key):
    """
      Search for first node containing data matching key in linear time O(n)
      Returns node or None if not found

      example use:
      l = LinkedList()
      l.add(10)
      l.add(n...)
      n = l.search(10)
      n 
    """
    current = self.head

    while current:
      if current.data == key:
        return current
      else:
        current = current.next_node
    return None

  def insert(self, data, index):
    """
      Insert new Node containing data at index position in linear time O(n)
      Insertion at O(1)
      Searching O(n)
    """

    if index == 0:
      self.add(data)
    
    if index > 0:
      new = Node(data)
      position = index
      current = self.head

      while position > 1:
        current = current.next_node
        position -= 1

      prev_node = current
      next_node = current.next_node
      
      prev_node.next_node = new
      new.next_node = next_node
    
  def remove(self, key):
    """
      Remove a node containing data matching key
      Return node or None if key doesn't exist
      Taking T:O(n) 
    """
    current = self.head
    previous = None
    found = False

    while current and not found:
      if current.data == key and current is self.head:
        found = True
        self.head = current.next_node
      elif current.data == key:
        found = True
        previous.next_node = current.next_node
      else:
        previous = current
        current = current.next_node

    return current

  def node_at_index(self, index):
    if index == 0:
      return self.head
    else:
      current = self.head
      position = 0

      while position < index:
        current = current.next_node
        position += 1
      
      return current


  def __repr__(self):
    """
      Return a string representation of the list in linear time O(n)
    """

    nodes = []
    current = self.head

    while current:
      if current is self.head:
        nodes.append("[Head: %s]" % current.data)
      elif current.next_node is None:
        nodes.append("[Tail: %s]" % current.data)
      else:
        nodes.append("[%s]" % current.data)
      
      current = current.next_node
    return '-> '.join(nodes)

"""
  Using LinkedList in command line
  l = LinkedList()
  l.add(1)
  l.add(2)
  l.size()

  OR

  l = LinkedList()
  N1 = Node(10)
  l.head = N1
  l.size()
"""