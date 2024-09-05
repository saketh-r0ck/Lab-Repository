
def interval_scheduling(intervals):
    credit_hrs = []
    end_time = 0
    for interval in intervals:
        if end_time < interval[0]:
            credit_hrs.append(interval)
            end_time = interval[1]
    return credit_hrs


def find_min_intervals(times):
    intervals = []
    i = 0
    n = len(times)
    
    while i < n:
        start_time = times[i]
        end_time = start_time + 1
        intervals.append((start_time, end_time))
        while i < n and times[i] <= end_time:
            i += 1
    
    return intervals

def time_int(x):
    y = x.split(":")
    return int(y[0]) + 0.01*int(y[1])


inp = input().split()
times = list(map(time_int,inp))
interval = [(times[i], times[i+1]) for i in range(len(times) - 1)]
if times: 
    interval.append((times[-1], times[-1] + 1))

print("Interval Scheduling Intervals: ", interval_scheduling(interval))
result = find_min_intervals(times)
print("Greedy strategy Intervals:", result)