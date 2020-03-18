name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
marks = [ 40, 50, 60, 70 ]

mapped=list(zip(name,roll_no,marks))

#rec=dict(mapped)
print(mapped)
# print(type(mapped))
# print(type(set(mapped)))
#
diction={'Ian':25,'Caleb':23}

dic=list(diction.values())
dic.sort()

dicsort=[name for (title, year) in diction.items() if year == 25]

# print(dicsort)

print (dic)
# dictionV=list(diction.values())
# dictionV.sort()
# print(dictionV)
# print(dictionV==22)
