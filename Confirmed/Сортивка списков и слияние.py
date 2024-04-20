list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
sorted_list = []
sorted_list.extend(list1), sorted_list.extend(list2)
sorted_list.sort()
for i_elem in sorted_list:
    while sorted_list.count(i_elem) > 1:
        sorted_list.remove(i_elem)
print(sorted_list)