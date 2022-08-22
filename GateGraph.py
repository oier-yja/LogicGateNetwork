import warnings

import networkx as nx

from gatenetwork.Gate import Gate


class GateGraph:
    def __init__(self, inputs_num, outputs_num):
        self.inputs_num = inputs_num
        self.outputs_num = outputs_num
        self.gates_num = 0
        self.node_color = []
        self.G = nx.DiGraph()

        for i in range(1, self.inputs_num + 1):
            self.G.add_node(i, label='input')
            self.node_color.append('y')

        for i in range(self.inputs_num + 1, self.inputs_num + self.outputs_num + 1):
            self.G.add_node(i, label='output')
            self.node_color.append('g')

    def addGate(self):
        self.gates_num = self.gates_num + 1
        gate = Gate()
        self.G.add_node(self.inputs_num + self.outputs_num + self.gates_num, label='gate: '+str(gate.getG()), gate=gate)
        self.node_color.append('brown')

    def addEdge(self, u, v):
        self.G.add_edge(u, v)

    def getGatesRange(self):
        return range(self.inputs_num + self.outputs_num + 1, self.inputs_num + self.outputs_num + self.gates_num + 1)

    def getInputsRange(self):
        return range(1, self.inputs_num + 1)

    def getOutputsRange(self):
        return range(self.inputs_num + 1, self.inputs_num + self.outputs_num + 1)

    def getLastGateIndex(self):
        return self.inputs_num + self.outputs_num + self.gates_num

    def getPredecessorsIndexOf(self, index):
        result = []
        for key in self.G.pred[index].keys():
            result.append(key)
        return result

    def getGate(self, index):
        if index in self.getGatesRange():
            return self.G.nodes[index]['gate']
        else:
            return -1

    # Divide nodes into 4 parts
    def classifyNodes(self):
        # nodes with 0 out-degree and 2 in-degree
        available_nodes = []
        # nodes with non o out-degree and 2 in-degree
        unavailable_nodes = []
        # gates with 0 in-degree
        edge_required_gates = []
        # gates with 1 in-degree
        edges_required_gates = []
        for i in range(1, self.inputs_num + 1):
            if self.G.out_degree[i] is 0:
                available_nodes.append(i)
            else:
                unavailable_nodes.append(i)

        start_index = self.inputs_num + self.outputs_num + 1
        for i in range(start_index, start_index + self.gates_num):
            if self.G.out_degree[i] is 0 and self.G.in_degree[i] is 2:
                available_nodes.append(i)
            elif self.G.out_degree[i] is not 0 and self.G.in_degree[i] is 2:
                unavailable_nodes.append(i)

            if self.G.in_degree[i] is 0:
                edges_required_gates.append(i)
            elif self.G.in_degree[i] is 1:
                edge_required_gates.append(i)

        if len(edge_required_gates) is not 0:
            warnings.warn("edge_required_gates argument is zero")

        return available_nodes, unavailable_nodes, edge_required_gates, edges_required_gates

