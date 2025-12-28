
def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [-2, 45, 0, 11, -9]

# bubbleSort(data)

# print('Sorted Array in Ascending Order:')
# print(data)

'''Question:Partition the labels in the given string '''
Input=  "ababcbacadefegdehijhklij"
Output= [9, 7, 8]
def partion_logic(st):
  last_index={ch:i for i,ch in enumerate(st)}
  start,end=0,0
  part=[]
  for i,ch in enumerate(st):
    end=max(end,last_index[ch])
    if i==end:
      part.append(end-start+1)
      start=i+1
  print(part)

partion_logic(Input)

    
