charlist = [(s) for s in input("please input a string of charcters seperated by spaces\n").split()]

def listsplitter (charlist):
  stringlist = []
  numlist = []
  for i in (charlist):
    if i.isdigit() == True:
      numlist.append(i)
    elif i.isdigit() == False:
      stringlist.append(i)
  return stringlist, numlist

x, y = listsplitter(charlist)
y = [int(i) for i in y]

print(y)
def numbersorter(y):
  result = []
  orderedlist = []
  orderedlist = sorted(y[1::2],reverse = True)
  del y[1::2]
  result = [None]*(len(y)+len(orderedlist))
  result[::2] = y
  result[1::2] = orderedlist
  return result


print("The string you inputted has been seperated into numbers and words\n",listsplitter(charlist))
print("The new ordered numberstring skipping every second number is\n", numbersorter(y))
