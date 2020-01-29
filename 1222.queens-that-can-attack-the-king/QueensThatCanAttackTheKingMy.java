/*
 * @lc app=leetcode id=1222 lang=java
 *
 * [1222] Queens That Can Attack the King
 */

import java.util.*;

// @lc code=start

// class Solution {
class QueensThatCanAttackTheKingMy {
    
    public List<List<Integer>> queensAttacktheKing(int[][] queens, int[] king) {
        
        int[][] directions = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
        List<List<Integer>> attack_queens = new ArrayList<List<Integer>>();

        int i, j;
        for (int[] direction: directions) {
            i = king[0]; j = king[1];
        
        thewhile:
            while (true) {
                i += direction[0]; j += direction[1];

                if (i < 0 || i > 7 || j < 0 || j > 7) break;

                for (int[] queen: queens)
                    if (queen[0] == i && queen[1] == j) {
                        attack_queens.add(Arrays.asList(i, j));
                        break thewhile;
                    }
            }
        }
        
        return attack_queens;
    }
}
// @lc code=end

