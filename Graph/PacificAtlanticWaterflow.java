import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;

public class PacificAtlanticWaterflow {

    private final int[][] HEIGHTS = {
            {1, 2, 2, 3, 5},
            {3, 2, 3, 4, 4},
            {2, 4, 5, 3, 1},
            {6, 7, 1, 4, 5},
            {5, 1, 1, 2, 4}
    };

    private final int COLS = HEIGHTS.length;
    private final int ROWS = HEIGHTS[0].length;

    HashSet<ArrayList<Integer>> pacific;
    HashSet<ArrayList<Integer>> atlantic;

    public Solution() {
        pacific = new HashSet<>();
        atlantic = new HashSet<>();
    }


    public List<List<Integer>> pacificAtlantic() {

        for (int i = 0; i < COLS; i++) {
            dfs(0, i, pacific, 0);
            dfs(ROWS-1, i, atlantic, 0);
        }

        for (int j = 0; j < ROWS; j++) {
            dfs(j, 0, pacific, 0);
            dfs(j, COLS-1, atlantic, 0);
        }

        List<List<Integer>> result = new ArrayList<>();

        for (ArrayList<Integer> curr : pacific) {
            if (atlantic.contains(curr)) {
                result.add(curr);
            }
        }
        return result;

    }

    private void dfs(int row, int col, HashSet<ArrayList<Integer>> visit, int prevHeight){

        ArrayList<Integer> tuple = new ArrayList<>();
        Collections.addAll(tuple, row, col);

        if (visit.contains(tuple) ||
                row < 0 || col < 0 ||
                row == ROWS  || col == COLS ||
                HEIGHTS[row][col] < prevHeight) {

            return;
        }

        visit.add(tuple);

        dfs(row + 1, col, visit, HEIGHTS[row][col]);
        dfs(row - 1, col, visit, HEIGHTS[row][col]);
        dfs(row, col + 1, visit, HEIGHTS[row][col]);
        dfs(row, col - 1, visit, HEIGHTS[row][col]);

    }

    public static void main(String[] args) {
        PacificAtlanticWaterflow solution = new PacificAtlanticWaterflow();
        System.out.println(solution.pacificAtlantic());
    }


}





