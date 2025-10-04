N = int(input())
myList = []

element = map(int, input().split())
myList = list(element)
for i in range(N):
    print(myList[i]**2, end=" ")