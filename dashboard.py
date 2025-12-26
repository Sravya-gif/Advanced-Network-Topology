import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import networkx as nx
import asyncio
import socket
import json
import threading
import time

G = nx.Graph()
nodes = {}

PORT = 6000

def udp_listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("0.0.0.0", PORT))
    while True:
        data, addr = s.recvfrom(1024)
        d = json.loads(data.decode())
        n = d["id"]
        nodes[n] = time.time()
        G.add_node(n)

def cleanup():
    while True:
        now = time.time()
        for n, t in list(nodes.items()):
            if now - t > 5:
                nodes.pop(n)
                if n in G:
                    G.remove_node(n)
        time.sleep(1)

threading.Thread(target=udp_listener, daemon=True).start()
threading.Thread(target=cleanup, daemon=True).start()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2("Dynamic Network Topology"),
    dcc.Graph(id="graph"),
    dcc.Interval(id="i", interval=1000)
])

@app.callback(Output("graph", "figure"), Input("i", "n_intervals"))
def update(_):
    G.clear_edges()
    l = list(G.nodes())
    for i in range(len(l) - 1):
        G.add_edge(l[i], l[i + 1])

    pos = nx.spring_layout(G)
    edge_x, edge_y = [], []
    for a, b in G.edges():
        x0, y0 = pos[a]
        x1, y1 = pos[b]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    node_x = [pos[n][0] for n in G.nodes()]
    node_y = [pos[n][1] for n in G.nodes()]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode="lines"))
    fig.add_trace(go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        text=list(G.nodes()),
        marker=dict(size=25)
    ))
    return fig

app.run(debug=False)
