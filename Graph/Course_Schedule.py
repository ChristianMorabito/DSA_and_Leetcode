def course_schedule(create_list, array, num_courses):
    prerequisite_map = create_list(array, num_courses)
    print(prerequisite_map)
    visit_set = set()

    def dfs(crs):
        # BASE CASES
        # if course has no prerequisites (list is empty), then it definitely can be completed
        if not prerequisite_map[crs]:
            return True
        # if cycle detected
        if crs in visit_set:
            return False

        visit_set.add(crs)
        for pre in prerequisite_map[crs]:
            if not dfs(pre):
                return False  # returning False ends this function & the main function too.
        # make list empty because it's dfs did not return False, therefore it's recursive path has been checked
        # so it can be cleared (which coincides with the base case for True)
        prerequisite_map[crs] = []  # making this empty will allow the base case to return True.
        return True

    # this loop is necessary to ensure that there are no isolated graphs.
    for course in range(num_courses):
        if not dfs(course):
            return False
    return True


def create_adjacency_list(array, num_courses):
    prerequisite_map = {i: [] for i in range(num_courses)}
    for course, prerequisite in array:
        prerequisite_map[course].append(prerequisite)
    return prerequisite_map


print(course_schedule(create_adjacency_list, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]], 5))
