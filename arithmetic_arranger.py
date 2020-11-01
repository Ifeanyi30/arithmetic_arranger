def arithmetic_arranger(problems,answer=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  operation = ("+", "-")
  dashes = ''
  first_problems = ''
  second_problems = ''
  displays = ''

  calc = [cal.split(" ") for cal in problems]
  for index,item in enumerate(calc):
      if item[1] not in operation:
          return "Error: Operator must be '+' or '-'."
      if item[1] == '+':
          try:
              result = int(item[0]) + int(item[2])
          except ValueError:
              return 'Error: Numbers must only contain digits.'
      elif item[1] == '-':
          try:
              result = int(item[0]) - int(item[2])
          except ValueError:
              return 'Error: Numbers must only contain digits.'

      if len(item[0]) >4 or len(item[2]) > 4:
          return 'Error: Numbers cannot be more than four digits.'

      score = max(len(item[0]), len(item[2]))
      up_align = " " * (score + 2 - len(item[0])) + item[0]
      down_align = item[1] + " " * (score + 1 - len(item[2])) + item[2]
      display = " " * (score + 2 - len(str(result))) + str(result)

      first_problems += up_align + "    " if index != len(calc)-1 \
            else up_align
      second_problems += down_align + "    " if index != len(calc)-1 \
            else down_align
      dashes += "-" * len(down_align) + "    " if index != len(calc)-1 \
            else "-" * len(down_align)
      displays += display + "    " if index != len(calc)-1 \
            else display
  if answer:
      return first_problems + '\n' + second_problems + '\n' + \
          dashes + '\n' + displays
  return first_problems + '\n' + second_problems + '\n' + \
          dashes
