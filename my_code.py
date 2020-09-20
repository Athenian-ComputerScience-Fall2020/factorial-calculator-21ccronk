# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# None
# I know this is not much. I was trying to think through it and kept getting stuck.

def factorial_calc(x):   #you may choose the name of the parameter
    while x > 0:
        y = x - 1
        fac = x * y
        return y

    return fac   # be sure to return the factorial


if __name__ == '__main__':

    #num = int(input("Enter a value to factorialize: "))

   
    print(factorial_calc(4))

    
