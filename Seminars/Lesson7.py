# №1
# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print("ok")
# else:
#     print("fail")

# №2
# from math import pi
# def find_farthest_orbit(list_of_orbits):
#     list1 = [i for i in list_of_orbits if i[0] != i[1]]
#     list_s = [(pi * i[0] * i[1]) for i in list1]
#     max_s = list_s.index(max(list_s))
#     return list1[max_s]   
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# №3
# def same_by (characteristic, object):
#     result = True
#     list1 = [characteristic(x) for x in object]
#     for i in range(len(list1) - 1):
#         if list1[i] != list1[i + 1]:
#             result = False
#     return result    
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")