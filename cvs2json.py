# CVS to JSON
# cvs2json.py
# Created by Mauro J. Pappaterra on 31 of March 2018.
import os.path as p
import codecs
import json as j

HOME_SCREEN = """>>>                               <<<
>>> .csv to .json file converter  <<<
>>>                               <<<"""

print(HOME_SCREEN)

again = True
while (again):
    # Ask user to enter path to external file
    path = input("\nEnter path to external .csv file:\n")
    while (not p.isfile(path) or (path[-4:] != '.csv')):
        path = input("\nERROR!: not a valid path or .csv file! \nEnter path to external .csv file:\n")

    #FOR TESTING PURPOSES
    #path = 'example-data.csv'

    with codecs.open(path, 'r', encoding='utf8') as myFile:
        full_cvs = myFile.readlines()  # saves each line of the text into a list
        #print(full_cvs)

    keys = full_cvs[0].replace('\r','').replace('\n','').split(',')
    no_keys = len(keys)
    json = []
    #print(keys)

    for line in full_cvs[1:]:
        new_line = line.replace('\r','').replace('\n','').split(',')
        #print(new_line)
        index = 0
        dictionary = {}

        while (index < no_keys):
            dictionary[keys[index]] = new_line[index]
            index +=1
        #print(dictionary)
        json.append(dictionary)

    #print(json)
    with open (path[:-4] + '.json', 'w') as file:
        file.write (j.dumps(json, indent=4))

    print("\nSUCCESS! The .csv file has been converted to .json")

    again = input("\nWant to convert another .csv file? y/n\n").lower()
    while (again != 'y' and again != 'n'):
        again = input("Not a valid option. Enter 'y' for yes or 'n' for no!").lower()
    again = (again == 'y')

print("\n-EXIT BY USER-")


