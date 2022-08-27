import sys
sys.path.insert(0,"..")
from data_structures.linked_list import LinkedList

def merge_sort(linked_list):
  """
  Sorts a linked list into ascending order

  - Recursively divide a linked list into sublists containing single node
  - Repeatedly merge the sublists to produce sorted sublists until one remains
  - Returns a sorted linked list
  T:O(kn log n) due to split function taking k log n
  """

  if linked_list.size() == 1:
    return linked_list
  elif linked_list.head is None:
    return linked_list

  # Divided
  left_half, right_half = split(linked_list)
  # Conquer
  left = merge_sort(left_half)
  right = merge_sort(right_half)
  # Combine
  return merge(left, right)

def split(linked_list):
  """
  Divide unsorted linked lists into sublists at midpoint
  T:O(k log n), node_at_index costs k time
  """

  if linked_list == None or linked_list.head == None:
    left_half = linked_list
    right_half = None
  
    return left_half, right_half
  else:
    size = linked_list.size()
    mid = size//2

    mid_node = linked_list.node_at_index(mid-1)
  
  left_half = linked_list
  right_half = LinkedList()
  right_half.head = mid_node.next_node
  mid_node.next_node = None

  return left_half, right_half

def merge(left, right):
  """
  Merges two linked list, sorting by data in nodes
  Return new merged linked list
  T:O(n)
  """

  # Create new linked list that contains nodes from merging left and right

  merged = LinkedList()
  # add temp head 
  merged.add(0)

  # set current to head of linked list
  current = merged.head

  #obtain head nodes for left and right linked list
  left_head = left.head
  right_head = right.head

  # interate over left and right as until a tail node is reached
  while left_head or right_head:
    # if head node of left is none, we have passed tail
    # add the node from right to merged linked list
    if left_head is None:
      current.next_node = right_head
      # call next on right to set loop condition to False
      right_head = right_head.next_node
    # if head node of right is not, we have passed tail
    # add the node from left to merged linked list
    elif right_head is None:
      current.next_node = left_head
      # call next on left to set loop condition to False
      left_head = left_head.next_node
    else:
      # not at either tail node
      # obtain node data to compare
      left_data = left_head.data
      right_data = right_head.data
      # if data on left is less than right, set current to left node
      if left_data < right_data:
        current.next_node = left_head
        # move left head to next node
        left_head = left_head.next_node
      # If left data is greater than right, set current to right node
      else: 
        current.next_node = right_head
        # move right head to next node
        right_head = right_head.next_node
    # move current to next node
    current = current.next_node

  # discard temp head and set first merged node as head
  head = merged.head.next_node
  merged.head = head

  return merged

l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)
print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)