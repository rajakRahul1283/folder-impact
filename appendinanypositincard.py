my_list = list(map(int, input("Enter the list: ").split()))
element = 10
position = 3
new_list = []
for i in range(len(my_list)):
     if i == position-1:
        new_list.append(element)
     if i < len(my_list):
        new_list.append(my_list[i])
print(new_list)
