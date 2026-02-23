import sys


def main() -> int:
    cpf = input().strip().replace(".", "").replace("-", "")
    if not cpf.isdigit() or len(cpf) != 11 or cpf == cpf[0] * 11:
        print("The provided input isnt valid.")
        return -1

    sum = 0
    mult = list(range(10, 1, -1))
    for i in range(9):
        sum += int(cpf[i]) * mult[i]
    val_first_digit = sum * 10
    val_first_digit = val_first_digit % 11
    if val_first_digit > 9:
        val_first_digit = 0

    sum = 0
    mult = list(range(11, 1, -1))
    for i in range(10):
        sum += int(cpf[i]) * mult[i]
    val_second_digit = sum * 10
    val_second_digit = val_second_digit % 11
    if val_second_digit > 9:
        val_second_digit = 0

    val_cpf = cpf[:9] + str(val_first_digit) + str(val_second_digit)
    if val_cpf == cpf:
        print("The giving digits form a valid CPF ID.")
    else:
        print("The inputed digits don't form a valid CPF ID.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
