#Given 2 int arrays, a and b, each length 3,
#return a new array length 2 containing their middle elements.

def middle_way(a,b):
    index_a = int((len(a)-1)/2)
    index_b = int((len(b)-1)/2)
    new_array = [a[index_a],b[index_b]]
    print (new_array)

middle_way([1, 2, 3], [4, 5, 6]) #→ [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) #→ [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) #→ [2, 4]
middle_way([1,4,7,9,4],[1,2,3]) #→ [7, 2]



#Given an array of ints, return True if the array is length 1 or more,
#and the first element and the last element are equal.

def same_first_last(nums):
  if len(nums) >=1 and nums[0] == nums[-1]:
    return True
  else:
    return False

print(same_first_last([1, 2, 3])) #→ False
print(same_first_last([1, 2, 3, 1])) #→ True
same_first_last([1, 2, 1]) #→ True
