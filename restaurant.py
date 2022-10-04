#Xabien Loor
#Restaurant Assignment
#CS-175L

#Loop
keep_going = 'yes'
while keep_going == 'yes':

#Setting Boolean Variables
    vegetarian = False
    vegan = False
    gluten_free = False
    restrictions = True
    restrictions = input("Are there any menu restrictions for anyone in your party? ").lower()
    if restrictions == 'no':
        print("Here are your restaurant choices:")
        print("Joe's Gourmet Burgers")
        print("Mama's Fine Italian")
        print("Main Street Pizza Company")
        print("Corner Cafe")
        print("The Chef's Kitchen")

#Inputs
    if restrictions =='yes':
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

#If Statements
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
    
    keep_going = input("Enter 'yes' if you would like to do another restaurant search (enter 'no' to end): ")
    

#End
