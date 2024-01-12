
  # x = 25
  # y = 25
  #  def setup():
  #      size(1000,1000)
  #      frameRate(200)
  #      background(1)
  # def draw():
  #     global x, y
  #     ellipse(x, y, 50, 50)
  #     if keyPressed:
  #         background(1)
  #         ellipse(x, y, 50, 50)
  #         if key == 'a' or key == 'A':
  #             x = x - 1
  #         elif key == 'd' or key == 'D':
  #             x = x + 1
  #         elif key == 'w' or key == 'W':
  #             y = y - 1
  #         elif key == 's' or key == 'S':
  #             y = y + 1
# x = 1
# def setup():
#     size(1000,1000)
#     frameRate(1000)
#     background(1)
#     stroke(1)
# def draw():
#     global x
#     if keyPressed:
#         if key == 'r' or key == 'R':
#             fill(255,3,3)
#         elif key == 'o' or key == 'O':
#             fill(255,145,3)
#         elif key == 'y' or key == 'Y':
#             fill(255,245,3)
#         elif key == 'g' or key == 'G':
#             fill(3,255,21)
#         elif key == 'h' or key == 'H':
#             fill(1)
#         elif key == 'w' or key == 'W':
#             fill(255)
#         elif key == 'c' or key == 'C':
#             fill(3,255,240)
#         elif key == 'b' or key == 'B':
#             fill(3,29,255)
#         elif key == 'p' or key == 'P':
#             fill(185,255,3)
#         elif key == 'f' or key == 'F':
#             ellipse(mouseX,mouseY,25,25)
#         elif key == 'l' or key == 'L':
#             clear()
#         elif key == 's' or key == 'S':
#             x = x + 1
#             stroke(x)
#         elif key == 'n' or key == 'N':
#             x = x - 1
#             stroke(x)
# x = 25
# def setup():
#     size(1000,1000)
#     background(1)
#     frameRate(100)
# def draw():
#     global x
#     ellipse(500,500,x,x)
#     if keyPressed:
#         if key == 's' or key == 'S':
#             background(1)
#             x = x + 1
#             ellipse(500,500,x,x)
#         if key == 'n' or key == 'N':
#             background(1)
#             x = x - 1
#             ellipse(500,500,x,x)
#             if x < 1:
#                 x = 1
# def setup():
#     size(1000,1000)
#     background(2)
#     frameRate(100)
#     textSize(30)
# def draw():
#     if keyPressed:
#         background(1)
#         if key == 'q' or key == 'Q':
#             text('q',50,50)
#         if key == 'w' or key == 'W':
#             text('w',50,50)
#         if key == 'e' or key == 'E':
#             text('e',50,50)
#         if key == 'r' or key == 'R':
#             text('r',50,50)
#         if key == 't' or key == 'T':
#             text('t',50,50)
#         if key == 'y' or key == 'Y':
#             text('y',50,50)
#         if key == 'u' or key == 'U':
#             text('u',50,50)
#         if key == 'i' or key == 'I':
#             text('i',50,50)
#         if key == 'o' or key == 'O':
#             text('o',50,50)
#         if key == 'p' or key == 'P':
#             text('p',50,50)
#         if key == 'a' or key == 'A':
#             text('a',50,50)
#         if key == 's' or key == 'S':
#             text('s',50,50)
#         if key == 'd' or key == 'D':
#             text('d',50,50)
#         if key == 'f' or key == 'F':
#             text('f',50,50)
#         if key == 'g' or key == 'G':
#             text('g',50,50)
#         if key == 'h' or key == 'H':
#             text('h',50,50)
#         if key == 'j' or key == 'J':
#             text('j',50,50)
#         if key == 'k' or key == 'K':
#             text('k',50,50)
#         if key == 'l' or key == 'L':
#             text('l',50,50)
#         if key == 'z' or key == 'Z':
#             text('z',50,50)
#         if key == 'x' or key == 'X':
#             text('x',50,50)
#         if key == 'c' or key == 'C':
#             text('c',50,50)
#         if key == 'v' or key == 'V':
#             text('v',50,50)
#         if key == 'b' or key == 'B':
#             text('b',50,50)
#         if key == 'n' or key == 'N':
#             text('n',50,50)
#         if key == 'm' or key == 'M':
#             text('m',50,50)
# x = 50
# def setup():
#     size(1000,1000)
#     background(2)
#     frameRate(10)
#     textSize(30)
# def draw():
#     global x
#     if keyPressed:
#         x = x + 24
#         if key == 'q' or key == 'Q':
#             text('q',x,50)
#         if key == 'w' or key == 'W':
#             text('w',x,50)
#         if key == 'e' or key == 'E':
#             text('e',x,50)
#         if key == 'r' or key == 'R':
#             text('r',x,50)
#         if key == 't' or key == 'T':
#             text('t',x,50)
#         if key == 'y' or key == 'Y':
#             text('y',x,50)
#         if key == 'u' or key == 'U':
#             text('u',x,50)
#         if key == 'i' or key == 'I':
#             text('i',x,50)
#         if key == 'o' or key == 'O':
#             text('o',x,50)
#         if key == 'p' or key == 'P':
#             text('p',x,50)
#         if key == 'a' or key == 'A':
#             text('a',x,50)
#         if key == 's' or key == 'S':
#             text('s',x,50)
#         if key == 'd' or key == 'D':
#             text('d',x,50)
#         if key == 'f' or key == 'F':
#             text('f',x,50)
#         if key == 'g' or key == 'G':
#             text('g',x,50)
#         if key == 'h' or key == 'H':
#             text('h',x,50)
#         if key == 'j' or key == 'J':
#             text('j',x,50)
#         if key == 'k' or key == 'K':
#             text('k',x,50)
#         if key == 'l' or key == 'L':
#             text('l',x,50)
#         if key == 'z' or key == 'Z':
#             text('z',x,50)
#         if key == 'x' or key == 'X':
#             text('x',x,50)
#         if key == 'c' or key == 'C':
#             text('c',x,50)
#         if key == 'v' or key == 'V':
#             text('v',x,50)
#         if key == 'b' or key == 'B':
#             text('b',x,50)
#         if key == 'n' or key == 'N':
#             text('n',x,50)
#         if key == 'm' or key == 'M':
#             text('m',x,50)
#         if key == '`' or key == '~':
#             clear()
#         if key == ' ':
#             text(' ',x,50)
x = 25
y = 25
dirb = 3.2
dira = 2.9
def setup():
    size(1000,1000) 
    background(1)
    frameRate(150)
def draw():
    global x,y,dira,dirb
    background(1)
    ellipse(x,y,50,50)
    x = x + dira
    y = y + dirb
    if x > 975:
        dira = dira - 2.9
    if x < 25:
        dira = dira + 2.9
    if y > 975:
        dirb = dirb - 3.2
    if y < 25:
        dirb = dirb + 3.2
    
      
      


            
        
