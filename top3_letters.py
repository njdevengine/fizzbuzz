#given user input of a string, return 3 most commonly repeated letters
def top():
    string = input()

    array = sorted(string)
    unique = list(set(string))
    counts = []
    for i in unique:
        count = 0
        for letter in array:
            if letter == i:
                count+=1
        counts.append(count)

    rank = []
    for check in reversed(range(max(counts)+1)):
        for i in range(len(counts)):
            if counts[i] == check:
                rank.append(unique[i])

    top_3 = rank[:3]
    print("\n")
    for i in top_3:
        print(i)

if __name__ == "__main__":
    top()
