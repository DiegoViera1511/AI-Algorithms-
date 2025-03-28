# A* Pathfinding Algorithm

This project implements the A* pathfinding algorithm to find the shortest path between two points on a grid map while avoiding obstacles. The algorithm uses the **Manhattan distance** as a heuristic to efficiently explore the grid.

## Features
- **A* Search Algorithm**: Optimal pathfinding with heuristic-based exploration.
- **Obstacle Avoidance**: Detects and navigates around obstacles marked as `1` in the grid.
- **Path Visualization**: Prints the final path on the grid using `2` to mark the path.
- **Manhattan Distance Heuristic**: Ensures efficient exploration of the grid.

## Code Structure

### Key Functions
1. **`findPath(map, start, end)`**  
   Implements the A* algorithm:
   - Uses a priority queue (min-heap) to explore nodes.
   - Tracks movement costs (`g-cost`) and heuristic costs (`h-cost`).
   - Returns a dictionary `p` to reconstruct the path.

2. **`h_manhattan(pos1, pos2)`**  
   Computes the Manhattan distance heuristic between two positions.

3. **`printPath(map, path, start, end)`**  
   Visualizes the grid with the path marked as `2`, start as `S`, end as `E`, and obstacles as `X`.

### Dependencies
- Python's `heapq` for priority queue operations.
- `sys` for initializing cost matrices with infinity.

## Usage

1. **Define the Grid**  
   Modify the `map` variable to customize obstacles and grid size. Use:
   - `0`: Walkable cell.
   - `1`: Obstacle.

2. **Set Start/End Points**  
   Update `start` and `end` to specify the pathfinding coordinates.

3. **Run the Script**  
   Execute the code to compute and print the path:
   ```bash
   python astar.py