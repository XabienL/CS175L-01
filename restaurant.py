#Xabien Loor
#Restaurant Assignment
#CS-175L

#Setting Boolean Variables
vegetarian = False
vegan = False
gluten_free = False

#inputs
response1 = input('Is anyone in your party a vegetarian? ').lower()
if response1 == 'yes':
    vegetarian = True
    
response2 = input('Is anyone in your party a vegan? ').lower()
if response2 == 'yes':
    vegan = True

response3 = input('Is anyone in your party gluten free? ').lower()
if response3 == 'yes':
    gluten_free = True

print("Here are your restaurant choices:")

#If statements
if vegetarian == False and vegan == False and gluten_free == False:
    print("Joe's Gourmet Burgers")
if vegetarian == True and vegan == False and gluten_free == False:
    print("Mama's Fine Italian")
if vegetarian == True and vegan == False and gluten_free == True:
    print("Main Street Pizza Company")
if vegetarian == True and vegan == True and gluten_free == True:
    print("Corner Cafe")
if vegetarian == True and vegan == True and gluten_free == True:
    print("The Chef's Kitchen")
#End
