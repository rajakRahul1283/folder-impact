list1 = list(map(int, input("Enter 4 integers for list1 (space-separated): ").split()))
list2 = list(map(int, input("Enter 4 integers for list2 (space-separated): ").split()))
index_pairs = [(0, 0), (1, 2), (3, 3)]
compatible = True
for i1, i2 in index_pairs:
    if list1[i1] <= list2[i2]:
        compatible = False
        break

if compatible:
    print("is a compatible array")
else:
    print("Not compatible array")
