def create_playfair_grid(key):
  key = key.replace('j', 'i')
  seen = set()
  grid = []
  for char in key:
      if char not in seen and char.isalpha():
          seen.add(char)
          grid.append(char)
  for char in 'abcdefghiklmnopqrstuvwxyz':  # 'j' is omitted
      if char not in seen:
          seen.add(char)
          grid.append(char)

  return [grid[i:i+5] for i in range(0, 25, 5)]
## Creates grid

def find_position(grid, char):
  for row in range(5):
      for col in range(5):
          if grid[row][col] == char:
              return row, col
  return None
## Finds the position of any character in a grid
def decode_playfair_pair(grid, a, b):
  row_a, col_a = find_position(grid, a)
  row_b, col_b = find_position(grid, b)

  if row_a == row_b:
      return grid[row_a][(col_a - 1) % 5] + grid[row_b][(col_b - 1) % 5]
  elif col_a == col_b:
      return grid[(row_a - 1) % 5][col_a] + grid[(row_b - 1) % 5][col_b]
  else:
      return grid[row_a][col_b] + grid[row_b][col_a]
  ## Wrapping around and choosing row immediately left or column immediately up

def decode_playfair_cipher(key, ciphertext):
  grid = create_playfair_grid(key)
  ciphertext = ciphertext.replace('j', 'i')
  words = ciphertext.split()
  decoded_message = []

  for word in words:
      pairs = [word[i:i+2] for i in range(0, len(word), 2)]
      decoded_word = ""
      for pair in pairs:
          if len(pair) == 1:  # Handle odd length words by adding 'x' or 'q'
              pair += 'x' if pair != 'x' else 'q'
          decoded_word += decode_playfair_pair(grid, pair[0], pair[1])
      decoded_message.append(decoded_word)

  return ' '.join(decoded_message)
key = "codingquest"
ciphertext = "rmqfgs yegv em qnpu pdml dc atuy olzy anpu"
decoded_message = decode_playfair_cipher(key, ciphertext)
print(decoded_message)

# Output: please pick up some milk on thex wayx home

