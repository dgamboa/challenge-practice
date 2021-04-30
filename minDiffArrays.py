# You are given two integer arrays a and b of the same length.

# Let's define the difference between a and b as the sum of absolute differences of corresponding elements:

# difference = |a[0] - b[0]| + |a[1] - b[1]| + ... + |a[a.length - 1] - b[b.length - 1]|
# You can replace one element of a with any other element of a. Your task is to return the minimum possible difference between a and b that can be achieved by performing at most one such replacement on a. You can also choose to leave the array intact.

# Example

# For a = [1, 3, 5] and b = [5, 3, 1], the output should be minDiffOfArrays(a, b) = 4.

# If we leave the array a intact, the difference is |1 - 5| + |3 - 3| + |5 - 1| = 8;
# If we replace a[0] with a[1], we get a = [3, 3, 5] and the difference is |3 - 5| + |3 - 3| + |5 - 1| = 6;
# If we replace a[0] with a[2], we get a = [5, 3, 5] and the difference is |5 - 5| + |3 - 3| + |5 - 1| = 4;
# If we replace a[1] with a[0], we get a = [1, 1, 5] and the difference is |1 - 5| + |1 - 3| + |5 - 1| = 10;
# If we replace a[1] with a[2], we get a = [1, 5, 5] and the difference is |1 - 5| + |5 - 3| + |5 - 1| = 10;
# If we replace a[2] with a[0], we get a = [1, 3, 1] and the difference is |1 - 5| + |3 - 3| + |1 - 1| = 4;
# If we replace a[2] with a[1], we get a = [1, 3, 3] and the difference is |1 - 5| + |3 - 3| + |3 - 1| = 6;
# So the final answer is 4, since it's the minimum possible difference.

def minDiffOfArrays(a, b):
    # aggregate the absolute difference between a[n] - b[n] for each n item
    agg = []

    # track the max impact of changing each n item in a for another item in a
    # [impact of change, index to change, index to import from]
    tracker = [0, 0, 0]
    
    # loop through all items in b one by one
    for i in range(len(b)):
      diff = abs(a[i] - b[i])
      agg.append(diff)

      # loop through all items in a one by one
      for j in range(len(a)):
        cur = diff - abs(a[j] - b[i])
        if cur > tracker[0]:
          tracker = [cur, i, j]

    # change the item in a that minimizes the difference
    agg[tracker[1]] = agg[tracker[1]] - tracker[0]
    
    return sum(agg)

print(minDiffOfArrays([1,3,5], [5,3,1])) # 4
print(minDiffOfArrays([60,70,80], [1000,2000,3000])) # 5770
