from ghosts.node_grid import Node_grid
from ghosts.vec2int import Vec2Int

class Pathfinder:
    def __init__(self, grid: list[list[int]]):
        self.node_grid = Node_grid(grid)

    # Actual pathfinding
    def find_path(self, start_pos: Vec2Int, target_pos: Vec2Int) -> list[Vec2Int]:
        # Update starting node
        self.node_grid.get_node(start_pos).update(0, self.dist_to_point(start_pos, target_pos) * 10, start_pos)

        curr_pos = start_pos

        # Run loop until destination is reached
        while curr_pos != target_pos:
            
            # Set current node to unpickable
            self.node_grid.get_node(curr_pos).pick_state = 2

            # Find movable adjacent nodes, returns tuple
            adj = self.get_adjacents(curr_pos)  

            curr_node = self.node_grid.get_node(curr_pos)
            for i in range(len(adj)):
                # Update gcost and hcost values in adjacent nodes
                self.node_grid.get_node(adj[i]).update(curr_node.gcost + 10, self.dist_to_point(adj[i], target_pos) * 10, curr_pos)
            # Find the node on the grid that has the lowest fcost, and as a tie breaker hcost
            curr_pos = self.find_best_node()

        path = self.backtrack_path(target_pos)
        self.node_grid.clear()

        return path


    # Helper methods
    def dist_to_point(self, start_pos: Vec2Int, target_pos: Vec2Int):
        x_diff = abs(start_pos.x - target_pos.x)
        y_diff = abs(start_pos.y - target_pos.y)
        return x_diff + y_diff


    # Check if nodes in all directions are within the grid and are passable
    def get_adjacents(self, pos: Vec2Int):
        adjacents = []
    
        # Check Up
        if pos.y - 1 > -1:
            if self.node_grid.get_node(Vec2Int(pos.x, pos.y - 1)).passable:
                adjacents.append(Vec2Int(pos.x, pos.y - 1))

        # Check Down
        if pos.y + 1 < self.node_grid.height:
            if self.node_grid.get_node(Vec2Int(pos.x, pos.y + 1)).passable:
                adjacents.append(Vec2Int(pos.x, pos.y + 1))

        # Check Right
        if pos.x + 1 < self.node_grid.width:
            if self.node_grid.get_node(Vec2Int(pos.x + 1, pos.y)).passable:
                adjacents.append(Vec2Int(pos.x + 1, pos.y))

        # Check Left
        if pos.x - 1 > -1:
            if self.node_grid.get_node(Vec2Int(pos.x - 1, pos.y)).passable:
                adjacents.append(Vec2Int(pos.x - 1, pos.y))

        return adjacents

        
    # Find the best available node in the grid
    def find_best_node(self):
        return self.find_lowest_hcost(self.find_lowest_fcost())


    # Find the nodes with the lowest fcosts
    def find_lowest_fcost(self):
        lowest_cost = 10000
        lowest_fcords = []
        test = []

        for y in range(self.node_grid.height):
            for x in range(self.node_grid.width):
                curr_pos = Vec2Int(x, y)
                curr_node = self.node_grid.get_node(curr_pos)
                if curr_node.pick_state == 1:
                    test.append(curr_pos)
                    if curr_node.fcost < lowest_cost:
                        lowest_fcords.clear()
                        lowest_fcords.append(curr_pos)
                        lowest_cost = curr_node.fcost
                    elif curr_node.fcost == lowest_cost:
                        lowest_fcords.append(curr_pos)
                        
        return lowest_fcords


    # Find the nodes closest to the destination and just pick one
    def find_lowest_hcost(self, lowest_fcords: list[Vec2Int]):

        if len(lowest_fcords) == 1:
            return lowest_fcords[0]

        lowest_hcords = []
        lowest_hcords.append(lowest_fcords[0])
        lowest_cost = self.node_grid.get_node(lowest_fcords[0]).hcost

        for i in range(1, len(lowest_fcords)):
            curr_hcost = self.node_grid.get_node(lowest_fcords[i]).hcost
            if lowest_cost < curr_hcost:
                lowest_hcords.clear()
                lowest_hcords.append(lowest_fcords[i])
                lowest_cost = curr_hcost
            elif lowest_cost < curr_hcost:
                lowest_hcords.append(lowest_fcords[i])
        
        return lowest_hcords[0]


    # Backtracks from target_node to start_node through node.activator
    def backtrack_path(self, target_pos: Vec2Int) -> list[Vec2Int]:
        path = []
        path.append(target_pos)

        while self.node_grid.get_node(target_pos).activator != target_pos:
            target_pos = self.node_grid.get_node(target_pos).activator
            path.append(target_pos)

        path.reverse()

        return path