"""
Problem: Group Anagrams
Source: Robinhood / LeetCode #49

Problem Statement:
Given an array of strings, group anagrams together.

Example:
Input: ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
Output: [['eat', 'ate', 'tea'], ['apt', 'pat'], ['now']]

Solution Approach:
Create a canonical signature for each word by sorting its letters alphabetically,
then use this signature as a dictionary key to group words together.

Complexity:
Time: O(n * k log k) where n = number of words, k = average word length
Space: O(n * k) to store all words and their signatures

Key Insights:
1. Anagrams share the same sorted letter sequence
2. Dictionary grouping provides efficient O(1) average-time lookups
3. The sorted signature serves as a fingerprint that ignores letter order

Reflections:
A foundational problem that demonstrates the power of canonical forms.
Instead of the naive O(n²) pairwise comparison, the signature approach achieves
O(n) grouping. The elegance lies in the simplicity: anagrams reduce to identical
strings when sorted.

I considered alternative approaches like prime multiplication (mathematically
elegant but practically inefficient) and frequency arrays (good for large alphabets).
The sorted string approach won due to Python's highly optimized string operations.

This also prompted thinking about real-world considerations: case sensitivity,
sorting preferences, and edge cases like empty strings. The optional parameters
show how a production solution might evolve from a basic algorithm.

The core lesson: often the best solution isn't the most clever, but the one that
leverages language strengths while maintaining clarity.
"""

from collections import defaultdict
from typing import List

def group_anagrams(words: List[str], 
                   case_sensitive: bool = False,
                   sort_groups: bool = False,
                   sort_within_groups: bool = False) -> List[List[str]]:
    """
    Group anagrams with configurable options.
    
    Args:
        words: List of strings to group
        case_sensitive: If False, 'Eat' and 'ate' are considered anagrams
        sort_groups: Sort groups by size (largest first)
        sort_within_groups: Sort words within each group alphabetically
        
    Returns:
        List of anagram groups
    """
    anagram_groups = defaultdict(list)
    
    for word in words:
        word_to_process = word if case_sensitive else word.lower()
        signature = ''.join(sorted(word_to_process))
        anagram_groups[signature].append(word)
    
    result = list(anagram_groups.values())
    
    if sort_within_groups:
        result = [sorted(group) for group in result]
    
    if sort_groups:
        result.sort(key=lambda x: (-len(x), x[0]))
    
    return result


if __name__ == "__main__":
    # Test cases from problem statement
    basic_test = ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
    print("Basic test:")
    print(f"Input: {basic_test}")
    print(f"Output: {group_anagrams(basic_test)}")
    
    # Test with case variations
    case_test = ['eat', 'Eat', 'ate', 'Tea', 'now', 'OWN']
    print("\nCase-insensitive test:")
    print(f"Input: {case_test}")
    print(f"Output: {group_anagrams(case_test, case_sensitive=False)}")
    
    # Test with sorting options
    print("\nWith all sorting enabled:")
    test_words = ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
    result = group_anagrams(test_words, 
                           sort_groups=True, 
                           sort_within_groups=True)
    print(result)
    
    # Edge cases
    print("\nEdge cases:")
    print(f"Empty list: {group_anagrams([])}")
    print(f"Single word: {group_anagrams(['hello'])}")
    print(f"Empty strings: {group_anagrams(['', 'a', ''])}")