>>> import random
>>> import math
>>> smaller = int(input("Enter the smaller number: "))
Enter the smaller number: 4
>>> larger = int(input("Enter the larger number: "))
Enter the larger number: 8
>>> count = 0
>>> print()

>>> while True:
...      count += 1
...       myNumber = (smaller + larger) // 2
...       print('%d %d' % (smaller, larger))
...       print('Your number is %d' % myNumber)
...       choice = input('Enter =, <, or >: ')
...       if choice == '=':
...            print("Hooray, I've got it in %d tries" % count)
...            break
...            elif smaller == larger:
...                 print("I'm out of guesses, and you cheated")
...                 break
...                 elif choice == '<':
...                      larger = myNumber - 1
...                      else:
...                           smaller = myNumber + 1
...                           if choice.lower() == 'cheat':
...                                 print("You cheated! The game is over.")
...                                 break
...
  File "<python-input-6>", line 3
    myNumber = (smaller + larger) // 2
IndentationError: unexpected indent
>>>
