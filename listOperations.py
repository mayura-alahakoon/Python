data = [[23, 11, 5, 14], [8, 32, 20, 5]]

color = input()
total = 23 + 11 + 5 + 14 + 8 + 32 + 20 + 5

if color == "brown":
    print(int((data[0][0] + data[1][0])*100/total))
elif color == "blue":
    print(int((data[0][1]+data[1][1]*100/total)))
elif color == "green":
    print(int(data[0][2]+data[1][2]*100/total))
else:
    print(int((data[0][3] + data[1][3])*100/total))

data = [
    [23, 11, 5, 14],
    [8, 32, 20, 5]
]

# input_color = input().lower()

# total = sum(sum(data, []))
# colors = {'brown': 0, 'blue': 1, 'green': 2, 'black': 3}
# col_index = colors[input_color]

# male_count = data[0][col_index]
# female_count = data[1][col_index]

# percentage = (male_count + female_count) / total * 100
# result = round(percentage)

# print(result)