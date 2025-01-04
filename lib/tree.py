class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    result = []
    nodes_to_visit = [self.root]
    while nodes_to_visit:
      current_node = nodes_to_visit.pop()

      if current_node['id'] == id:
        return current_node
      
      nodes_to_visit.extend(current_node.get('children', []))

    return None


