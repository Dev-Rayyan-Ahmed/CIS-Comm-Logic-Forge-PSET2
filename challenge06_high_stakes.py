def maximize_freelance_profit(deadlines, profits):
    parent = list(range(max(deadlines) + 1))

    def find(i):
        #compressing path for speed
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    #combining and sorting by profit
    jobs = sorted(zip(deadlines, profits), key=lambda x: x[1], reverse=True)
    
    count = 0
    total_profit = 0
    
    for deadline, profit in jobs:
        #finding latest available slot
        available_slot = find(deadline)
        
        if available_slot > 0:
            count += 1
            total_profit += profit
            #merging slot with previous one
            union(available_slot, available_slot - 1)
            
    return [count, total_profit]

# Driver Code
d1 = [4, 1, 1, 1]
p1 = [20, 10, 40, 30]
print(f"Result: {maximize_freelance_profit(d1, p1)}")

d2 = [2, 1, 2, 1, 1]
p2 = [100, 19, 27, 25, 15]
print(f"Result: {maximize_freelance_profit(d2, p2)}")