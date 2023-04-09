#your code goes here
x = str(input());
y = str(input());
totalLetters = len(x);
letterCount = x.count(y);

percentage = int((letterCount/totalLetters) * 100)

print(percentage);