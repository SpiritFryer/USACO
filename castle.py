"""
ID: seishin1
LANG: PYTHON3
TASK: castle
"""
# component(i) denotes the
# component that node i is in
#  1 function flood_fill(new_component)
#
#  2 do
#  3   num_visited = 0
#  4   for all nodes i
#  5     if component(i) = -2
#  6       num_visited = num_visited + 1
#  7       component(i) = new_component
#  8       for all neighbors j of node i
#  9         if component(j) = nil
# 10           component(j) = -2
# 11 until num_visited = 0
#
# 12 function find_components
#
# 13  num_components = 0
# 14  for all nodes i
# 15    component(node i) = nil
# 16  for all nodes i
# 17    if component(node i) is nil
# 18      num_components =
#                  num_components + 1
# 19      component(i) = -2
# 20      flood_fill(component
#                         num_components)


def add_to_component(node_id, new_component, new_component_id, adj_list, nodes_to_components):
  # node_id is already in new_component

  # For each neighbor, add it and its neighbors to new_component, if they're not in yet.
  queue = [node_id]
  while queue:  # While queue is not empty
    current_node = queue.pop(0)
    for neighbor_node in adj_list[current_node]:
      if neighbor_node not in new_component:
        new_component.add(neighbor_node)
        nodes_to_components[neighbor_node] = new_component_id
        queue.append(neighbor_node)


def generate_components(adj_list):
  components = []
  nodes_to_components = [None for _ in range(len(adj_list))]
  for node_id in range(len(adj_list)):
    if nodes_to_components[node_id] is None:  # node_id is not in a component yet
      new_component = set()
      new_component.add(node_id)
      components.append(new_component)
      new_component_id = len(components) - 1
      nodes_to_components[node_id] = new_component_id
      add_to_component(node_id, new_component, new_component_id, adj_list, nodes_to_components)

  return components, nodes_to_components


fin = open('castle.in', 'r')
fout = open('castle.out', 'w')

# Input: n rows, each containing m integers, to describe the n*m castle floorspace.
# Each integer is a sum of four possible numbers, to indicate which of the four cardinal directions contains a wall.
# 1: wall to the west
# 2: wall to the north
# 4: wall to the east
# 8: wall to the south
# I.e.:
# 0: No walls
# 1: Wall to West
# 2: Wall to North
# 3: Wall to North + West
# 4: Wall to East
# 5: Wall to East + West
# 6: Wall to East + North
# 7: Wall to East + North + West
# 8: Wall to South
# 9: Wall to South + West
# 10: Wall to South + North
# 11: Wall to South + North + West
# 12: Wall to South + East
# 13: Wall to South + East + West
# 14: Wall to South + East + North
# 15: Wall to South + East + North + West

m,n = map(int, fin.readline().split())

# Castle: graph where nodes are tiles. Walls between tiles indicate no connectivity.
# No walls between tiles indicate that there is an undirected edge.
# Use an adjacency matrix, to make it easy to calculate the transitive closure later.
# Nvm, we used an adjacency list as we never would have made use of an adj. matrix's properties.

# Input affordance: Castle always has at least 2 rooms and at least 1 wall that can be removed.

castle_adj_list = [set() for _ in range(m*n)]
# A node id at a given row i (0 to n-1), column j (0 to m-1) is i*n + j

walls_between_nodes = list()  # List of tuples of what nodes have walls between them.

input_rows = list(list(map(int, line.split())) for line in fin)  # m integers
print('Input:', input_rows)

