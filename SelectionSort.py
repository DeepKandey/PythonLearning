def selectionsort(list2):
    for i in range(len(list2) - 1):
        minpos = i
        for j in range(i, len(list2)):
            if list2[j] < list2[minpos]:
                minpos = j

        print(list2)
        temp = list2[i]
        list2[i] = list2[minpos]
        list2[minpos] = temp


list1 = [12, 9, 6, 3, 67, 12, 10]
selectionsort(list1)
print("Final Sorted List")
print(list1)
