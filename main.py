def separator():
  print('\n' + 20 * "=" + '\n')

# create list with values
scores = [1000, 500, 400, 300]
print(scores)
length = len(scores)
print("There are", length, "items in scores")

separator()

print("Original scores")
for i in range(len(scores)):
  print(scores[i])

# double each value in list
for i in range(len(scores)):
  scores[i] = scores[i] * 2

print("\nDoubled scores")
for i in range(len(scores)):
  print(scores[i])

separator()

#largest value in list
print("Largest value: ", max(scores))
#smallest value in list
print("Smallest value: ", min(scores))
# sort list in ascending order
scores.sort() 
# print list after sorting
print("List after sorting")
for score in scores:
  print(score)

separator()

scores = [1000, 500, 400, 300]
bonus = []
for score in scores:
  bonus.append(score * .1)
print("Bonus list")
for b in bonus:
  print(b)

print("\nTotal scores with bonus")
for i in range(len(scores)):
  print(scores[i] + bonus[i])

separator()

menu = ["Coffee", "Latte", "Tea", "Hot Chocolate"]

def printMenu(menu):
  count = 1
  for drink in menu:
    print(str(count) + ". " + drink)
    count += 1

printMenu(menu)

def getChoice():
  choice = -1
  while choice < 1 or choice > 4:
    choice = int(input("Enter choice: "))
  return choice


customerchoice = getChoice()
print("\nYou ordered", menu[customerchoice - 1])

separator()

print("\nWe ran out of tea - let's replace the tea item in the menu with something else.\n\n")

menu[2] = "Caffe Mocha"

printMenu(menu)
customerchoice = getChoice()
print("\nYou ordered", menu[customerchoice - 1])

separator()

sales = {"coffee" : 0,
         "latte" : 0,
         "tea" : 0,
         "hot chocolate" : 0
}

while True:
  customerchoice = input("Enter drink name: ")
  if customerchoice in sales:
    sales[customerchoice] += 1
  enter = input("Order again? (y/n)")
  if enter != 'y':
    break

print("\nSales totals: ")

for item in sales.items():
  print(item)
  print("Drink:", item[0], "Quantity:", item[1])


separator()

message = input("Enter message: ")

letterfreq = {}

for character in message:
  if character != ' ':
    if character in letterfreq:
      letterfreq[character] += 1
    else:
      letterfreq[character] = 1

for item in letterfreq.items():
  print(item)
