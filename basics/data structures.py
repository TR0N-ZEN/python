
# import the stuff done in singleton.py in the same folder as this file
import singleton
print(singleton.x+singleton.y+singleton.z)

set1 = {1, 2, "3"}
# unordered, unindexed, no-duplicates, unchangable (engl.: set - de.: Menge);
# has methods
# m1.union(m2) - "Vereinigung",
# m1.intersection(m2) - "Schnitt"
# m1.symmetric_difference(m2) - "Symetrische Different" and more

list1 = [1, 2, "4"]  # ordered, indexed, duplicates, changable
tuple1 = ("1", 2, "3")  # ordered, indexed, duplicates, unchangable
dictonary1 = {  # unordered, indexed, no-duplicates, changable
    "key1": 3,
    "key2": "3",
    "3": [1, 4, 1]
}


class Vehicle:
    def __init__(self, terrain):
        self.terrain = terrain

    def start(self):
        print("Generic sound.")


class Car(Vehicle):
    # equivalent to 'super().__init__(self, terrain)'
    def __init__(self, terrain, propulsion):
        Vehicle.__init__(self, terrain)
        self.propulsion = propulsion


c1 = Car("land", "electric motor")


"""
set:
    methods:
        add()                           Adds an element to the set
        clear()                         Removes all the elements from the set
        copy()                          Returns a copy of the set
        difference()                    Returns a set containing the difference
                                        between two or more sets
        difference_update()             Removes the items in this set that are
                                        also included in another, specified set
        discard()                       Remove the specified item
        intersection()                  Returns a set, that is the intersection
                                        of two other sets
        intersection_update()           Removes the items in this set that are
                                        not present in other, specified set(s)
        isdisjoint()                    Returns whether two sets have a
                                        intersection or not
        issubset()                      Returns whether another set contains
                                        this set or not
        issuperset()                    Returns whether this set contains
                                        another set or not
        pop()                           Removes an element from the set
        remove()                        Removes the specified element
        symmetric_difference()          Returns a set with the symmetric
                                        differences of two sets
        symmetric_difference_update()   inserts the symmetric differences from
                                        this set and another
        union()                         Return a set containing the union of
                                        sets
        update()                        Update the set with the union of this
                                        set and others
"""

set_0 = set([1, 2, 3, 1])
set_1 = set_0.copy()
set_1.add(4)
print(set_1)

set_2 = set_0.symmetric_difference(set_1)
print(set_2)

if set_0.issubset(set_1):
    set_0.update(set_2)
elif set_0.issuperset(set_1):
    set_1.update(set_2)
else:
    print("what the hEEEeeeel")
print(set_0.symmetric_difference(set_1))

print("noice" if set_2.pop() == 4 else "the what?")
print(set_2)


"""
array:
    methods:
        append()    Adds an element at the end of the list
        clear()     Removes all the elements from the list
        copy()      Returns a copy of the list
        count()     Returns the number of elements with the specified value
        extend()    Add the elements of a list (or any iterable), to the end
                    of the current list
        index()     Returns the index of the first element with the specified
                    value
        insert()    Adds an element at the specified position
        pop()       Removes the element at the specified position
        remove()    Removes the item with the specified value
        reverse()   Reverses the order of the list
        sort()      Sorts the list

tuple:
    methods:
        count()     Returns the number of times a specified value occurs in a
                    tuple
        index()     Searches the tuple for a specified value and returns the
                    position of where it was found

dictonary:
    mehtods:
        clear()         Removes all the elements from the dictionary
        copy()          Returns a copy of the dictionary
        fromkeys()      Returns a dictionary with the specified keys and value
        get()           Returns the value of the specified key
        items()         Returns a list containing a tuple for each key value
                        pair
        keys()          Returns a list containing the dictionary's keys
        pop()           Removes the element with the specified key
        popitem()       Removes the last inserted key-value pair
        setdefault()    Returns the value of the specified key. If the key does
                        not exist: insert the key, with the specified value
        update()        Updates the dictionary with the specified key-value
                        pairs
        values()        Returns a list of all the values in the dictionary
"""
