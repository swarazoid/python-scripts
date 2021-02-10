print("Reading text from the sample file")
try:
    file = open("sample.txt", "r")
    s = file.read()
    print(s)
    word_count = len(s.split())
    print("The sample text file has {} words!".format(word_count))
except FileNotFoundError:
    print("No matching file found")
