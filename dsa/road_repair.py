

def get_parent_component(self, x, parent_component):
    if x == parent_component[x]:
        return x
    parent_component[x] = self.get_parent_component(x)
    return parent_component[x]

def road_repair(self, edges):
    # edge.u
    # edge.v
    # edge.c

    edges.sort(key=lambda x: x.c)
    n = len(edges)
    m = 10

    parent_component = [i for i in range(m)]
    total_cost = 0

    for edge in edges:
        u = edge.u
        v = edge.v
        c = edge.c

        pu = self.get_parent_component(u, parent_component)
        pv = self.get_parent_component(v, parent_component)

        if pu != pv:
            parent_component[min[pu, pv]] = max(pu, pv)
            total_cost = total_cost + c

    return total_cost








