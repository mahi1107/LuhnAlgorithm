def luhn_check(number: str) -> bool:
    n = len(number)
    total = 0
    is_second = False  

    for i in range(n - 1, -1, -1):  
        digit = int(number[i])  

        if is_second:
            digit *= 2
            if digit > 9:
                digit -= 9

        total += digit
        is_second = not is_second  # flip True <-> False

    return total % 10 == 0


def main():
    number = input("Enter a number: ").strip()
    if luhn_check(number):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
