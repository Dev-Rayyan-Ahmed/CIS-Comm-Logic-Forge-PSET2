def min_cancelled_bookings(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])

    removals = 0
    current_idx = 0
    next_idx = 1
    
    while next_idx < len(intervals):
        last_valid_end = intervals[current_idx][1]
        next_start = intervals[next_idx][0]
        
        if next_start < last_valid_end:
            # Overlap detected: remove the 'next' one
            removals += 1
        else:
            # no overlap: update current pointer to this valid meeting
            current_idx = next_idx
            
        next_idx += 1
            
    return removals

#Driver Code
print()
intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
print("Example 1 Output:", min_cancelled_bookings(intervals1))