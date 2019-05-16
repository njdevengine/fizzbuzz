import os
with open("Output.txt", "w") as text_file:
    for i in os.walk("C:\\"):
        text_file.write(str(i))
    text_file.close()
