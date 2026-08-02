# Two Sum

## Approach 1: Hash Map (Dictionary)

My first approach was to use the target value to determine what number was needed to complete the pair.

For each number in the list, I subtract it from the target:

```
difference = target - current number
```

The resulting difference represents the other number needed to form the target pair.

For example:

```
nums = [2, 7, 11, 15]
target = 9

current number = 2
difference = 9 - 2 = 7
```

Since `7` is the missing half of the pair, I need to check whether it has already appeared in the list.

To efficiently search for this number, I used a dictionary (hash map) to store:

* The number that has already been seen
* Its corresponding index

As I iterate through the list, I check if the required difference exists in the dictionary:

* If it exists, the pair has been found, and I return the stored index and the current index.
* If it does not exist, the current number is added to the dictionary so it can be checked against future numbers.

This allows the solution to avoid comparing every possible pair and reduces the time complexity from `O(n²)` to `O(n)`.

## Approach 2: Adding a Base Case

In my second submission, I added a base case to handle lists containing exactly two numbers.

Since a list of length two can only have one possible pair, the answer will always be:

```
[0, 1]
```

By checking this condition before entering the loop, the program can immediately return the answer without performing unnecessary calculations.

## Complexity Analysis

### Time Complexity:

`O(n)`

The list is only traversed once, and dictionary lookups are performed in constant time.

### Space Complexity:

`O(n)`

The dictionary stores up to every number in the input list and its index.
