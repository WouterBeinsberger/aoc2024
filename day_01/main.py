def read_document(path: str):
  with open(path, "r") as file:
    return file.read().splitlines()
  
def parse_line_left(document: list[str]):
  left = []

  for line in document:
    line_split = line.split()
    print(f"Line: {line_split}")
    left.append(int(line_split[0]))

  print(f"Left: {left}")
  return left

def parse_line_right(document: list[str]):
  right = []

  for line in document:
    line_split = line.split()
    print(f"Line: {line_split}")
    right.append(int(line_split[-1]))

  print(f"Right: {right}")
  return right

def absolute_value_after_subtraction(left: list[int], right: list[int]):
  abs_values = []

  for i, j in zip(left, right):
    abs_values.append(abs(i - j))

  print(f"Absolute value of substraction: {abs_values}")
  return abs_values

def multiply_by_appearance_in_left_list(left: list[int], right: list[int]):
  multiplied_values = []

  for number in left:
    multiplied_values.append(number * right.count(number))

  print(f"Multiplied values: {multiplied_values}")
  return multiplied_values
  


def main():
  document = read_document("data.txt")
  left = parse_line_left(document)
  right = parse_line_right(document)

  left.sort()
  right.sort()

  abs_values = absolute_value_after_subtraction(left, right)
  sum_abs_values = sum(abs_values)

  multiplied_values = multiply_by_appearance_in_left_list(left, right)
  sum_multiplied_values = sum(multiplied_values)

  print(f"Final sum absolute value: {sum_abs_values}")
  print(f"Final sum multiplied value: {sum_multiplied_values}")

if __name__ == '__main__':
  main()