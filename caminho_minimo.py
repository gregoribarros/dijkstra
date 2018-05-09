from igraph import *
import numpy as np

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

for vertex in g.vs:
	for edge in g.incident(vertex):
		origem = g.es[edge].tuple[0]
		alvo = g.es[edge].tuple[1]
		print(g.vs[origem]['nome'],g.es[edge]['peso'],g.vs[alvo]['nome'])


#print(listaArestas)
print("\n----------------------grafo-------------------\n")
print(g)
print("\n------------matriz de adjacencia--------------\n")
print(m)
