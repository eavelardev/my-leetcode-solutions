/*
 * @lc app=leetcode id=403 lang=java
 *
 * [403] Frog Jump
 */

import java.util.*;

// @lc code=start

class FrogJumpMe {
// class Solution {
    public boolean canCross(int[] stones) {
        
        List<Integer> lstones = new ArrayList<Integer>();
        for (int stone :stones) lstones.add(stone);
        int last_stone = lstones.get(lstones.size()-1);

        // Max number of jumps units with 1099 stones 
        // calculated using n*(n-1)/2
        if (last_stone > 603351) return false;

        return dfs(0, 0, last_stone, lstones);
    }

    public static boolean dfs(int node, int k, int last_stone, List<Integer> lstones) {

        for (int jump_unit : new int[] {k+1, k, k-1})
            if (jump_unit > 0) {
                int new_node = node + jump_unit;
                if (lstones.contains(new_node)) {
                    if (new_node == last_stone) return true;
                    if(dfs(new_node, jump_unit, last_stone, lstones)) return true;
                }
            }

        return false;
    }
}

// @lc code=end

