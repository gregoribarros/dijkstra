from igraph import *
import numpy as np

def runGraph(graph,vertex):
	listOfEdges = []
	subList = []
	for edge in graph.incident(vertex):
		origem = graph.es[edge].tuple[0]
		alvo = graph.es[edge].tuple[1]
		subList = [origem,graph.es[edge]['peso'],alvo]
		listOfEdges.append(subList)
	return listOfEdges

myGraph = Graph(directed=True)

myGraph.add_vertices(5)
myGraph.vs['nome'] = ['a','b','c','d','e']
myGraph.add_edges([(0,1), (0,4), (1,2), (1,3), (1,4), (2,4)])
myGraph.es['peso'] = [3,11,3,2,7,2]

costList = 5 * [999]
costList[0] = 0

for arrow in runGraph(myGraph,myGraph.vs[0]):
	costList[arrow[2]]=arrow[1]

for vertex in myGraph.vs:
	print (vertex['nome'])
	for actualArrow in runGraph(myGraph,vertex):
		if(costList[actualArrow[0]]+actualArrow[1]<costList[actualArrow[2]]):
			costList[actualArrow[2]]= costList[actualArrow[0]]+actualArrow[1]
	print(costList)