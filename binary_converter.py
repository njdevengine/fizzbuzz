#function that does binary conversion on any number
def binary_conversion(target):
    #defines my array and sets numbers for the doubler
    array = [1]
    num = 1
    total = 0
    i = 0
    #doubler pops doubled numbers into array
    while num < target:
        num = num*2
        array.append(num)
    endarray = (len(array)-2)
    #will store bool numbers as an array
    boolie = []
    end = (len(array)-1)
    #checks if each number can be added to total
    #w/o exceeding target
    #adds '1' to boolie if true, else '0'
    for x in reversed(range(0,end)):
        if ((array[x]) + total) <= target:
            total = array[x] + total
            boolie.append("1")
        else:
            boolie.append("0")
    boolie = "".join(boolie)
    print(boolie)
