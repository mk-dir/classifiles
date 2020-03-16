def test(a):
    for each in a:
        if each%2==1:

            print(each," is odd")
        else:
            print(each," is Even")


test((13,12,11,7))

#Arguement is an input to a function. It is placed inside the function call

#a=(13,12,11,7)

def sumn(*args):

    total=0
    for each in args:
        total=total+each

    print(total)

sumn(1,2,3,4,5,6,7,8,9,0,11,13)

# string formatting??

day=420
print("I can't wait for {} to come".format(day))