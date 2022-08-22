import math
import random
from gatenetwork.GateGraph import GateGraph


class GateGraphGenerator:

    def __init__(self, gate_graph: GateGraph):
        self.__gate_graph = gate_graph

    def generateOutputGates(self):
        for i in self.__gate_graph.getOutputsRange():
            self.__gate_graph.addGate()
            self.__gate_graph.addEdge(self.__gate_graph.getLastGateIndex(), i)

    def generateGatesWithRandomEdges(self, num):
        for i in range(num):
            self.__gate_graph.addGate()
            available_nodes, unavailable_nodes, edge_required_gates, edges_required_gates = \
                self.__gate_graph.classifyNodes()
            if len(available_nodes) >= 2:
                u1 = random.choice(available_nodes)
                u2 = random.choice(available_nodes)
                while u1 is u2:
                    u2 = random.choice(available_nodes)
                self.__gate_graph.addEdge(u1, self.__gate_graph.getLastGateIndex())
                self.__gate_graph.addEdge(u2, self.__gate_graph.getLastGateIndex())
            elif len(available_nodes) is 1 and len(unavailable_nodes) >= 1:
                u1 = available_nodes[0]
                u2 = random.choice(unavailable_nodes)
                self.__gate_graph.addEdge(u1, self.__gate_graph.getLastGateIndex())
                self.__gate_graph.addEdge(u2, self.__gate_graph.getLastGateIndex())
            elif len(unavailable_nodes) >= 2:
                u1 = random.choice(unavailable_nodes)
                u2 = random.choice(unavailable_nodes)
                while u1 is u2:
                    u2 = random.choice(unavailable_nodes)
                self.__gate_graph.addEdge(u1, self.__gate_graph.getLastGateIndex())
                self.__gate_graph.addEdge(u2, self.__gate_graph.getLastGateIndex())

    # Generate gates to ensure full link
    def generateFullLinkRequiredGates(self):
        available_nodes, unavailable_nodes, edge_required_gates, edges_required_gates = self.__gate_graph.classifyNodes()
        for i in range(int(math.factorial(len(available_nodes)) / 2 * math.factorial(len(available_nodes) - 2)) -
                       len(edges_required_gates) * 2):
            self.__gate_graph.addGate()
            if len(unavailable_nodes) > 1:
                u1 = random.choice(unavailable_nodes)
                u2 = random.choice(unavailable_nodes)
                while u1 is u2:
                    u2 = random.choice(unavailable_nodes)

                self.__gate_graph.addEdge(u1, self.__gate_graph.getLastGateIndex())
                self.__gate_graph.addEdge(u2, self.__gate_graph.getLastGateIndex())

    # Link nodes randomly
    def generateRandomEdges(self):
        available_nodes, unavailable_nodes, edge_required_gates, edges_required_gates = self.__gate_graph.classifyNodes()
        for edges_required_gate in edges_required_gates:
            if len(available_nodes) > 1:
                u1 = random.choice(available_nodes)
                u2 = random.choice(available_nodes)
                while u1 is u2:
                    u2 = random.choice(available_nodes)

                self.__gate_graph.addEdge(u1, edges_required_gate)
                self.__gate_graph.addEdge(u2, edges_required_gate)
                available_nodes.remove(u1)
                unavailable_nodes.append(u1)
                available_nodes.remove(u2)
                unavailable_nodes.append(u2)
            elif len(available_nodes) is 1 and len(unavailable_nodes) > 0:
                u1 = available_nodes[0]
                u2 = random.choice(unavailable_nodes)

                self.__gate_graph.addEdge(u1, edges_required_gate)
                self.__gate_graph.addEdge(u2, edges_required_gate)
                available_nodes.remove(u1)
                unavailable_nodes.append(u1)
            elif len(unavailable_nodes) > 1:
                u1 = random.choice(unavailable_nodes)
                u2 = random.choice(unavailable_nodes)
                while u1 is u2:
                    u2 = random.choice(unavailable_nodes)

                self.__gate_graph.addEdge(u1, edges_required_gate)
                self.__gate_graph.addEdge(u2, edges_required_gate)
