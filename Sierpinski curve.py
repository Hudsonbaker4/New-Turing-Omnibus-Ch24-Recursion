import turtle as t

def zig(n):
  if n == 1:
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
  else:
    zig(n/2)
    zag(n/2)
    zig(n/2)
    zag(n/2)

def zag(n):
  if n == 1:
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
  else:
    zag(n/2)
    zag(n/2)
    zig(n/2)
    zag(n/2)

zig(8)
