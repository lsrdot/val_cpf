#!/usr/bin/env -S uv run
import sys
import random


def main() -> int:
    while True:
        print("""\
        (g) - Generate a new valid CPF ID without formatting.
        (G) - Generate a new valid formatted CPF ID.
        (v) - Validate a CPF ID.
        (q) - Exit.
        """)
        response = input("> ").strip()

        if response.lower() == "q":
            print("Bye!")
            break
        elif response == "G":
            cpf = gen_cpf()
            print(f"CPF: {cpf[0:3:1]}.{cpf[3:6:1]}.{cpf[6:9:1]}-{cpf[9::1]}\n")
        elif response == "g":
            print(f"CPF: {gen_cpf()}\n")
        elif response.lower() == "v":
            validate_cpf()
        else:
            print("The provided input isn't valid.\n")
    return 0


def validate_cpf() -> None:
    cpf = (
        input("Paste here the CPF ID. you want to validate: \n> ")
        .strip()
        .replace(".", "")
        .replace("-", "")
    )

    if not cpf.isdigit() or len(cpf) != 11 or cpf == cpf[0] * 11:
        print("The provided input isnt valid!\n")
        return

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
        print("The giving digits form a valid CPF ID.\n")
    else:
        print("The inputed digits don't form a valid CPF ID.\n")


def gen_cpf() -> str:
    digits = ""
    for i in range(9):
        digits += str(random.randint(0, 9))
    if digits == digits[0] * 9:
        return gen_cpf()

    sum = 0
    mult = list(range(10, 1, -1))
    for i in range(9):
        sum += int(digits[i]) * mult[i]
    val_first_digit = (sum * 10) % 11
    if val_first_digit > 9:
        val_first_digit = 0
    digits += str(val_first_digit)

    sum = 0
    mult = list(range(11, 1, -1))
    for i in range(10):
        sum += int(digits[i]) * mult[i]
    val_second_digit = (sum * 10) % 11
    if val_second_digit > 9:
        val_second_digit = 0
    digits += str(val_second_digit)

    return digits


if __name__ == "__main__":
    sys.exit(main())
