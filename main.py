
def listsplitter (charlist):
  stringlist = []
  numlist = []
  for i in (charlist):
    if i.isdigit() == True:
      numlist.append(i)
    elif i.isdigit() == False:
      stringlist.append(i)
  return stringlist, numlist

def numbersorter(numlist):
  orderedlist = []
  for index, element in enumerate(numlist):
    if index % 2 != 0:
      orderedlist.append(element)
  orderedlist.sort(reverse=True)
  return orderedlist

charlist = [(s) for s in input("please input a string of charcters seperated by spaces\n").split()]
print(listsplitter(charlist))