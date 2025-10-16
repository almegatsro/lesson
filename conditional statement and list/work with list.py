lst = ['apple', 'guava', 'mango', 'Banana', 'Kiwi', 'watermelon', 'pawpaw']
print('length of the list is: ', len(lst))
print('first item in the list is: ', lst[0])
print('last item in the list is: ', lst[-1])

lst.append('orange')
print('list after adding orange: ', lst)

lst.remove('Banana')
print('list after removing Banana: ', lst)

lst.sort()
print('list after sorting: ', lst)

lst.reverse()
print('list after reversing: ', lst)

print("multiplying list by 2: ", lst * 2)
print("slicing the list from index 1 to 4: ", lst[1:5])

lst.clear()
print('list after clearing all items: ', lst)