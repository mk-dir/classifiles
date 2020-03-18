def diff(list):
    list.sort(reverse=True)
    print(list)

    return list[0]-list[-1]


x=diff([1,2,4,5])

print(x)


def checkString(string1,string2):
    if len(string1)==len(string2):
        return "True"
    else:
        return "False"

print(checkString("AB","CD"))


def conv(dic):
    dic2=[]
    dic=list(dic.items())
    print(dic)
    for each in dic:
        dic2.append(list(each))
    return dic2

users={"a":1,"b":2}

print(conv(users))


inventory={
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}

def profit(inv):
    return (inv["sell_price"]-inv["cost_price"])*inv["inventory"]

print(profit(inventory))