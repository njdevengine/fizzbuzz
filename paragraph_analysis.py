with open ("paragraph_1.txt", "r") as myfile:
    data=myfile.readlines()
    data = ''.join(data)
print(data)

#Approximate word count
wordarray = data.split(" ")
print("Approximate Word Count: " + str(len(wordarray)))
#Approximate sentence count
sentencearray = data.split(".")
print("Approximate Sentence Count: " + str(len(sentencearray)))
#Approximate letter count (per word)
wordlenarray = []
for word in wordarray:
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace("(","")
    word = word.replace(")","")
    wordlenarray.append(len(word))
totalchars = 0
for num in wordlenarray:
    totalchars = totalchars + num
print("Average Letter Count: " +str(round(totalchars/(len(wordlenarray)),2)))
#Average sentence length (in words)

##WIP

sentencelenarray = []
ntotal = 0
length = len(sentencearray)
length2 = len(sentencelenarray)
for num in range(-6,length):
    sentencelenarray.append(len((sentencearray[num]).split(" ")))
print(sentencelenarray)
