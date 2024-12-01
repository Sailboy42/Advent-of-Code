
ex_1 = [3, 4, 2, 1, 3, 3]
ex_2 = [4, 3, 5, 3, 9, 3]

def Read_Two_Column_File(file_name):
    with open(file_name, 'r') as data:
        x = []
        y = []
        for line in data:
            p = line.split()
            x.append(float(p[0]))
            y.append(float(p[1]))

    return x, y
a, b = Read_Two_Column_File('Day1.txt')
#print(a)
#print(b)
#a = ex_1
#b = ex_2
distances = []
a.sort()
b.sort()

# Part 1
for i in range(len(a)):
    distances.append(abs(a[i] - b[i]))

print(sum(distances))

# Part 2
sim_score = []
for i in range(len(a)):
    sim_score.append(b.count(a[i]) * a[i])

print(sum(sim_score))

    