#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// Prototypes
int letter_counter(string s, int len);
int word_counter(string s, int len);
int sentence_counter(string s, int len);
int cl_index(int l, int w, int s);

int main(void)
{
    // Ask the user for some text
    string text = get_string("Text: ");

    // Find the length of the text
    int length = strlen(text);

    // Calculate letters, words and sentences
    int letters = letter_counter(text, length);
    int words = word_counter(text, length);
    int sentences = sentence_counter(text, length);

    // Calculate Coleman-Liau index
    int grade = cl_index(letters, words, sentences);

    // Print out the grade level
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

int letter_counter(string s, int len)
{
    // Letter counter
    int letters = 0;

    // Calculate letters
    for (int i = 0; i < len; i++)
    {
        if (isalpha(s[i]))
        {
            letters += 1;
        }
    }
    return letters;
}

int word_counter(string s, int len)
{

    // Word  counter
    int words = 0;

    // Calculate words
    for (int i = 0; i < len; i++)
    {
        char character = s[i];
        if (isspace(character))
        // Calculate whitespaces
        {
            words += 1;
        }
    }
    return words + 1;
}

int sentence_counter(string s, int len)
{
    // Sentence counter
    int sentences = 0;

    // Calculate sentences
    for (int i = 0; i < len; i++)
    {
        char character = s[i];
        if (character == '.' || character == '!' || character == '?')
        {
            sentences += 1;
        }
    }
    return sentences;
}

int cl_index(int l, int w, int s)
{
    // Calculate the avarages (L and S)
    float let_per_word = (l / (float) w) * 100;
    float sent_per_word = (s / (float) w) * 100;

    // Calculate the formula
    float index = 0.0588 * let_per_word - 0.296 * sent_per_word - 15.8;

    return round(index);
}
