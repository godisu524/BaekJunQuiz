N = int(input())
cost_per_home = []

# 각 집마다 색깔 별 가격을 저장한다. 
for _ in range(N):
    cost_per_home.append(list(map(int, input().split())))
    
dp = [cost_per_home[0]]
print(dp)
for i in range(1, N):
    cost_per_color = []
    
    # 맨 처음에 min값을 선택한다고 최종 값이 min이 되는 것이 아니기 때문에,
    # 각 경우의 수를 고려하여 저장해야한다.
    # 빨강색을 선택한다면 이전 값은 다른 색이 되어야 한다.
    # 26 + 57 + 13 이 가능한 것으로 보아, 이웃이 전부 색이 같지 않아야 된다는 뜻은
    # 빨초빨 이 경우는 가능하나 빨빨초 이런 경우만 안된다는 경우로 생각,,
    # 전자의 경우이므로 다음 집을 칠할떄, 내가 칠할 색만 제외하고 다른 경우만 고려해주면 됨.
    temp_red = min(dp[i - 1][1], dp[i - 1][2])
    cost_per_color.append(temp_red + cost_per_home[i][0])

    temp_green = min(dp[i - 1][0], dp[i - 1][2])
    cost_per_color.append(temp_green + cost_per_home[i][1])

    temp_blue = min(dp[i - 1][0], dp[i - 1][1])
    cost_per_color.append(temp_blue + cost_per_home[i][2])
    
    dp.append(cost_per_color)
    print(dp)

print(min(dp[N - 1]))