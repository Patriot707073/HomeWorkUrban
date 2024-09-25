def calculate_sum(data):
  def recursive_sum(item, current_sum=0):
      if isinstance(item, int):
          current_sum += item
      elif isinstance(item, str):
          current_sum += len(item)
      elif isinstance(item, (list, tuple, set)):
          for elem in item:
              current_sum = recursive_sum(elem, current_sum)
      elif isinstance(item, dict):
          for key, value in item.items():
              current_sum = recursive_sum(key, current_sum)
              current_sum = recursive_sum(value, current_sum)

      return current_sum

  return recursive_sum(data)

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_sum(data_structure)
print(result)