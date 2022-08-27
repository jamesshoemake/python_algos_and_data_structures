def recursive_binary_search(list, target):
  """
    bineary search requires values to be sorted
    python has a max recursion depth
  """
  if len(list) ==0: 
    return False
  else:
    mid = (len(list))//2

    if list[mid] == target:
      return True
    else:
      if list[mid] < target:
        return recursive_binary_search(list[mid+1:], target) # [mid+1:] short hand for start at mid plus one, go to end of list
      else:
        return recursive_binary_search(list[:mid], target)

def verify(result):
  print("Target found at Index: ", result)
  
numbers = [1,2,3,4,5,6,7,8,9,10]

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 9)
verify(result)