import math
def calculate_minimum_speed(piles, k):

    max_pile = max(piles)

    #checking every speed from 1 up to the max pile size
    for speed in range(1, max_pile + 1):
        hours_needed = 0
        
        for p in piles:
            hours_needed += math.ceil(p / speed)
            
        #returning the first speed that fits the time limit
        if hours_needed <= k:
            return speed

    return max_pile

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