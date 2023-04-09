text = input()
words = text.split(" ");
signleLetter =0
count = 0
for letter in words:
    count +=1
    for signle in letter:
        signleLetter +=1


print(signleLetter/ count)
