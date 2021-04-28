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
