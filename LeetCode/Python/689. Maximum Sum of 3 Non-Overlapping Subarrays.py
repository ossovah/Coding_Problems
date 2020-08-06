"""
See the problem description at: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

Let us assume that nums = [1, 2, 1, 2, 6, 7, 5, 1] and k = 2. The following outlines the approach:
1) Since the problem involves computing the sum of subarrays, it is helpful to compute the cumulative 
sum of the array. This allows computing the sum of any subarray in O(1) time.
2) Suppose the length of the array is denoted by n. The starting index of the middle subarray must be in 
the following (inclusive) range: [k, n - 2 × k]. This is necessary to ensure that we can have a 
non-overlapping subarray in the left side and one in the right side of the middle subarray. In the above 
example, n = 8 and k = 2. So the starting index of the middle subarray must be in the range [2, 4].
3) We will examine all the scenarios the middle subarray can be to find the solution to the problem. In 
our example, the starting index of the middle subarray could be 2, 3, or 4. Thus, the middle subarray 
could be [1, 2], [2, 6], or [6,7]. These would result in middle subarray cumulative sums of 3, 8, and 13,
respectively. The important question here is what is the left and right subarrays that have the maximum 
cumulative sum for each of the above three cases. We will find this out in the next step.
4) We define two vectors called left and right of length n, where left[i] is the starting index of the 
subarray that ends in the range [0, i] and has the maximum cumulative sum in that range, and right[j] is 
the starting index of the subarray that begins in the range [j, n - 1] and has the maximum cumulative sum 
in that range. Note that similar to the middle subarray, which could only begin in a certain range, the 
left and right subarrays also need to begin in a certain range. However, for simplicity of handling the 
indexes:
    a) We define both left and right to be of length n.
    b) We initialize left to an all-0 vector and update its values with indexes  k.
    c) We initialize right to an all-(n-k) vector and update its values with indexes  n - k - 1.
    4) For the above problem, we have:
        indexes: 0, 1, 2, 3, 4, 5, 6, 7
        nums  = [1, 2, 1, 2, 6, 7, 5, 1]
        left  = [0, 0, 0, 0, 3, 4, 4, 4]
        right = [4, 4, 4, 4, 4, 5, 6, 6]
5) Let us see how left and right will help to find the maximum sum of 3 non-overlapping subarrays. Suppose 
the middle subarray begins at index 4. For this case, the left subarray with the largest cumulative sum 
that ends in index 4 - 1 = 3 begins at index left[3] = 0, which includes [1, 2]  Furthermore, the right 
subarray with the largest cumulative sum that begins in index 4 + 2 = 6 begins at index right[6] = 6, 
which includes [5, 1]. This way, we can find the sum of 3 non-overlapping subarrays. If we repeat this 
process for all the possible middle subarrays, and compare their corresponding results, we will be able 
to find the starting indexes with 3 non-overlapping subarrays that have the largest sum.
6) We should ensure comparison conditions are done in a way that the solution is lexicographically larger 
than alternative solutions.
7) The solution has O(n) time and space complexity.
"""

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Find the cumul. sum of nums so we can find the sum of any k consecutive elements in O(1) time:
        len_nums = len(nums)
        cum_sum = [0] * (len_nums + 1)
        for i in range(len_nums):
            cum_sum[i + 1] = cum_sum[i] + nums[i]

        # Find the maximum subarray sum for a left subarray:
        left = [0] * len_nums   
        # left[i]: starting index of the subarray with max sum that ends in the range [0, i]
        arr_sum = cum_sum[k] - cum_sum[0]   
        for i in range(k, len_nums):
            arr_i_cum_sum = cum_sum[i + 1] - cum_sum[i - k + 1]
            if arr_i_cum_sum > arr_sum:
                left[i] = i - k + 1
                arr_sum = arr_i_cum_sum
            else:
                left[i] = left[i - 1]
                
        # Find the maximum subarray sum for a right subarray:
        right = [len_nums - k] * len_nums   
        # right[j]: starting index of the subarray with max sum that begins in the range [j, len_nums-1]
        arr_sum = cum_sum[len_nums] - cum_sum[len_nums - k]
        for j in range(len_nums - k - 1, -1, -1):
            arr_j_cum_sum = cum_sum[j + k] - cum_sum[j]
            if arr_j_cum_sum >= arr_sum:
                right[j] = j
                arr_sum = arr_j_cum_sum
            else:
                right[j] = right[j + 1]
        
        # Find the max sum by iterating through the middle interval index based on above 2 cache:
        max_sum = 0
        ans = [0, 0, 0]
        for m in range(k, len_nums - 2 * k + 1):    
            # The middle subarray must start anywhere in the above range, so it would be possible
            # to have an interval before and one after the middle one.
            l, r = left[m - 1], right[m + k] # indexes of the max cum sum subarrays in the left & right
            left_subarr_sum = cum_sum[l + k] - cum_sum[l]
            midlle_subarr_sum = cum_sum[m + k] - cum_sum[m]
            right_subarr_sum = cum_sum[r + k] - cum_sum[r]
            total_sum = left_subarr_sum + midlle_subarr_sum + right_subarr_sum
            if total_sum > max_sum:
                max_sum = total_sum
                ans = [l, m, r]
                
        return ans
