
n = int(input())

scores = list(map(int, input().split()))

unique_scores = sorted(set(scores))
print(unique_scores)
print(unique_scores[-2])
