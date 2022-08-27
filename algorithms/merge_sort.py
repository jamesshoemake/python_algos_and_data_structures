def merge_sort(list):
  """
  Sorts a list into ascending order
  Returns a new sorted list

  Divide: Find midpoint and divide into sublists
  Conquer: Recurvsively sort sublists created in divide
  Combine: merge the sorted sublists created in conquer 

  T:O(n log n) for python T:O(n k log n)
  S:O(n)
  """

  if len(list) <= 1:
    return list

  # Divide
  left_half, right_half = split(list)
  
  # Conquer
  left = merge_sort(left_half)
  right = merge_sort(right_half)
  
  # Combine
  return merge(left, right)

def split(list):
  """
  Divide unsorted list at midpoint
  return two sublists -> left, right

  T: O(k log n), using the python slice runs in k time
  """

  mid = len(list)//2
  left = list[:mid] # start at beginning stops before mid point
  right = list[mid:]

  return left, right

def merge(left, right):
  """
  Merge two lists (array), sorting in the process of merging
  Return a new merged list

  T:O(n)
  """

  l = []
  i = 0
  j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      l.append(left[i])
      i += 1
    else:
      l.append(right[j])
      j += 1

  while i < len(left):
    l.append(left[i])
    i += 1
  
  while j < len(right):
    l.append(right[j])
    j += 1
  
  return l

def verify_sorted(list):
  n = len(list)
  
  if n == 0 or n == 1:
    return True
  
  return list[0] < list[1] and verify_sorted(list[1:])

thelist = [64,3,5,1,2,34]
l = merge_sort(thelist)
# print(l)
print(verify_sorted(thelist))
print(verify_sorted(l))