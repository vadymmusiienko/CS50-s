#include <cs50.h>
#include <stdio.h>

void print_hashes(int num);
int get_height(void);
void pyramid(int h);

int main(void)
{
    pyramid(get_height());
}

int get_height(void)
{
    int h;
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);

    return h;
}

void pyramid(int h)
{
    int i, n;
    // Write a raw
    for (i = 0; i < h; i++)
    {
        // Write the spaces on the left
        for (n = 0; n < h - i - 1; n++)
        {
            printf(" ");
        }

        // Write the hashes on the left
        print_hashes(i + 1);

        // Write the gap in between
        printf("  ");

        // Write the hashes on the right
        print_hashes(i + 1);
        // Add a new line
        printf("\n");
    }
}

void print_hashes(int num)
{
    for (int j = 0; j < num; j++)
    {
        printf("#");
    }
}
