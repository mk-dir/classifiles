names=["She","Ken",[1,2,3,["a","b"]],"myself"]

print(names[0])
print(names[2][0])
print(names[2][3][1])

print(names)

names.pop()

print(names)

names.append("box")

print(names)

names.insert(0,"lighter")

print(names)
names[-1]="Plate"
print(names)