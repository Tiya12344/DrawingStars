def pattern1(num_of_stars):
    """
    Goal:
    *
    * *
    * * *
    * * * *
    """
    for i in range(num_of_stars):
        for j in range(0, i+1):
            print("*", end = " ")
        print("\n")

def pattern2():
    """
    Goal:
    *
    * *
    * * *
    * * * *
    * * *
    * *
    *
    """
    num_of_stars = 4
    pattern1(num_of_stars)
    for i in range(num_of_stars, 0, -1):
        for j in range(0, i - 1):
             print("*", end = " ")
        print("\n")

def pattern3():
    """
     goal
       *
      * *
     * * *
    * * * *

    """
    num_of_stars = 4
    space = (2*num_of_stars)- 2
    for i in range( 0, num_of_stars):
        for j in range(0, space):
            print(end = " ")
        space = space-1
        for j in range(0, i + 1):
            print("*", end = " ")
        print(" ")

pattern3()


