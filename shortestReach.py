# Shortest path from the starting node to all other nodes
import sys

class Graph():

	def __init__(self, num_vertices):
		self.v = num_vertices    #number of vertices in the graph
		self.graph = [[0 for column in range(num_vertices)]
					for row in range(num_vertices)]

	# Function to print graph
	def print_graph(self, dist):    #Dist represents distances from the source
		print ("Source to destination")
		for node in range(self.v):
			print (node, "\t", dist[node])   #Output vertex distance from the source

	# Function to find the shortest Reach. 
	def shortest_reach(self, dist, srSet):   #srSet represent shortest path tree

		# Initialize shortest distance for next node
		min = sys.maxint

		# Check for the neareast vertex not in the set shorest path tree
		for u in range(self.V):
			if dist[u] < min and srSet[u] == False:
				min = dist[u]
				min_index = u

		return min_index

	# Function to find the shortest path algorith of a graph represented by a matrix
	def dijkstra(self, s):

		dist = [sys.maxint] * self.v
		dist[s] = 0
		srSet = [False] * self.v

		for cout in range(self.v):
			
			# Get the minimum distance vertex
			u = self.shortest_reach(dist, srSet)
			
			# Store the minimum distance vertex
			srSet[u] = True
			
			# Update the vertices in the graph but only if the current distance
			# is greater than the new distance
			for a in range(self.v):
				if self.graph[u][a] > 0 and srSet[a] == False and \
				dist[a] > dist[u] + self.graph[u][a]:
						dist[a] = dist[u] + self.graph[u][a]

		self.print_graph(dist)

# Graph construction
g = Graph()
g.graph = [[0, 24, 3, 20],
            [24, 0, 6, 0],
            [3, 0, 6, 12],
            [20, 0, 12, 0],
            ];

g.dijkstra(0);



