import matplotlib.pyplot as plt
import networkx as nx

def draw_network(graph, filename = 'network.pdf', show = False):
    """
    This is a simple wrapper to the networkx_draw.
    Args:
        filename: what file to save down as.
        show: will display the graph on a window. 
    Nots:
        Takes any format that networkx matplotlib plotter takes.
    """

    labels = {}
    node_size = []
    node_list = []
    for node in graph.nodes(): 
        labels [ node ] = node    
        node_size.append ( len(node) * 1000 )
        node_list.append ( node )       
    pos=nx.shell_layout(graph,node_list)
    nx.draw_networkx_nodes( G = graph, 
                            pos = pos,
                            node_list = node_list,
                            node_size = node_size,
                            node_color = 'g',
                            node_shape = 'o' )
    nx.draw_networkx_edges(G = graph, pos = pos)
    nx.draw_networkx_labels(G = graph, pos = pos , labels = labels)
    plt.savefig(filename)

    if show == True:
        plt.show()
