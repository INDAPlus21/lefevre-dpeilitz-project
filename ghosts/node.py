from vec2int import Vec2Int

class Node:
    def __init__(self, passable: bool):
        self.reset(passable)
        
    # Update the values of this node
    def update(self, gcost: int, hcost: int, activator: Vec2Int):
        # Check if most efficient path from point a before changing the g_cost
        if self.gcost > gcost:
            self.gcost = gcost
            self.activator = activator
        # Set h_cost to distance to point b
        self.hcost = hcost
        # The f_cost, a node's rating so to speak, is the sum of the g_cost and the h_cost
        self.fcost = gcost + hcost
        # Check if node has been picked previously before making it pickable
        if self.pick_state != 2:
            self.pick_state = 1

    # Reset the node
    def reset(self, passable: bool):
        self.clear()
        self.passable = passable

    def clear(self):
        self.gcost = 1000000
        self.hcost = 1000000
        self.fcost = 1000000
        self.pick_state = 0 # 0 = inte uppdaterad, 1 = uppdaterad och pickable, 2 = redan använd