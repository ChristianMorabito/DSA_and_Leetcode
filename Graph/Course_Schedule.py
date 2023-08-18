def course_schedule(prerequisite_map, num_courses):
    visit_set = set()

    def dfs(crs):
        # BASE CASES
        # if course has no prerequisites (list is empty), then it definitely can be completed
        if not prerequisite_map[crs]:
            return True
        # if loop detected
        if crs in visit_set:
            return False

        visit_set.add(crs)
        for pre in prerequisite_map[crs]:
            if not dfs(pre):
                return False
        prerequisite_map[crs] = []
        return True

    for course in range(num_courses):
        if not dfs(course):
            return False
    return True



def create_adjacency_list(array, num_courses):
    prerequisite_map = {i: [] for i in range(num_courses)}
    for course, prerequisite in array:
        prerequisite_map[course].append(prerequisite)
    return prerequisite_map


pre_map = create_adjacency_list([[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]], 5)
print(course_schedule(pre_map, 5))
