#include <cs50.h>
#include <stdio.h>

// functions
int sum_dig(int i);
int check_luhn(long n);
int num_of_dig(long number);
int fst2_dig(long number);
void card_check(long num);

// main
int main(void)
{
    // get a credit card number
    long c_num = get_long("Number: ");

    // check Luhn’s Sum
    if (!check_luhn(c_num))
    {
        card_check(c_num);
    }
    else
    {
        printf("INVALID\n");
    }
}

int check_luhn(long n)
{
    // variable for the doubled sum
    int double_sum = 0;

    // variable for the regular sum
    int reg_sum = 0;

    // find the sums
    while (n)
    {
        reg_sum += n % 10;
        n = n / 10;
        double_sum += sum_dig((n % 10) * 2);
        n = n / 10;
    }

    // checks whether it is valid or not
    return ((double_sum + reg_sum) % 10);
}

int sum_dig(int i)
{
    // check whether it is 1 or 2 digit number
    if (i < 10)
    {
        return i;
    }
    else
    {
        return ((i / 10) + (i % 10));
    }
}

void card_check(long num)
{
    // variables with needed atributes of a number
    int number_of_digits = num_of_dig(num);
    int first_digits = fst2_dig(num);

    // find which card it is
    if ((first_digits == 34 || first_digits == 37) && number_of_digits == 15)
    {
        printf("AMEX\n");
    }
    else if ((first_digits > 50 && first_digits < 56) && number_of_digits == 16)
    {
        printf("MASTERCARD\n");
    }
    else if ((first_digits / 10 == 4) && (number_of_digits == 16 || number_of_digits == 13))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

int num_of_dig(long number)
{
    // check the number of digits
    int counter = 0;
    while (number > 0)
    {
        number = number / 10;
        counter++;
    }
    return counter;
}

int fst2_dig(long number)
{
    // find the first 2 digits of a number
    while (number > 99)
    {
        number = number / 10;
    }
    return number;
}
