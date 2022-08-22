import networkx as nx
from matplotlib import pyplot as plt

from gatenetwork.GateGraph import GateGraph
from gatenetwork.handlers.GateGraphCalculator import GateGraphCalculator


class GateGraphDisplayer:
    def __init__(self, gate_graph: GateGraph):
        self.__gate_graph = gate_graph

    def drawGateGraph(self):
        pos_nodes = nx.spring_layout(self.__gate_graph.G)
        pos_attrs = {}
        for node, coords in pos_nodes.items():
            pos_attrs[node] = (coords[0], coords[1] + 0.06)
        nx.draw_networkx(self.__gate_graph.G, pos_nodes, node_color=self.__gate_graph.node_color, node_size=200,
                         font_size=6)
        nx.draw_networkx_labels(self.__gate_graph.G, pos_attrs, labels=nx.get_node_attributes(self.__gate_graph.G, 'label'),
                                font_size=6)
        plt.show()

    def drawCoordinateGraph(self, calculator: GateGraphCalculator):
        plt.title("result")
        plt.plot(calculator.inputs_data, calculator.outputs_data)
        plt.plot(calculator.inputs_data, calculator.calculateAllOutputs())
        plt.show()
