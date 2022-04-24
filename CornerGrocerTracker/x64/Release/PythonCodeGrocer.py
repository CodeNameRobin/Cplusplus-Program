import re
import string

def printsomething(v):
  print(" ttttest")
        

def ItemByName(v):
    count = 0 #number of matches found
    v = v.capitalize() #capitalizes the word entered if it wasn't already
    with open(r'''C:\Users\twist\Documents\Coding Projects\CornerGrocerTracker\x64\Release\ProduceList.txt''') as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            curr_name = line.strip()
            if curr_name == v:
                count += 1           
    f.close()

    print(v + ": ", end="")
    return count

def ItemLists(v):
    produce = [[]] # array for uniqe produce and total count 
    type(produce)
    produce_types = [] # array of just uniqe produce types
    total = 0
    lines = []
    with open(r'''C:\Users\twist\Documents\Coding Projects\CornerGrocerTracker\x64\Release\ProduceList.txt''') as f:
        lines = [line.rstrip() for line in f]
        #print(lines)
    f.close()

    for i in range(len(lines)):
        total += 1
        if i == 0: #first item on the list automaticly gets put into uniqu produce list with a count of 1
            produce[0].append(lines[i])
            produce[0].append(1)
            produce_types.append(lines[i])
            
        else:  #else it checks to see if the next item is already listed if not it is added, if it is it only adds to count
            if (lines[i] not in produce_types):
                produce.append([lines[i]])
                produce_types.append(lines[i])
                produce_index = produce_types.index(lines[i])
                produce[produce_index].append(1)
                for j in range((i+1), len(lines)):
                    if lines[i] == lines[j] and (i != j):
                        produce_index = produce_types.index(lines[i])
                        produce[produce_index][1] = (produce[produce_index][1]) + 1     
        i+=1
    if(v == 1): #if user called for only the list and count
        for i in range(len(produce)):
            char_graph = str(produce[i][1]*'-')
            name = produce[i][0]
            length_of = str((15-(len(name)))*" ")
            length_of_2 = str((15-(len(str(produce[i][1]))))*" ")
            a_list = [str(produce[i][0]), str(produce[i][1]), char_graph]
            print((str(produce[i][0]))+ length_of + (str(produce[i][1])))
    else: # if user called for list with histogram
        for i in range(len(produce)):
            char_graph = str(produce[i][1]*'-')
            name = produce[i][0]
            length_of = str((15-(len(name)))*" ")
            length_of_2 = str((15-(len(str(produce[i][1]))))*" ")
            a_list = [str(produce[i][0]), str(produce[i][1]), char_graph]
            print((str(produce[i][0]))+ length_of + (str(produce[i][1])) + length_of_2 +(str(char_graph)))
    
    print()
    print("Total          ", end="")
    return total

