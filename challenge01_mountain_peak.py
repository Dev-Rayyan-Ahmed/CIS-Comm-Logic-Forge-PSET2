def count_ways_to_summit(n):
    if n == 1:
        return 1
    
    first = 1
    second = 2
    
    for _ in range(3, n + 1):
        current = first + second
        first = second
        second = current
        
    return second

n_steps = 45
ways = count_ways_to_summit(n_steps)
print(f"For {n_steps} steps, Found {ways} unique ways to reach the summit.")