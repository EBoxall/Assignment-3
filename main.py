
#splits string into list
charlist = [(s) for s in input("please input a string of charcters seperated by spaces\n").split()]

#function 1 that uses inputted string that has been turned into a list
def listsplitter (charlist):
  #define empty lists
  stringlist = []
  numlist = []
  #create fr loop that seperates the two into their respective lists
  for i in (charlist):
    if i.isdigit() == True:
      numlist.append(i)
    elif i.isdigit() == False:
      stringlist.append(i)
  #returns both lists
  return stringlist, numlist

#turns variable y into the numbers list
x, y = listsplitter(charlist)
#turns y into an integer list
y = [int(i) for i in y]

#function 2 that uses the numbers list
def numbersorter(y):
  #creates empty lists
  result = []
  orderedlist = []
  #sorts every second number in reverse order into a new list
  orderedlist = sorted(y[1::2],reverse = True)
  #deletes every second number from the old list
  del y[1::2]
  #adds empty spaces based off how long both lists are combined
  result = [None]*(len(y)+len(orderedlist))
  #adds the values of list y to every second number starting at 0
  result[::2] = y
  #adds the values of list orderedlist to every second number starting at 1
  result[1::2] = orderedlist
  #returns the result
  return result

#prints the lists/answers
print("The string you inputted has been seperated into numbers and words\n",listsplitter(charlist))
print("The new ordered numberstring skipping every second number is\n", numbersorter(y))
