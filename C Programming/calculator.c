#include <stdio.h>

int main()
{
    float num1, num2, result;
    int choice;

    printf("===== Calculator Program =====\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");

    printf("\nEnter your choice (1-4): ");
    scanf("%d", &choice);

    printf("Enter first number: ");
    scanf("%f", &num1);

    printf("Enter second number: ");
    scanf("%f", &num2);

    switch(choice)
    {
        case 1:
            result = num1 + num2;
            printf("Result = %.2f\n", result);
            break;

        case 2:
            result = num1 - num2;
            printf("Result = %.2f\n", result);
            break;

        case 3:
            result = num1 * num2;
            printf("Result = %.2f\n", result);
            break;

        case 4:
            if(num2 != 0)
            {
                result = num1 / num2;
                printf("Result = %.2f\n", result);
            }
            else
            {
                printf("Division by zero is not possible.\n");
            }
            break;

        default:
            printf("Invalid choice.\n");
    }

    return 0;
}