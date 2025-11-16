class Node:
  def __init__(self, value, link_node=None):
    # Initialize node with a value and optional link to the next node
    self.value = value
    self.link_node = link_node

  def set_link_node(self, link_node):
    # Update the link to point to a different node
    self.link_node = link_node

  def get_link_node(self):
    # Return the node that this node is linked to (next node)
    return self.link_node

  def get_value(self):
    # Return the value stored in this node
    return self.value
 
# Creating Nodes not linked to each other
# yacko, wacko, and dot are characters with different descriptions as their values
yacko = Node("likes to yak", None)
wacko = Node("has a penchant for hoarding snacks", None)
dot = Node("enjoys spending time in movie lots", None)

# Linking Nodes using our set_link_node method
# dot now points to wacko, and yacko points to dot, forming a chain: yacko -> dot -> wacko
dot.set_link_node(wacko)
yacko.set_link_node(dot)

# Accessing and printing the data using linked nodes
# yacko.get_link_node() points to dot, and we fetch its value
dots_data = yacko.get_link_node().get_value()

# dot.get_link_node() points to wacko, and we fetch its value
wackos_data = dot.get_link_node().get_value()

# Printing the values stored in the linked nodes
print(dots_data)  # Output: enjoys spending time in movie lots
print(wackos_data)  # Output: has a penchant for hoarding snacks