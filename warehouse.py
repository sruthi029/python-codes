def minimum_vehicles(weights, max_limit):
    placementlelo = sorted(filter(lambda x: x != 0, weights), reverse=True)

    left, right = 0, len(placementlelo) - 1
    vehicles = 0

    while left <= right:
        if placementlelo[left] + placementlelo[right] <= max_limit:
            right -= 1
        left += 1
        vehicles += 1

    return vehicles

weights = list(map(int, input().split()))
max_limit = int(input())

result = minimum_vehicles(weights, max_limit)
print(result, end="")


