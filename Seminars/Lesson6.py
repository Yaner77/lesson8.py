# №1
# n = int(input())
# list1 = list()
# for i in range(n):
#     x = int(input())
#     list1.append(x)
# m = int(input())
# list2 = list()
# for i in range(m):
#     x = int(input())
#     list2.append(x)
# count = 0
# for i in range(n):
#     for j in range(m):
#         if list1[i] == list[j]:
#             count += 1
#     if count == 0:
#         print(list1[i])
#     count = 0
            
# №2
# n = int(input())
# list1 = list()
# for i in range(n):
#     x = int(input())
#     list1.append(x)
# count = 0
# for i in range(1, n - 1):
#     if list1[i - 1] < list1[i] > list1[i + 1]:
#         count += 1
# print(count)

# №3
# list1 = [1, 2, 3, 2, 3]
# count = 0
# for i in range(len(list1)):
#     for j in range(i + 1, len(list1)):
#         if i != j and list1[i] == list1[j]:
#             count += 1
# print(count)

# №4
# k = int(input())
# list1 = list()
# for i in range(k):
#     summa = 0
#     for j in range(1, i//2 + 1):
#         if i % j == 0:
#             summa += j
#     list1.append(tuple([i, summa]))
# for i in range(len(list1)):
#     for j in range(i, len(list1)):
#         if i != j and list1[i][0] == list1[j][1] and list1[i][1] == list1[j][0]:
#             print(*list1[i])
            

        
        
    