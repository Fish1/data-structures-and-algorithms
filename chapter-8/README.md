### Notes

Hash tables have O(1) access time, given you have a key to the value you're looking for.

Hash tables can be used to link data together, or cleaverly used to create speedy algorithms.

Under the hood, hash maps are generally implemented as arrays. A "hashing" algorithm with take you're provided key, transform it into a number, and insert it into an array.

Sometimes these hashing algorithms with result in data being inserted into the same spot of the array. To solve this issue, each spot in the array will contain another array, where your value is stored along side they key.

In the worst case possible, all keys will map to the same spot, resulting in a lookup time of O(n). To mitigate this, hash tables will expand the number of availible cells in the array. Resulting in there being a better chance of data not being stored in the same cell.

Because of this expanding array feature, properly implemented hash maps must balance their size and speed. Larger hash maps take up more space and may be faster, while smaller hash maps take up less space and may be slower.

### Exercises

1) answer1.go

2) answer2.go

3) answer3.go

4) answer4.go