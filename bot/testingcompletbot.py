
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pickle
from pathlib import Path

from collections import defaultdict

def load_graph():
    pickle_in = open("../cl/graph.pickle","rb")
    Gin = pickle.load(pickle_in)
    return Gin


def encuesta(EID,G):

    preguntas = G.nodes[EID]['content']
    vecinos = list(G.successors(EID))
    prev_node = EID
    next_node = vecinos[0]
    for nodo in vecinos:
        if G[prev_node][next_node]['color'] == 'black':
            preguntas.remove(next_node)





    print (vecinos)


def dfs_successors(G, source=None, depth_limit=None):
    """Returns dictionary of successors in depth-first-search from source.

    Parameters
    ----------
    G : NetworkX graph

    source : node, optional
       Specify starting node for depth-first search.

    depth_limit : int, optional (default=len(G))
       Specify the maximum search depth.

    Returns
    -------
    succ: dict
       A dictionary with nodes as keys and list of successor nodes as values.

    Examples
    --------
    #>>> G = nx.path_graph(5)
    #>>> nx.dfs_successors(G, source=0)
    {0: [1], 1: [2], 2: [3], 3: [4]}
    #>>> nx.dfs_successors(G, source=0, depth_limit=2)
    {0: [1], 1: [2]}

    Notes
    -----
    If a source is not specified then a source is chosen arbitrarily and
    repeatedly until all components in the graph are searched.

    The implementation of this function is adapted from David Eppstein's
    depth-first search function in `PADS`_, with modifications
    to allow depth limits based on the Wikipedia article
    "`Depth-limited search`_".

    .. _PADS: http://www.ics.uci.edu/~eppstein/PADS
    .. _Depth-limited search: https://en.wikipedia.org/wiki/Depth-limited_search

    See Also
    --------
    dfs_preorder_nodes
    dfs_postorder_nodes
    dfs_labeled_edges
    edge_dfs
    bfs_tree
    """
    d = defaultdict(list)
    for s, t in dfs_edges(G, source=source, depth_limit=depth_limit):
        d[s].append(t)
    return dict(d)


def dfs_edges(G, source=None, depth_limit=None):
    """Iterate over edges in a depth-first-search (DFS).

    Perform a depth-first-search over the nodes of G and yield
    the edges in order. This may not generate all edges in G (see edge_dfs).

    Parameters
    ----------
    G : NetworkX graph

    source : node, optional
       Specify starting node for depth-first search and return edges in
       the component reachable from source.

    depth_limit : int, optional (default=len(G))
       Specify the maximum search depth.

    Returns
    -------
    edges: generator
       A generator of edges in the depth-first-search.

    Examples
    --------
    #>>> G = nx.path_graph(5)
    #>>> list(nx.dfs_edges(G, source=0))
    #[(0, 1), (1, 2), (2, 3), (3, 4)]
    #>>> list(nx.dfs_edges(G, source=0, depth_limit=2))
    [(0, 1), (1, 2)]

    Notes
    -----
    If a source is not specified then a source is chosen arbitrarily and
    repeatedly until all components in the graph are searched.

    The implementation of this function is adapted from David Eppstein's
    depth-first search function in `PADS`_, with modifications
    to allow depth limits based on the Wikipedia article
    "`Depth-limited search`_".

    .. _PADS: http://www.ics.uci.edu/~eppstein/PADS
    .. _Depth-limited search: https://en.wikipedia.org/wiki/Depth-limited_search

    See Also
    --------
    dfs_preorder_nodes
    dfs_postorder_nodes
    dfs_labeled_edges
    edge_dfs
    bfs_edges
    """
    if source is None:
        # edges for all components
        nodes = G
    else:
        # edges for components with source
        nodes = [source]
    visited = set()
    if depth_limit is None:
        depth_limit = len(G)
    for start in nodes:
        if start in visited:
            continue
        visited.add(start)
        stack = [(start, depth_limit, iter(G[start]))]
        while stack:
            parent, depth_now, children = stack[-1]
            try:
                child = next(children)
                if child not in visited:
                    yield parent, child
                    visited.add(child)
                    if depth_now > 1:
                        stack.append((child, depth_now - 1, iter(G[child])))
            except StopIteration:
                stack.pop()



def  extras(G):
    P1 = G.nodes['P1']['content']
    print(P1)
    print(G.nodes['R3']['content'])
    print(G['P1']['R1']['label'])

    print(G.nodes['E']['content'])
    print(G.nodes,G.edges)

def main():
    G = load_graph()
    print((dfs_successors(G,source = 'E')))





if __name__ == '__main__':
    main()


