/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start

class TwoSumLettcode {
// class Solution {
    /**
     * Approach 1: Brute Force
     */
    // public int[] twoSum(int[] nums, int target) {
    //     for (int i = 0; i < nums.length; i++) {
    //         for (int j = i + 1; j < nums.length; j++) {
    //             if (nums[j] == target - nums[i]) {
    //                 return new int[] { i, j };
    //             }
    //         }
    //     }
    //     throw new IllegalArgumentException("No two sum solution");
    // }

    /**
     * Approach 2: Two-pass Hash Table
     */
    // public int[] twoSum(int[] nums, int target) {
    //     Map<Integer, Integer> map = new HashMap<>();
    //     for (int i = 0; i < nums.length; i++) {
    //         map.put(nums[i], i);
    //     }
    //     for (int i = 0; i < nums.length; i++) {
    //         int complement = target - nums[i];
    //         if (map.containsKey(complement) && map.get(complement) != i) {
    //             return new int[] { i, map.get(complement) };
    //         }
    //     }
    //     throw new IllegalArgumentException("No two sum solution");
    // }

    /**
     * Approach 3: One-pass Hash Table (best)
     */
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }

    // public static void main(String[] args) {
    //     Solution solution = new Solution();
    //     int[] indexes = solution.twoSum(new int[] {2, 7, 11, 15}, 9);
    //     System.out.println(indexes[0] + " " + indexes[1]);
    // }
}
// @lc code=end

