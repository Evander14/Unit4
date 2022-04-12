'''
###########
Lab 4.03
###########

Instructions
In this lab we will be drawing images using nested for loops.

For each of the following problems, you will write a function that will draw the desired output. You may use an extra function if you find it helpful.

1.  Write a function, draw_7, to draw the 7x7 square (shown below)

    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
2.  Write a function stars_and_stripes, that will draw a 3 sets of rows. 1st a row of 7 stars followed by a row of 7 dashes (shown below)

    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
3.  Write a function, increasing_triangle that will print out the following:

    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    1 2 3 4 5 6
    1 2 3 4 5 6 7

4. Write a function, vertical_stars_and_stripes that will print out the following:

    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -

5.  Use a function to create your own pattern or drawing. Some possible pattern ideas:

    Write a function that will print a border around a 7x7 square (shown below)

        * * * * * * * *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * * * * * * * *
    Write a function that will print the following balanced_triangle.

        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
        1 2 3 4 5 6
        1 2 3 4 5 6 7
        1 2 3 4 5 6
        1 2 3 4 5
        1 2 3 4
        1 2 3
        1 2
        1
    Write a function that will print the following triangle.

        *
        ***
        *****
    
'''


'''
# 1
def draw_7():
    #7 rows of stars
    for i in range(7):
        
        #row of stars
        my_string = ''
        for i in range(7):
            my_string += ' *'
        print(my_string)
draw_7()
'''

'''
# 2
def stars_and_stripes():
    for i in range(3):
        star_string = ''
        for i in range(7):
            star_string += ' *'
        print(star_string)

        dash_string = ''
        for i in range(7):
            dash_string += ' -'
        print(dash_string)
stars_and_stripes()
'''

'''
#3
def increasing_triangle():
    triangle_string = ''

    for i in range(1,8):
        triangle_string += " " + str( i)
        print(triangle_string)

def increasing_deacreasing_triangle():
    increasing_triangle()
'''


def vertical_stars_and_stripes():
    #7 rows of stars
    for i in range(3):
        
        #row of stars
        my_string = ''
        for i in range(3):
            my_string += '  *'
        print(my_string)

        my_string = ''
        for i in range(4):
            my_string += ' -'
        print(my_string)
vertical_stars_and_stripes()