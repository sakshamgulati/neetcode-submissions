class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left,right= 0,len(nums)-1
        
        def binary_search(left,right):
            if left > right:
                return False
            
            mid= (left+right)//2
            if target == nums[mid]:
                return True
            
            #handle duplicates
            if nums[left]==nums[mid]==nums[right]:
                return binary_search(left+1,mid-1) or binary_search(mid+1,right)
            #check if the first half is sorted            
            if nums[left] <= nums[mid]:
                if nums[mid] >= target and nums[left] < target:
                    # focus on the sorted half
                    right=mid-1
                else:
                    left = mid + 1
                    
                return binary_search(left,right)
                    
            else:
                if target <=  nums[right] and target > nums[mid]:
                    left= mid + 1
                else:
                    right = mid - 1
                return binary_search(left,right)
            
        return binary_search(left,right)
