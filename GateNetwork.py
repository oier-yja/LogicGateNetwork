from GateGraph import GateGraph
from gatenetwork.optimizers.GateGraphOptimizer import GateGraphOptimizer
from handlers.GateGraphCalculator import GateGraphCalculator
from handlers.GateGraphDisplayer import GateGraphDisplayer
from handlers.GateGraphGenerator import GateGraphGenerator


class GateNetwork:
    def __init__(self, inputs_num, outputs_num):
        self.inputs_num = inputs_num
        self.outputs_num = outputs_num
        self.__gate_graph = GateGraph(inputs_num, outputs_num)
        self.generator = GateGraphGenerator(self.__gate_graph)
        self.calculator = GateGraphCalculator(self.__gate_graph, './datas/test2.csv')
        self.displayer = GateGraphDisplayer(self.__gate_graph)
        self.optimizer = GateGraphOptimizer(self.__gate_graph)


if __name__ == '__main__':
    gate_network = GateNetwork(12, 12)
    generator = gate_network.generator
    displayer = gate_network.displayer
    calculator = gate_network.calculator
    optimizer = gate_network.optimizer

    generator.generateOutputGates()
    generator.generateRandomEdges()

    # optimizer.mapSearchSpace()

    displayer.drawGateGraph()
    displayer.drawCoordinateGraph(calculator)
