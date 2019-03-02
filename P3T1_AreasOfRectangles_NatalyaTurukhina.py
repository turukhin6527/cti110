#This program asks for the length and width of two rectangles.
#This program determines which rectangle has the greates area, or the areas are equal.

#Get the dimentions of rectangle 1.
length1 = int(input('Enter the length of the rectangle 1: '))
width1 = int(input('Enter the width of the rectangle 1: '))

#Get the dimentions of rectangle 2.
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))             

#Calculate the areas of the rectangles.
area1 = length1*width1
area2 = length2*width2

#Determine which rectangle has the greatest area.
if area1 > area2:
    print('Rectangle 1 has the greatest area.')
elif area1 < area2:
    print('Rectangle 2 has the greatest area.')
else:
    print('Both rectangles have the same area')         
