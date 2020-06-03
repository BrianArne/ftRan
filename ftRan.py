import random
import sys
import time

Title = "It is time to randomize!!!"
End = "It is no loner time to randomize!!!"

def iterate(f_list):
    random.seed()
    input()
    while len(f_list) > 0:
        type_print(f_list.pop(random.randrange(len(f_list))), periods=True)
        if len(f_list) == 0:
            break
        input()
    print()
    type_print(End)
    print()

def process_list():
    iterate(sys.argv[1:])

def process_file():
    f = open(sys.argv[1])
    c_list = f.read()
    fasties = c_list.split(",")
    fasties[-1] = fasties[-1].strip()
    iterate(fasties)
    f.close()

def type_print(word, periods=False):
    if periods:
        for x in range(0,5):
            print('.', end='', flush=True)
            time.sleep(.05)
    for c in word:
        print(c, end='', flush=True)
        time.sleep(.05)
    print()

########
# MAIN #
########

print()
type_print(Title)
if len(sys.argv) < 1:
    print("Usage: ftRan.py [file] | [NameList]")
    exit()

random.seed()
if len(sys.argv) == 2:
    process_file()
else:
    process_list()
