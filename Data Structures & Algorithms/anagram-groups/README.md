# Group Anagrams - Approach and Thought Process

## Approach: Character Frequency Hash Map

This problem is similar to **Valid Anagram**, where the main idea is to compare the frequency of each character in a word. Since my previous solution used `ord()` logic to count letters (albeit inefficiently), I decided to apply the same concept here.

Instead of sorting each word, I will create a unique pattern based on the frequency of each letter.

For every word, I create an array of size 26, where each index represents a letter in the alphabet:

```
index:   0  1  2  3  ... 25
letter:  a  b  c  d  ... z
```

Using:

```python
count[ord(c) - ord('a')] += 1
```

I can convert each character into its corresponding alphabet index and increase the count at that position.

For example:

```
word = "eat"

a → index 0
e → index 4
t → index 19
```

The resulting frequency pattern becomes a unique identifier:

```
[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
```

Any words that contain the exact same letters will create the same pattern.

For example:

```
eat → [1,0,0,0,1,...,1]
tea → [1,0,0,0,1,...,1]
ate → [1,0,0,0,1,...,1]
```

Since their patterns match, they belong in the same anagram group.

## Hash Map Storage

I use a hashmap (`defaultdict`) to store each pattern as a key and a list of matching words as the value.

Example:

```
{
    (1,0,0,0,1,...): ["eat", "tea", "ate"],
    (1,0,0,0,0,...): ["bat"]
}
```

Whenever a word produces an existing pattern, it is appended to that group's list.

## Why This Approach?

A sorting approach would require sorting every word:

```
eat → aet
tea → aet
ate → aet
```

While this works, sorting takes additional time.

By counting characters directly, each word is processed in linear time because we only need to examine each character once.

## Complexity Analysis

Let:

* `n` = number of words
* `k` = average length of each word

### Time Complexity

```
O(n * k)
```

Each character in every word is counted once.

### Space Complexity

```
O(n * k)
```

The hashmap stores all grouped words and their frequency patterns.
