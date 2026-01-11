def min_cancelled_bookings(intervals):
    # sort by start time so we can process time wise
    intervals.sort(key=lambda x: x[0])
    n = len(intervals)
    memo = {}

    def solve(index, previous_end_time):
        state = (index, previous_end_time)
        if state in memo:
            return memo[state]
        
        # Base case: checked all meetings
        if index == n:
            return 0
        
        current_start, current_end = intervals[index]
        
        #skip this meeting and move on
        skip = solve(index + 1, previous_end_time)
        
        # attend this meeting if the time slot is free
        take = -1
        if current_start >= previous_end_time:
            take = 1 + solve(index + 1, current_end)
            
        result = max(skip, take)
        memo[state] = result
        return result

    # start checking from the first meeting
    max_kept = solve(0, float('-inf'))
    
    # cancellations = Total meetings minus the ones we could keep
    return n - max_kept

#Driver Code
schedule = [[1, 2], [2, 3], [3, 4], [1, 3]]
removals = min_cancelled_bookings(schedule)

print(f"Schedule: {schedule}")
print(f"Minimum Cancellations Needed: {removals}")