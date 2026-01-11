def find_longest_mirror_length(s):
    
    def solve(start, end):
        # Base Case: If indicators cross, empty string
        if start > end:
            return 0
        
        # Base Case: One character left
        if start == end:
            return 1
            
        #  Match found
        if s[start] == s[end]:
            return 2 + solve(start + 1, end - 1)
            
        return max(solve(start + 1, end), solve(start, end - 1))

    return solve(0, len(s) - 1)

# Driver Code
test_str = "bbabcbcab"
length = find_longest_mirror_length(test_str)
print(f"Input Sequence: '{test_str}'")
print(f"Longest Palindromic Subsequence Length: {length}")