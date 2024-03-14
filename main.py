def knapsack_dp(items, max_weight):
  n = len(items)
  dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

  for i in range(n + 1):
      for w in range(max_weight + 1):
          if i == 0 or w == 0:
              dp[i][w] = 0
          elif items[i - 1][1] <= w:
              dp[i][w] = max(items[i - 1][0] + dp[i - 1][w - items[i - 1][1]], dp[i - 1][w])
          else:
              dp[i][w] = dp[i - 1][w]

  total_value = dp[n][max_weight]
  selected_items = []

  i, j = n, max_weight
  while i > 0 and j > 0:
      if dp[i][j] != dp[i - 1][j]:
          selected_items.append(items[i - 1])
          i -= 1
          j -= items[i][1]
      else:
          i -= 1

  return total_value, selected_items

def read_input_from_file(file_path):
  with open(file_path, 'r') as file:
      data = file.read()

  data = data.strip('{},').split(', {{')
  max_weight = int(data[0])
  items_data = data[1].split('}, {')

  items = []
  for item_str in items_data:
      value, weight, _ = map(int, item_str.split(', '))
      items.append((value, weight))

  return items, max_weight

file_path = '10.txt'  # Replace with the path to your input file
items, max_weight = read_input_from_file(file_path)

max_profit, selected_items = knapsack_dp(items, max_weight)
print("Maximum Profit:", max_profit)
print("Selected Items:", selected_items)
