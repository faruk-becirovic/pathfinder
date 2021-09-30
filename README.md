# pathfinder
Implementation of breadth-first algorithm for path finding.

# Description
European road network is a serries of roads connecting major European urban centers. The network found under http://konect.cc/networks/subelj_euroroad/ shows a part
of the european road network. The file cityName.csv contains two columns: city ID and Name. Second file, FromTo.csv shows per row a single edge. First columnt shows
from node, while the second shows to node. This algoritym finds shortest reoute for two given cities A and B.

# Input
The input program will accept are the names of the two cities between wich it is necesary to find path.

# Output
The output of the program is the path, a sequence of cities it is necesary to go through tp reach the destination, city B and the distance,
that is the number of edges of the shortest pathe between two cities.
