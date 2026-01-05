from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    """
    Find the maximum value in each sliding window of size k.
    
    Args:
        nums: Integer array
        k: Size of the sliding window
    
    Returns:
        List of maximum values in each window
    
    Time Complexity: O(n) - each element is added and removed once
    Space Complexity: O(k) - deque stores at most k elements
    """
    if not nums or k == 0:
        return []
    
    # Deque to store indices of useful elements
    dq = deque()
    result = []
    
    for i in range(len(nums)):
        # Remove indices that are out of current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements from the back
        # Keep only useful elements that might be maximum
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        # Add current element index
        dq.append(i)
        
        # The front of deque has the index of maximum element
        # Add to result once window is full
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result


# Test with the given example
if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    
    result = maxSlidingWindow(nums, k)
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {result}")
    print()
    
    # Explanation of the sliding windows:
    print("Sliding windows:")
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        max_val = max(window)
        print(f"  Window {i+1}: {window} → max = {max_val}")
