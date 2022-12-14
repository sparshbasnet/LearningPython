# arr = [3, 1, 5, 13, 18, 2, 4]
# asc = arr
# for i in range (len(asc)):
#     for j in range(i+1,len(asc)):
#         if asc[i]>asc[j]:
#             asc[i],asc[j] = asc[j], asc[i]
# print(asc)

# dec = arr
# for i in range (len(dec)):
#     for j in range(i+1,len(dec)):
#         if dec[i]<dec[j]:
#             dec[i],dec[j] = dec[j], dec[i]
# print(dec)



# l=[2,6,78,96,45,123,48,5,8]
# l.sort(reverse=False)
# print (l)


data_list = [2,4,6,8,9,5]
new_list = []
while data_list:
    minimum = data_list[0]
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)
print (new_list)