import networkx as nx,time

G=nx.Graph()
nodes={}

def update_node(n):
    nodes[n]=time.time()
    G.add_node(n)

def cleanup(timeout=6):
    now=time.time()
    for n,t in list(nodes.items()):
        if now-t>timeout:
            nodes.pop(n)
            if n in G:
                G.remove_node(n)

def rebuild_edges():
    G.clear_edges()
    l=list(G.nodes())
    for i in range(len(l)-1):
        G.add_edge(l[i],l[i+1])
