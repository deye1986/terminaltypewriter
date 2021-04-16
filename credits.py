import sys
from time import sleep


def type_writer(x): 
    '''apply a typewriter style graphic to the output in the terminal'''
    for char in str(x):
        sleep(0.06) # speed
        sys.stdout.write(char) 
        sys.stdout.flush()

type_writer('''
    

    
    CREDITS


    * * * * DEVELOP 29/03/2021 * * * * 
    CodeNation Open Systems And Enterprise -
    

    * *  Typewriter Graphic * *
    Pushed to my GitHub page soon!!!
    github.com/deye1986

    Go to wearecodenation.com to find out more
    about the Open Systems course.....

    Massive thank you......
    CN Mike  - Tutor, residence: Mount Doom
    CN Leon    - Stand in
    CN Dan - Director
    CN Ezra    - Admissions

    And,

    Thank you for watching :)

    ***** GAME OVER!!!!! *****

    Continue?????????

    
''')