for j in range(m):
  for i in range(n - 1, -1, -1):
    current_tile_walls = input_rows[i][j]
    connected = [True, True, True, True]  # Connected West, North, East, South.
    if current_tile_walls >= 8:  # Wall to the South
      connected[3] = False
      current_tile_walls -= 8
    if current_tile_walls >= 4:  # Wall to the East
      connected[2] = False
      current_tile_walls -= 4
    if current_tile_walls >= 2:  # Wall to the North
      connected[1] = False
      current_tile_walls -= 2
    if current_tile_walls >= 1:  # Wall to the West
      connected[0] = False
      current_tile_walls -= 1

    # Affordance: Input always puts walls on the outermost layer, so no need to check for edge.
    # on_west_edge = j == 0
    on_east_edge = j == m - 1
    on_north_edge = i == 0
    # on_south_edge = i == n - 1

    current_node_id = i*m + j
    node_west_id = i*m + (j - 1)
    node_east_id = i*m + (j + 1)
    node_north_id = (i - 1)*m + j
    node_south_id = (i + 1)*m + j

    if connected[1]:  # If can move North
      castle_adj_list[current_node_id].add(node_north_id)
      castle_adj_list[node_north_id].add(current_node_id)
    else:
      # If we are on the outermost layer, then no need to save walls between outside and inside.
      if not on_north_edge:
        walls_between_nodes.append((min(current_node_id, node_north_id),
                                    max(current_node_id, node_north_id),
                                    '{} {} N'.format(i + 1, j + 1)))

    if connected[3]:  # If can move South
      castle_adj_list[current_node_id].add(node_south_id)
      castle_adj_list[node_south_id].add(current_node_id)
    # else:  # No need to run. South walls will have already been added as North walls previously.
    #   # If we are on the outermost layer, then no need to save walls between outside and inside.
    #   if not on_south_edge:
    #     walls_between_nodes.add((min(current_node_id, node_south_id), max(current_node_id, node_south_id)))

    if connected[2]:  # If can move East
      castle_adj_list[current_node_id].add(node_east_id)
      castle_adj_list[node_east_id].add(current_node_id)
    else:
      # If we are on the outermost layer, then no need to save walls between outside and inside.
      if not on_east_edge:
        walls_between_nodes.append((min(current_node_id, node_east_id),
                                    max(current_node_id, node_east_id),
                                    '{} {} E'.format(i + 1, j + 1)))

    if connected[0]:  # If can move West
      castle_adj_list[current_node_id].add(node_west_id)
      castle_adj_list[node_west_id].add(current_node_id)
    # else:  # No need to run. West walls will have already been added as East walls previously.
    #   # If we are on the outermost layer, then no need to save walls between outside and inside.
    #   if not on_west_edge:
    #     walls_between_nodes.add((min(current_node_id, node_west_id), max(current_node_id, node_west_id)))



print('Adj list:')
#print('\n'.join(str(row) for row in castle_adj_list))
print('\n'.join(str(id) + ': ' + str(sorted(list(row))) for id, row in enumerate(castle_adj_list)))

print('Walls between nodes:')
print(sorted(walls_between_nodes))

components, nodes_to_components = generate_components(castle_adj_list)

component_lengths = [len(c) for c in components]

print('Components:\n', components)
print('Nodes to components:\n', nodes_to_components)
print('Component lengths:\n', component_lengths)

num_castle_rooms = len(components)
current_largest_room = max(component_lengths)

print('Number of castle rooms:\n', num_castle_rooms)
print('Current largest room:\n', current_largest_room)

max_largest_room_size = current_largest_room
wall_to_remove = None
# Try removing each wall, see if it results in a bigger room.

for wall in walls_between_nodes:
  wall_0_comp = nodes_to_components[wall[0]]
  wall_1_comp = nodes_to_components[wall[1]]
  if wall_0_comp != wall_1_comp:
    new_big_room_size = component_lengths[wall_0_comp] + component_lengths[wall_1_comp]
    if new_big_room_size > max_largest_room_size:
      max_largest_room_size = new_big_room_size
      wall_to_remove = wall

print('max_largest_room_size:\n', max_largest_room_size)
print('wall_to_remove:\n', wall_to_remove)

print('Output:', num_castle_rooms, current_largest_room, max_largest_room_size, wall_to_remove[2], sep='\n')

fout.write(str(num_castle_rooms) + '\n'
           + str(current_largest_room) + '\n'
           + str(max_largest_room_size) + '\n'
           + str(wall_to_remove[2]) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

