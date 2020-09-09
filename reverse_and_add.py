# You are given two linked lists representing two non-negative numbers.
#The digits are stored in reverse order and each of their nodes contain a single digit.
#Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

#     342 + 465 = 807
# Make sure there are no trailing zeros in the output list
# So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

#version one takes 2 arguments
def addem(p1,p2):
    lists = [list(p1),list(p2)]
    part1 = [str(i) for i in lists[0]]
    part2 = [str(i) for i in lists[1]]
    return(int(("").join(reversed(part1)))+int(("").join(reversed(part2))))

addem([2,4,3],[5,6,4])

#version two takes user input
def addemup():
    p1 = input("Enter your first number: ")
    p2 = input("Enter your second number: ")
    lists = [list(p1),list(p2)]
    part1 = [str(i) for i in lists[0]]
    part2 = [str(i) for i in lists[1]]
    return(int(("").join(reversed(part1)))+int(("").join(reversed(part2))))
