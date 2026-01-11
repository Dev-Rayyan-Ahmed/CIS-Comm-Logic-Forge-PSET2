def can_balance_scales(arr):
    total_weight = sum(arr)
    
    if total_weight % 2 != 0:
        return False
        
    target = total_weight // 2
    n = len(arr)
    
    def check_subset(index, current_sum):
        if current_sum == target:
            return True
        if index >= n or current_sum > target:
            return False
            
        return check_subset(index + 1, current_sum + arr[index]) or check_subset(index + 1, current_sum)

    return check_subset(0, 0)

stones = [1, 5, 11, 5]
result = can_balance_scales(stones)
print(f"Can the stones {stones} be split into two equal bags? {result}")