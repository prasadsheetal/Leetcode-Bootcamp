def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    right_side_view = []
      
    if root is None:
        return right_side_view
      
    queue = deque([root])
      
    while queue:
        right_side_view.append(queue[-1].val)
          
        for _ in range(len(queue)):
            current_node = queue.popleft()
              
            if current_node.left:
                queue.append(current_node.left)
              
            if current_node.right:
                queue.append(current_node.right)
                  
    return right_side_view

        