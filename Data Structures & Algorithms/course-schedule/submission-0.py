class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)

        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if len(prereqs[course]) == 0:
                return True
            visited.add(course)
            for p in prereqs[course]:
                if not dfs(p):
                    return False
            prereqs[course] = []
            visited.remove(course)
            return True

            
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
                


        