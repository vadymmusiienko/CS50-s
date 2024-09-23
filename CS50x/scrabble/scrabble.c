#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// An array with each letter corresponding to the number of points at the index
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

// A constant which is a number of "A" in ASCII
const int START = 65;

// Prototypes
int points(string word);

int main(void)
{
    // Prompt both users for a word and store the answer in a variable
    string answer1 = get_string("Player 1: ");
    string answer2 = get_string("Player 2: ");

    // Calculate the points and compare them
    int points1 = points(answer1);
    int points2 = points(answer2);

    if (points1 > points2)
    {
        printf("Player 1 wins!\n");
    }
    else if (points1 < points2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int points(string word)
{
    char upper_word;
    int counter = 0;
    for (int i = 0, length = strlen(word); i < length; i++)
    {
        if (isalpha(word[i]))
        {
            upper_word = toupper(word[i]);
            counter += POINTS[upper_word - START];
        }
    }
    return counter;
}
