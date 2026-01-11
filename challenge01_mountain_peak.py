def count_ways_to_summit(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_ways_to_summit(n - 1) + count_ways_to_summit(n - 2)


n_steps = 45  
ways = count_ways_to_summit(n_steps)
print(f"For {n_steps} steps, the unoptimized approach found {ways} unique ways to reach the summit.")