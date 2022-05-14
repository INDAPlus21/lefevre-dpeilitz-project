class Node:
    def __init__(self, passable: bool):
        self.reset(passable)
        
    # Update the values of this node
    def update(self, gcost: int, hcost: int, activator: tuple[int, int]):
        # Check if most efficient path from point a before changing the g_cost
        if self.g_cost > gcost:
            self.g_cost = gcost
            self.activator = activator
        # Set h_cost to distance to point b
        self.h_cost = hcost
        # The f_cost, a node's rating so to speak, is the sum of the g_cost and the h_cost
        self.f_cost = gcost + hcost
        # Check if node has been picked previously before making it pickable
        if self.pick_state != 2:
            self.pick_state = 1

    # Reset the node
    def reset(self, passable: bool):
        self.g_cost = 1000000
        self.h_cost = 1000000
        self.f_cost = 1000000
        self.pick_state = 0 # 0 = inte uppdaterad, 1 = uppdaterad och pickable, 2 = redan använd
        self.passable = passable