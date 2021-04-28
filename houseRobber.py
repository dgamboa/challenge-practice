def houseRobber(nums):
    if nums == []:
        return 0
    
    amount = []
    while nums != []:
        cur = nums.pop()
        if len(amount) == 0:
            amount.append(cur)
        elif len(amount) == 1:
            amount.append(max(cur, amount[0]))
        else:
            amount.append(max(cur + amount[-2], amount[-1]))
    
    return amount[-1]

# Simplified
def houseRobberSimplified(nums):
    prev_max = 0
    prev_prev_max = 0
    for n in nums:
        prev_prev_max, prev_max = prev_max, max(prev_prev_max + n, prev_max)
    return prev_max
