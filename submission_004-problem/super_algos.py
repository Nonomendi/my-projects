
def find_min(element):
     """TODO: complete for Step 1"""
     try:
          element=list(map(int,element))
     except : 
           return-1 
     else:
          if element==[]:
               return -1
          else:
               if len(element)==1:
                    return element[0]
               else:
                    if element[0]>element[1]:
                         element.pop(0)
                    else:
                         element.pop(1)
                    return find_min(element)
# my_list=[11,2,8,14,17]
# print(find_min(my_list))

def sum_all(element):
     """TODO: complete for Step 2"""
     type_verification = all([type(x) == int for x in element])
     # print(type_verification)
     if not type_verification:
          return -1
     if len(element) == 0:
          return -1
     elif len(element) == 1:
          return element[0]
     else:
          return element[0] + sum_all(element[1:])

# print(sum_all([2,3,4,'a'])) 
# print(sum_all([2,3,4]))
# print(sum_all([]))

def find_possible_strings(character_set, n):
     my_list = []
     k = len(character_set)
     return possible_stringsRec(character_set, "", k, n, my_list)

def possible_stringsRec(character_set, prefix, k, n, my_list):
     type_verification = all([type(x) == int for x in character_set])
     if type_verification:
          return []
     if n == 0:
          #    print(prefix)
               my_list.append(prefix)
               return prefix
     
     for i in range(k):
        newPrefix = prefix + character_set[i]
        possible_stringsRec(character_set, newPrefix, k, n - 1, my_list)

     return my_list
# character_set = ['a','b','c']
# possible_strings = find_possible_strings(character_set, 3)
# print(possible_strings)



