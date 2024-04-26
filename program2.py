def longest_substring(s: str) -> int:
    """
    Implementation of the longestSubstring function.
    """
    longest_substring_length = 0
    
    for i in range(len(s)):
        current_string_set = set()
        
        for x in range(i, len(s)):
            if s[x] in current_string_set:
                break
            else:
                current_string_set.add(s[x])
        
        longest_substring_length = max(
            longest_substring_length,
            len(current_string_set)
        )
    
    return longest_substring_length


    """"
    
    Implement the function longest_substring 
    using the provided longest_substring function to find 
    the length of the longest substring without repeating characters.

    """ 
    pass