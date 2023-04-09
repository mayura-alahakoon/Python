s1 = input()
s2 = input()
s1Words = set(s1.split(" "));
s2Words = set(s2.split(" "));
commonwords = s1Words & s2Words
print(len(commonwords)); 