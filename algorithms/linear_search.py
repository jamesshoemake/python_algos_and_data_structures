def linear_search(list,target):
  """ 
    Return index of target target if found, otherwise return none
    target is the position the value exists
    list is the list of values to search
  """

  for i in range(0,len(list)):
    if list[i] == target:
      return i
  
  return None

def verify(index):
  if index is not None:
    print("Target found at Index: ",index)
  else:
    print("Target not present in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 9)
verify(result)