import statistics

data = [1, 2, 3, 4, 5, 4, 3, 3, 1]

mean = statistics.mean(data)
median = statistics.median(data) 
mode = statistics.mode(data)
stdev = statistics.stdev(data)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")  
print(f"Standard Deviation: {stdev:.3f}")
