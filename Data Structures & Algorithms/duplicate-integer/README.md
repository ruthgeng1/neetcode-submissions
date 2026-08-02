# Contains Duplicate

## Problem
Given an integer array `nums`, determine if any value appears at least twice in the array. Return `true` if there is a duplicate, otherwise return `false`.

## Approach 1: Sorting (O(n log n))

My initial approach was to sort the array first. After sorting, duplicate values would appear next to each other, making them easier to detect.

I created a temporary variable to store the previous number and iterated through the sorted list. If the current number matched the previous number, a duplicate was found.

### Complexity
- Time Complexity: `O(n log n)` due to sorting
- Space Complexity: `O(1)` (excluding the sorting algorithm's internal space)

## Approach 2: Hash Set (O(n))

After reviewing the first solution, I realized that a hash set would be a more efficient approach. Since sets only store unique values, comparing the size of the set with the original array allows us to determine whether duplicates exist.

If the length of the set is smaller than the original array, it means some values were removed due to duplication.

The final implementation was simplified into a one-line solution.

### Complexity
- Time Complexity: `O(n)` because each element is processed when creating the set
- Space Complexity: `O(n)` because the set stores up to every unique element

## Solution Progression

- Submission 1: Implemented sorting approach (`O(n log n)`)
- Submissions 2-4: Experimented with hash set optimization
- Final Solution: Reduced the solution to a concise one-line implementation using a set (`O(n)`)
