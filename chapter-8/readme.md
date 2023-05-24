# Chapter 8 Notes


## Hash Table Speeds

Array Lookup = O(N)
Ordered Array Lookup = O(log(N))
Hash Map Lookup = O(1)

## Hashing

Hashing is the process of taking characters and converting it to a number

ABC = 123
DEF = 456

A very simple hash would be taking each character and coverting it to the numbered position in the alphabet.

# Inserting into a hash table

1) take the key and hash it
2) find the hash position in the array
3) insert the value at that position

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

bad = 2 * 1 * 4 = 8

arr[bad] = "evil"
arr[8] = "evil"

arr = [1, 2, 3, 4, 5, 6, 7, "evil", 9, 10, 11]

If we want to find a value and do not know its key, then we must perform an O(N) lookup, and check each value.

dab = 4 * 1 * 2 = 8
arr[dab] = "pat"

Now when we put dab into the array, we hit the same spot as "bad". We can account for this by storing another array at this position.

arr = [1, 2, 3, 4, 5, 6, 7, [{"bad","evil"}, {"dab","pat"}], 9, 10, 11]

Now when we try to access "bad" or "dab" we get a list of objects. We then linearly search the objects for the correct associated key.
With this we can store an unlimited amount of data in a hash map.

These are called collisions. Take the case when every key is a collision. We simply get an array of all the items.

This means the worst case performance of a hash map is O(N).
But in the average case when most keys don't collide we get O(1) lookup.

You should build a hash function that minimizes the number of collisions between keys. Multiplying the number of the alphabets is a poor hash function.

But if your hash map only has 10 cells, and you want to store 100 items, you are then guarentted to have many collisions.
We can up the number of cells, but then if we don't use them all, we are wasting memory.

# Hash Table use cases

If you notices that you have a giant if statement, you might be able to convert it to a hash table

case status_code:
    case 15:
        print("cheese")
    case 12:
        print("burger")
    case 9:
        print("apple")
    case 20:
        print("orange")
    case 30:
        print("chicken")
end case

status_codes = {
    15 => "cheese"
    12 => "burger"
    9 => "apple"
    20 => "orange"
    30 => "chicken"
}

my_item = status_codes[20]

In this example we can reuse the status_codes hash map, and copy it into different places. We cannot do that with a switch construct.







