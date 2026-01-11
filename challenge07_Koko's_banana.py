import math

def calculate_minimum_speed(piles, k):
    left = 1
    right = max(piles)
    result = right

    while left <= right:
        mid_speed = (left + right) // 2
        hours_needed = 0
        
        for p in piles:
            hours_needed += math.ceil(p / mid_speed)
            
        if hours_needed <= k:
            result = mid_speed
    
            right = mid_speed - 1
        else:
    
            left = mid_speed + 1
            
    return result

# Driver Code
piles1 = [5, 10, 3]
k1 = 4
print(f"Piles: {piles1}, Hours: {k1}")
print(f"Minimum Speed: {calculate_minimum_speed(piles1, k1)}")

print("-" * 20)

piles2 = [5, 10, 15, 20]
k2 = 7
print(f"Piles: {piles2}, Hours: {k2}")
print(f"Minimum Speed: {calculate_minimum_speed(piles2, k2)}")