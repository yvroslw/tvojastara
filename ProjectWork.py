txt = open("file.txt", 'r', encoding='utf8')
word = input("Enter word --> ")
list = txt.read().split('\n\n')
c = 0
for i in list:
    for a in i.split():

        if a == word:
            print("Required paragraph: " + i + "\n")
            c += 1
            break

if c == 0:
    print("Word haven't been found.")
