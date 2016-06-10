
import random
#gather array of 100 random numbers with range of 0-100000. 
my_randoms = random.sample(xrange(100001), 100)


def bubbleSort(unsorted_list):
    length = len(unsorted_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if unsorted_list[i] > unsorted_list[i+1]:
                sorted = False
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]

bubbleSort(my_randoms)
print my_randoms
