#script returns the mean of an array
my_list = [1,4,6,8,9,10,44,2,30]

def mean(list):
    total = 0
    for i in my_list:
        total = i+total
    average = total / len(my_list)
    print(str(average))
mean(my_list)
