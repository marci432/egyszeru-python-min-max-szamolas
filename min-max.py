list=[18,67,32,54,71,99,22,61,92,67,42]
min=999
max=0
for x in list:
    if min > x:
        min = x
    if max < x:
        max = x
print ("a legnagyobb szam a listaban:" , max)
print ("a legkisebb szam a listaban:" , min)
print(list)
