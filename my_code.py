# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# Help from Megan

def factorial_calc(x):   #you may choose the name of the parameter
    fac = 1
    while x > 0:
        fac = fac * x
        x = x - 1
    return fac

       # be sure to return the factorial


if __name__ == '__main__':

    x = int(input("Enter a value to factorialize: "))

   
    print(factorial_calc(x))

    
