class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # 1. Find the pivot: first index (from the right) where nums[i-1] < nums[i]
        pivot_index = -1
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                pivot_index = i - 1
                break
        
        # 2. If a pivot was found, find the smallest element in the suffix
        #    that's still greater than pivot_val, scanning RIGHT TO LEFT
        #    (suffix is decreasing, so right-to-left finds the smallest qualifier first)
        if pivot_index != -1:
            pivot_val = nums[pivot_index]
            for i in range(n - 1, pivot_index, -1):
                if nums[i] > pivot_val:
                    nums[pivot_index], nums[i] = nums[i], nums[pivot_index]
                    break
        
        # 3. Reverse the suffix in place (works for both cases:
        #    if pivot found, suffix was decreasing -> now needs reversing to ascending;
        #    if no pivot found, whole array was decreasing -> reverse whole array)
        left, right = pivot_index + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1