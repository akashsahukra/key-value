0# This file have functions for create read and delete

import json
import threading
import time
import sys


def create(key, data):
    if key in d.keys():
        print(f"\n{key} already exists.")
    else:
        if len(key) > 32:
            print("\nLength of Key should be less than 32 chars")
        elif sys.getsizeof(data) > 16*1024:
            print("\nData should be less than 16KB")
        else:
            d[key] = data
            obj = json.dumps(d, indent=4)

            # write into file
            with open("key-value.json", "w")as f:
                f.write(obj)
            print("\nCreated "+key +":"+ data)


def read(key):
    # print(d)
    if key in d.keys():
        print("\n"+key + " : " + d[key])
    else:
        print(f"\nThere is no key called {key}")


def modify(key, data):
    if key not in d.keys():
        print(f"\nThere is no key called {key}")
    else:
        d[key] = data
        obj = json.dumps(d, indent=4)

        # write into file
        with open("key-value.json", "w")as f:
            f.write(obj)
        print("\nModified " + key + ":" + data)
        


def delete(key):
    if key in d.keys():
        d.pop(key)
        obj = json.dumps(d, indent=4, )

        # write into file
        with open("key-value.json", "w")as f:
            f.write(obj)
        print(f"\nDeleted {key}")
    else:
        print(f"\nError: Key Not found")

def show():
    [print('-'+i) for i in d.keys()]

def create1(key, data, time_to_live):
    t = threading.Timer(time_to_live, delete, [key])
    start = time.time()
    t.start()  # Start timer
    end = time.time() # end timer
    create(key, data)


if __name__ == "__main__":
    d = {}
    f = open('key-value.json', 'a')
    with open('key-value.json', 'r+') as f:
        try:
            d = json.loads(f.read())
        except:
            pass
    print('''

      Name     Commands

    ->Create - create key value (or) create key value time_to_live[integer]
    ->Read   - read key
    ->Delete - delete key
    ->Modify - modify key data
    ->Exit   - exit
    ->Show   - show
        ''')
    while True:
        try:
            a = input().split()
            if a[0] == "create":
                if len(a) == 3:
                    create(a[1], a[2])
                else:
                    create1(a[1], a[2], int(a[3]))
            elif a[0] == "read":
                
                read(a[1])
            elif a[0] == "delete":
                
                delete(a[1])
            elif a[0] == "modify":
                modify(a[1], a[2])
            elif a[0] == "show":
                show()
            elif a[0] == "exit":
                break
            else:
                print("\nInvalid Input")

        except:
            print("\nEnter the correct details")
