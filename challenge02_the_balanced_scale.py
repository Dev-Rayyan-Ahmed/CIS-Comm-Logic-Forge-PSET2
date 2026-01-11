def can_balance_scales(arr):
    total_weight = sum(arr)
    
    if total_weight % 2 != 0:
        return False
        
    target = total_weight // 2
    possible_sums = {0}
    
    for stone in arr:
        current_sums = list(possible_sums)
        for s in current_sums:
            new_sum = s + stone
            if new_sum == target:
                return True
            if new_sum < target:
                possible_sums.add(new_sum)
                
    return target in possible_sums


test_stones = [[1, 5, 11, 5],[1,2,4],[1,2,2,1]]
for stones in test_stones:
    result = can_balance_scales(stones)
    print(f"Can the stones {stones} be split into two equal bags? {result}")