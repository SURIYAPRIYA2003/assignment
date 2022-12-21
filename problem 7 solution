n = int(input())
details = []
for i in range(n):
    name = input()
    grade = float(input())
    details.append([name, grade])

details.sort(key=lambda x: x[1])
sorted_list1 = []
for i in details:
    if i[1] == details[1][1]:
        sorted_list1.append(i[0])
sorted_list2 = sorted(sorted_list1)
for i in sorted_list2:
    print(i)
