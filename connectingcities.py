def count_ways(target, numbers):
  dp = [0] * (target + 1)
  dp[0] = 1
  for i in range(1, target + 1):
      for num in numbers:
          if i - num >= 0:
              dp[i] += dp[i - num]

  return dp[target]
target = 856
numbers = [40, 12, 2,1]
ways = count_ways(target, numbers)
print(f"Number of ways to sum up to {target} using {numbers}: {ways}")

# Output: Number of ways to sum up to 856 using [40, 12, 2, 1]: 361595632332583638761407421958897298379960745882500550853575978681928496636233758054533916390012124244431806190608039087381666468880612638124124662565287224989590899000769252066051