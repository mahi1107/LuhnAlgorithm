#include <stdio.h>
#include <string.h>

int luhnCheck(char number[]) {
    int n = strlen(number);
    int sum = 0;
    int isSecond = 0;  // start from rightmost digit

    for (int i = n - 1; i >= 0; i--) {
        int digit = number[i] - '0';  // convert char to int

        if (isSecond) {
            digit = digit * 2;
            if (digit > 9)
                digit = digit - 9;
        }

        sum += digit;
        isSecond = !isSecond;  // flip 0 <-> 1
    }

    return (sum % 10 == 0);
}

int main() {
    char number[50];

    printf("Enter a number: ");
    scanf("%s", number);

    if (luhnCheck(number))
        printf("Valid \n");
    else
        printf("Invalid \n");

    return 0;
}
