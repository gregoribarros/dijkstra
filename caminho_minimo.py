from igraph import *
import numpy as np

class Arrow:
	def __init__(self):
		self.origin = ''
		self.target = ''
		self.cost = ''

	def aPrint(self):
		print(self.origin,self.cost,self.target)

def runGraph(graph,vertex):
	listOfArrows = []
	for edge in graph.incident(vertex):
		a = Arrow()
		a.origin = graph.es[edge].tuple[0]
		a.cost = graph.es[edge]['peso']
		a.target = graph.es[edge].tuple[1]
		listOfArrows.append(a)
	return listOfArrows

myGraph = Graph(directed=True)

myGraph.add_vertices(5)
myGraph.vs['nome'] = ['a','b','c','d','e']
myGraph.add_edges([(0,1), (0,4), (1,2), (1,3), (1,4), (2,4)])
myGraph.es['peso'] = [3,11,3,2,7,2]

costList = 5 * [999]
costList[0] = 0

for vertex in myGraph.vs:
	for actualArrow in runGraph(myGraph,vertex):
		if(costList[actualArrow.origin] + actualArrow.cost < costList[actualArrow.target]):
			costList[actualArrow.target] = costList[actualArrow.origin] + actualArrow.cost

print(costList)