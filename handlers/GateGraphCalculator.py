import random
import math
import networkx as nx
import pandas as pd
from gatenetwork.GateGraph import GateGraph


class GateGraphCalculator:
    def __init__(self, gate_graph: GateGraph, file_path):
        self.__gate_graph = gate_graph
        self.inputs = []
        self.outputs = []
        self.datas_index = 0

        self.inputs_data = pd.read_csv(file_path, sep=',', header='infer', usecols=[0])
        self.inputs_data = self.inputs_data.values[0::, 0::].reshape(-1, len(self.inputs_data)).tolist()[0]
        for i in range(len(self.inputs_data)):
            if math.isnan(self.inputs_data[i]):
                break
            else:
                self.inputs_data[i] = int(self.inputs_data[i])

        self.outputs_data = pd.read_csv(file_path, sep=',', header='infer', usecols=[1])
        self.outputs_data = self.outputs_data.values[0::, 0::].reshape(-1, len(self.outputs_data)).tolist()[0]
        for i in range(len(self.outputs_data)):
            if math.isnan(self.outputs_data[i]):
                break
            else:
                self.outputs_data[i] = int(self.outputs_data[i])

    def loadDatas(self):
        self.inputs.clear()
        self.outputs.clear()
        a = self.inputs_data[self.datas_index]
        b = self.outputs_data[self.datas_index]

        for i in range(12):
            self.inputs.append(a % 2)
            self.outputs.append(b % 2)
            a = a >> 1
            b = b >> 1

        self.datas_index = self.datas_index + 1

    def __stimulateGate(self, index):
        if index in self.__gate_graph.getGatesRange():
            predecessors = self.__gate_graph.getPredecessorsIndexOf(index)
            a = self.__stimulateGate(predecessors[0])
            b = self.__stimulateGate(predecessors[1])
            return self.__gate_graph.getGate(index).stimulate(a, b)

        elif index in self.__gate_graph.getInputsRange():
            return self.inputs[index - 1]

        elif index in self.__gate_graph.getOutputsRange():
            predecessors = self.__gate_graph.getPredecessorsIndexOf(index)
            return self.__stimulateGate(predecessors[0])

    def calculateOutputs(self):
        result = 0
        for i in self.__gate_graph.getOutputsRange():
            result = result << 1
            result = result + self.__stimulateGate(i)

        return result

    def calculateAllOutputs(self):
        result = []
        for i in range(len(self.outputs_data)):
            self.loadDatas()
            result.append(self.calculateOutputs())
        return result

    def printDatas(self):
        print(self.inputs)
        print(self.outputs)