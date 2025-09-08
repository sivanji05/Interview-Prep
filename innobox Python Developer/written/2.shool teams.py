# """    SCHOOL TEAMS  Problem    """

# def schoolTeams(N, A):
#     visited = set()  # Set to track visited students
#     teams = 0  # Counter for the number of teams

#     for i in range(N):  # Loop through each student
#         if i + 1 not in visited:  # If student is not visited, start a new team
#             teams += 1  # A new cycle (team) is found
#             current = i + 1  # Start from this student
            
#             # Follow the cycle until we revisit a node
#             while current not in visited:
#                 visited.add(current)  # Mark the student as visited
#                 current = A[current - 1]  # Move to the next student in the cycle

#     return teams  # Return the number of teams

# # Input handling
# N = int(input())  # Read number of students
# A = list(map(int, input().split()))  # Read the teammate array

# # Output the result
# print(schoolTeams(N, A))







def school_teams(n,a):
    visited=set()
    team=0
    for i in range(n):
        if i+1 not in visited:
            team+=1
            current=i+1

            while current not in visited:
                visited.add(current)  
                current = a[current - 1]

    return team

n=int(input())
a=list(map(int,input().split()))

result=school_teams(n,a)
print(result)
