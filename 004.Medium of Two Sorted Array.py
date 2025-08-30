class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = nums1 + nums2
        new_list.sort()
        
        n = len(new_list)
        mid = n // 2
        
        if n % 2 == 1:
            return float(new_list[mid])
        else:
            return (new_list[mid - 1] + new_list[mid]) / 2.0
