import matplotlib.pyplot as plt
import networkx as nx

def _search_list(list, search):
    """
    internal searching of the list
    """
    present = False
    for sublist in list:
        if search in sublist:
            present = True 
            break 
    return present

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
    shells = []

    for node in graph.nodes(): 
        labels [ node ] = node    
        node_size.append ( len(node) * 1000 )
        node_list.append ( node ) 
        succ_list = []        
        for succ in graph.successors(node):
            succ_list = []            
            if not _search_list(shells, succ) is True: 
                succ_list.append(succ)      
        shells.append(succ_list) 
    import pdb
    pdb.set_trace()
    pos=nx.shell_layout(graph,shells)
    nx.draw_networkx_nodes( G = graph, 
                            pos = pos,
                            node_list = node_list,
                            node_size = node_size,
                            node_color = 'g',
                            node_shape = 'o' )
    nx.draw_networkx_edges(G = graph, pos = pos)
    nx.draw_networkx_labels(G = graph, pos = pos , 
                            labels = labels ,font_family='sans-serif',
                            font_size=7)
    plt.savefig(filename)

    if show == True:
        plt.show()
