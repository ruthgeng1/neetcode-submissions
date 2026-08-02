# Valid Anagram

## Initial Approach

My first approach was to use the Unicode values of each character to create a numerical representation of the strings.

Since anagrams contain the same characters, I reasoned that each character would have the same Unicode value. I calculated the sum of the squared Unicode values for each string and compared the results. If the sums were equal, I assumed the strings were anagrams.

However, I realized that this approach is not collision-proof. Different combinations of characters can produce the same sum, meaning two non-anagrams could incorrectly be considered anagrams.

## Improved Approach: Character Frequency Counting

To solve this issue, I used a dictionary to store the frequency of each character in both strings.

Each character is used as a key, and its occurrence count is stored as the value. By comparing the two dictionaries, we can determine whether both strings contain the exact same characters with the same frequencies.

### Complexity
- Time Complexity: `O(n)` because each string is iterated through once.
- Space Complexity: `O(k)` where `k` is the number of unique characters.

## Solution Progression

- Initial solution: Used Unicode sums to compare strings.
- Identified that the hashing method was not collision-proof.
- Final solution: Used character frequency maps to guarantee correctness.
