import re

def recurse(elements):
  with open('bags.txt', 'r') as f:
    for line in f:
      line = line.rstrip()
      for i in elements:
        if line.startswith(i):
          line = line.split("contain")
          x = re.findall("[0-9]\s[a-z]+\s[a-z]+\sbag", line[1])
          for bag in x:
            if bag not in elements:
              elements.append(bag)
          break
  print(elements)
  x = 0
  count = 0
  for bags in elements:
    print(bags[x][0])
  print(count)
  return recurse(elements)



elements = ['shiny gold bag', 'dark brown bag', 'mirrored coral bag', 'faded olive bag', 'posh bronze bag', 'shiny olive bag', 'dull aqua bag', 'clear coral bag', 'dotted lime bag', 'dim red bag', 'pale aqua bag', 'dark gray bag']

recurse (elements)
