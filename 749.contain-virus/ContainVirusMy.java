/*
 * @lc app=leetcode id=749 lang=java
 *
 * [749] Contain Virus
 */

// @lc code=start

// class Solution {
class ContainVirusMy {
    
    public int containVirus(int[][] grid) {

        int n = grid[0].length;
        int num_regions = 0;
        int num_walls = 0;

        do {
            Map<Integer, List<Integer>> graph = get_graph(grid);
            if (graph.size() == 0) return 0;
            Map<Integer, Boolean> visited = new HashMap<Integer, Boolean>();

            for (int node : graph.keySet()) 
                visited.put(node, false);
            
            List<List<Integer>> regions = new ArrayList<List<Integer>>();
            List<List<int[]>> perimeters = new ArrayList<List<int[]>>();

            for (int node : graph.keySet()) 
                if (visited.get(node) == false) {
                    List<Integer> region = new ArrayList<Integer>();
                    List<int[]> perimeter = new ArrayList<int[]>();
                    dfs(grid, graph, node, visited, region, perimeter);
                    regions.add(region);
                    perimeters.add(perimeter);
                }

            int most_viral_region = 0;
            int max_frontier_size = get_frontier_size(perimeters.get(0));

            for (int i = 1; i < regions.size(); i++) {
                int frontier_size = get_frontier_size(perimeters.get(i));
                if (max_frontier_size < frontier_size) {
                    max_frontier_size = frontier_size;
                    most_viral_region = i;
                }
            }

            for (int i = 0; i < regions.size(); i++) 
                for (int[] cell : perimeters.get(i)) {
                    int[] coord = pos_to_coord(cell[0], n);
                    if (i == most_viral_region)
                        grid[coord[0]][coord[1]] += cell[1]; // add wall
                    else
                        grid[coord[0]][coord[1]] |= 1; // spread virus                   
                }

            num_walls += perimeters.get(most_viral_region).size();
            
            for (int cell : regions.get(most_viral_region)) {
                int[] coord = pos_to_coord(cell, n);
                grid[coord[0]][coord[1]] = -1;  // affected cell blocked
            }

            num_regions = regions.size();

        } while(num_regions != 1);

        return num_walls;
    }

    public static Map<Integer, List<Integer>> get_graph(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        Map<Integer, List<Integer>> graph = new HashMap<Integer, List<Integer>>();
        
        for (int pos = 0; pos < m*n; pos++)
            if (is_pos_available(grid, pos)) {
                List<Integer> adjacents = new ArrayList<Integer>();
                for (int[] neighbor : get_neighbors(grid, pos))
                    if (is_pos_available(grid, neighbor[0]))
                        adjacents.add(neighbor[0]);
 
                graph.put(pos, adjacents);
            } 

        return graph;
    }

    public static int get_frontier_size(List<int[]> perimeter) {
        Set<Integer> frontier = new HashSet<>();
        for (int[] cell : perimeter)
            frontier.add(cell[0]);

        return frontier.size();
    }

    public static List<int[]> get_neighbors(int[][] grid, int pos) {
        int m = grid.length, n = grid[0].length;
        int[] coord = pos_to_coord(pos, n);
        int i = coord[0], j = coord[1];
        List<int[]> neighbors = new ArrayList<int[]>();

        // We use the unused grid cells bits to declare the adjacent cell walls 
        // bit 1: left, bit 2: up, bit 3: right, bit 4: down
        if (j-1 >= 0) neighbors.add(new int[] {coord_to_pos(new int[] {i,j-1}, n), 8});
        if (i-1 >= 0) neighbors.add(new int[] {coord_to_pos(new int[] {i-1,j}, n), 16});
        if (j+1 <  n) neighbors.add(new int[] {coord_to_pos(new int[] {i,j+1}, n), 2});
        if (i+1 <  m) neighbors.add(new int[] {coord_to_pos(new int[] {i+1,j}, n), 4});

        return neighbors;
    }

    public static void dfs(int[][] grid, Map<Integer,List<Integer>> graph, int node, 
        Map<Integer,Boolean> visited, List<Integer> region, List<int[]> perimeter) {
        
        visited.put(node, true);
        region.add(node);
        
        for (int[] neighbor : get_neighbors(grid, node)) {
            int[] coord = pos_to_coord(neighbor[0], grid[0].length);
            // check for no adyacent cell wall and no infected cell
            if ((grid[coord[0]][coord[1]] & (neighbor[1] + 1)) == 0)
                perimeter.add(new int[] {neighbor[0], neighbor[1]});       
        }
        
        for (int next_node : graph.get(node))
            if (visited.get(next_node) == false) 
                dfs(grid, graph, next_node, visited, region, perimeter);
    }

    public static Boolean is_pos_available(int[][] grid, int pos) {
        int[] coord = pos_to_coord(pos, grid[0].length);
        int val_pos = grid[coord[0]][coord[1]];
        // check infected and no blocked cells 
        if ((val_pos & 1) == 1 & val_pos > 0) return true;
        return false;
    }

    public static int[] pos_to_coord(int pos, int n) {
        return new int[] {pos/n, pos%n};
    }

    public static int coord_to_pos(int[] coord, int n) {
        return n*coord[0] + coord[1];
    }
}

// @lc code=end

