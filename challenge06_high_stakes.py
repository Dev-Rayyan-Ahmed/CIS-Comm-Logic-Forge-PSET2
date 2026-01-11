def maximize_freelance_profit(deadlines, profits):
    #combining deadlines and profits
    jobs = []
    for d, p in zip(deadlines, profits):
        jobs.append((d, p))
    
    #sorting jobs by profit descending
    jobs.sort(key=lambda x: x[1], reverse=True)
    
    max_deadline = max(deadlines) if deadlines else 0
    #tracking empty slots (false means empty)
    timeline = [False] * (max_deadline + 1)
    
    count = 0
    total_profit = 0
    
    for deadline, profit in jobs:
        #checking slots backwards from deadline
        for t in range(min(deadline, max_deadline), 0, -1):
            if not timeline[t]:
                timeline[t] = True
                count += 1
                total_profit += profit
                break 
                
    return [count, total_profit]

# Driver Code
d1 = [4, 1, 1, 1]
p1 = [20, 10, 40, 30]
print(f"Result: {maximize_freelance_profit(d1, p1)}")

d2 = [2, 1, 2, 1, 1]
p2 = [100, 19, 27, 25, 15]
print(f"Result: {maximize_freelance_profit(d2, p2)}")