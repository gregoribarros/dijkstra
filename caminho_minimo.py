from igraph import *
import numpy as np

def runGraph(graph):
	listOfEdges = []
	subList = []

	for vertex in graph.vs:
		for edge in graph.incident(vertex):
			origem = graph.es[edge].tuple[0]
			alvo = graph.es[edge].tuple[1]
			subList = [graph.vs[origem]['nome'],graph.es[edge]['peso'],graph.vs[alvo]['nome']]
			listOfEdges.append(subList)
	return listOfEdges


g = Graph(directed=True)

g.add_vertices(5)
g.vs['nome'] = ['a','b','c','d','e']
g.add_edges([(0,1), (0,4), (1,2), (1,3), (1,4), (2,4)])

g.es['peso'] = [3,11,3,2,7,2]

m = np.zeros((5,5),dtype=np.int)
m [0:5,0:5] = 999

for i in range(0,5):
	m[i][i] = 0

listaArestas = []
listaDist = []
i=0

for edge in g.es:
	m[edge.tuple[0]][edge.tuple[1]]=edge['peso']

print(runGraph(g))


nFonte = g.__isub__(g.vs[2])


print(runGraph(nFonte))


#print(listaArestas)
print("\n----------------------grafo-------------------\n")
print(nFonte)
print("\n------------matriz de adjacencia--------------\n")
print(m)
