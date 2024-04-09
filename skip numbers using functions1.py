def minJumps(arr):
    n = len(arr)
    
    # If the array is empty or the first element is 0, it's not reachable
    if n == 0 or arr[0] == 0:
        return -1
    
    # Initialize variables to keep track of current coverage and maximum coverage
    max_reachable = arr[0]
    steps = arr[0]
    jumps = 1
    
    # Iterate through the array
    for i in range(1, n):
        # If the current index is beyond the maximum reachable index, return -1
        if i > max_reachable:
            return -1
        
        # If the current index is within the current coverage, update the maximum coverage
        if i <= steps:
            max_reachable = max(max_reachable, i + arr[i])
        
        # If the current index reaches the end of coverage, increment jumps and update the next coverage
        if i == steps:
            jumps += 1
            steps = max_reachable
    
    return jumps

# Test cases
test_cases = [[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [2, 3, 1, 1, 4],
              [1, 3, 6, 1, 0, 9]]
for i, arr in enumerate(test_cases, start=1):
    print("Test Case", i, ":")
    print("Input:", arr)
    print("Output:", minJumps(arr))
    print()
