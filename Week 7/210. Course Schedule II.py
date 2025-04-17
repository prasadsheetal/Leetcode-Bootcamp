def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = defaultdict(list)

    incoming_edges_count = [0] * numCourses
      
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        incoming_edges_count[course] += 1
      
    course_order = []
      
    queue = deque(course for course, count in enumerate(incoming_edges_count) if count == 0)
      
    while queue:
        current_course = queue.popleft()
        course_order.append(current_course) 
          
        for dependent_course in graph[current_course]:
            incoming_edges_count[dependent_course] -= 1
              
            if incoming_edges_count[dependent_course] == 0:
                queue.append(dependent_course)
      
    return course_order if len(course_order) == numCourses else []
        