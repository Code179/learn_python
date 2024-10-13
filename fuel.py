def main():
  while True:
    fraction = input("Fraction: ")
    fuel = convert(fraction)
    if fuel is not None:
      fuel = gauge(fuel)
      print(fuel)
      break

def convert(fraction):
  try:
    left, right = map(int, fraction.split("/"))
    if left > right: raise ValueError("Invalid fraction")
    fuel = round((left / right) * 100)
    return fuel
  except ValueError:
    print("Invalid fraction")
  except ZeroDivisionError:
    print("Cant divide by 0")

def gauge(percentage):
  if percentage >= 99:
      return "F"
  elif percentage <= 1:
      return "E"
  else:
    return f"{percentage}%"


if __name__ == "__main__":
  main()
