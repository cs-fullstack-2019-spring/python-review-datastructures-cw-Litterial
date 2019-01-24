def main():

    def quest1():
    # * Create a function that has a loop that quits with ```q```
    #     * Allow the User to enter names until ```q``` is entered
    # * Add each name entered to a List
    # * When the User enters ```q``` print the list of names
    #
    # ADDITIONAL REQUIREMENTS:
    # * Your code should be able to process the quit command (q) the User enters regardless of case
        def this_is_not_the_same_problem():
            array=[]                  #empty array
            while(True):
                namesforArray=input("Please enter a name. Press 'q' or 'Q' to exit. ")  #ask for input
                if (namesforArray=='q'or namesforArray=="Q"):
                    break                              #breaks out of while statement when q or Q is entered, but q will not reach the array
                else:
                    array.append(namesforArray)      #adds each name to the empty array
            for x in range(len(array)):       #prints each element
                print(array[x])
        this_is_not_the_same_problem()

    def quest2():
    # Prompts the User for which property they want to use to sort the list (e.g. ```AGE``` or ```NAME```).
    # Print the formatted list of names and ages sorted by the specified sort criteria.
    # Continue prompting the User for the sort criteria and print a sorted list until the User enters ```q``` then exit.
        myDictionaryList = [
            {
                "Name": "Kelvin",
                "Age": 30
            },
            {
                "Name": "Bob",
                "Age": 50
            },
            {
                "Name": "Alex",
                "Age": 21
            }
        ]

        def sortage(element):   #function to sort by age
            return element["Age"]   #when working with dictionaries, you must type out the key

        def sortname(element):      #function to sort by name
            return element["Name"]

        for x in myDictionaryList:   #goes through elements
            for name,age in x.items(): #goes though dictionary
                print(name+ ":",age)

        howtoSort=''
        while (howtoSort!='q'):
            howtoSort= input("How would you like to sort your dictionary? 'name or age?' ")   #ask for input
            howtoSort= howtoSort.lower()  #lowercase letters just in case of caps

            if howtoSort == "age":              #if age
                myDictionaryList.sort(key=sortage)   #sortage is now "age" from the returning it from the function
                #print(f"Dictionary sorted by age:{myDictionaryList}")
                for x in myDictionaryList:
                    for name,age in x.items():
                        print(name+ ":",age)
            elif howtoSort == "name":         #if name
                myDictionaryList.sort(key=sortname)       #gets value from sortname
                for x in myDictionaryList:
                    for name,age in x.items():
                        print(name+ ":",age)
            elif howtoSort =="q":                    #an optional message if q is entered
                print("Thank you")
            else:
                "Invalid input"



    #quest1()
    quest2()

if __name__ == '__main__':
    main()