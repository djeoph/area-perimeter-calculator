
def num_check(question):




 error = "dumby"

 while True:
  try:
       big = float(input(question))

       if big > 0:
           return big
       else:
          print(error)
  except ValueError:
      print(error)

#a dinner routine
for number in range(0, 2):
    width = num_check("thick?")
    print(width)

print()

for number in range(0, 2):
    high = num_check("tall?")
    print(high)