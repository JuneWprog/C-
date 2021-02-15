#!/usr/bin/python

#to generate pretty sine wave on the terminal using ascii star character.
#The amplitude of the sinewave shall be 10 lines, and one period of the sinewave shall be 60 
#points (60 characters). Draw the zero axis using the dash character. Use dictionary indexed by the 
#amplitude to keep track of which positions on the x axis should have the star

import sys

star_record={0: [12, 13, 14, 15, 16, 17, 18], 1: [10, 11, 19, 20], 2: [9, 21], 3: [7, 8, 22, 23], 4: [6, 24], 5: [5, 25], 6: [4, 26], 7: [3, 27], 8: [2, 28], 9: [1, 29], 10: [0, 30], 11: [31, 59], 12: [32, 58], 13: [33, 57], 14: [34, 56], 15: [35, 55], 16: [36, 54], 17: [37, 38, 52, 53], 18: [39, 51], 19: [40, 41, 49, 50], 20: [42, 43, 44, 45, 46, 47, 48]}

space=' '
star='*'
dash='-'

for i in range(21):
    for j in range (60):
        if i ==10:
            if j in star_record[i]:
                sys.stdout.write(str(star)) 
            else:
                sys.stdout.write(str(dash))
            if j==59:
                print'\r'
        else:
            
            if j in star_record[i]:
                sys.stdout.write(str(star)) 
            else:
                sys.stdout.write(str(space))
            if j==59:
                print'\r'



    

           
    





