# **************************************************************************** #
# ************** Merge Intervals********************************************** #
# **************************************************************************** #

# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

# Time complexity O(n log n):
def merge(intervals):
  if len(intervals) < 2:
    return intervals
  
  intervals.sort(key = lambda x: x.start)

  merged = []

  start = intervals[0].start
  end = intervals[0].end

  for i in range(1, len(intervals)):
    interval = intervals[i]
    if interval.start <= end:
      end = max(end, interval.end)
    else:
      merged.append(Interval(start, end))
      start = interval.start
      end = interval.end
  
  merged.append(Interval(start, end))

  return merged
