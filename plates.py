def main():
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")

def two_letters(plate):
  return len(plate) >= 2 and plate[0].isalpha() and plate[1].isalpha()


def min_max_char(plate):
  return len(plate) <= 6 and len(plate) >= 2


def no_number_in_middle(plate):
  for i in range(len(plate)):
    if plate[i].isdigit():
      sliced = plate[i:7]
      if sliced.isdigit():
        return True
    elif plate.isalpha():
      return True


def first_number_not_zero(plate):
  return plate[0] != "0"


def no_pun_space_period(plate):
  return plate.isalnum()


def is_valid(plate):
  return two_letters(plate) and min_max_char(plate) and no_number_in_middle(
      plate) and first_number_not_zero(plate) and no_pun_space_period(plate)


if __name__ == "__main__":
  main()
