def double_index(lst, index):

# Checks to see if index is too big
    if index >= len(lst):
        return lst
    
    else:

# Gets the original list up to index
        new_lst = lst[0:index]

# Adds double the value at index to the new list 
        new_lst.append(lst[index]*2)

# Adds the rest of the original list
        new_lst = new_lst + lst[index+1:]
        return new_lst

print(double_index([3, 8, -10, 12], 2))
 
#########
def double_index2(lst2, index2):
    if index2 >= len(lst2):
        return lst2
    else:
        new_list = list(lst2)
        new_list[index2] = new_list[index2] * 2
        return new_list

# Uncomment the line below when your function is done
print(double_index2([3, 8, -10, 12], 2))
print(double_index2([3, 8, -10, 12], 3))

# Exercice 5:
# my solution
#Write your function here
def middle_element(lst):
  if len(lst) % 2 == 0:
    index1 = int(len(lst) / 2 - 1)
    index2 = int(len(lst) / 2)
    sum = (lst[index1] + lst[index2]) / 2
    return sum
  else:
    index_odd = (len(lst) - 1) / 2
    index_odd = int(index_odd)
    return lst[index_odd]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

# solution
def middle_element2(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

print(middle_element2([5, 2, -10, -4, 4, 5]))
