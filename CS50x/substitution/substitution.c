#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Constants
const int KEY_LENGTH = 26;

// Prototypes
string upper_string(string word);
int validate(string key);
string encrypt(string message, string key);

int main(int argc, string argv[])
{
    // Make sure to get a key
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Get an uppercase key
    string key = upper_string(argv[1]);

    // Validate the key
    if (!validate(key))
    {
        return 1;
    }

    // Get a plaintext
    string plaintext = get_string("plaintext:  ");

    // Encrypt the message
    string ciphertext = encrypt(plaintext, key);

    // Print out the encrypted message
    printf("ciphertext: %s\n", ciphertext);

    return 0;
}

string upper_string(string word)
{
    for (int i = 0; i < KEY_LENGTH; i++)
    {
        word[i] = toupper(word[i]);
    }
    return word;
}

int validate(string key)
{
    // Make sure the key has 26 characters
    if (strlen(key) != KEY_LENGTH)
    {
        printf("Key must contain 26 characters.\n");
        return 0;
    }

    // Validate the key (Only non-repetative alphabetical characters)
    for (int i = 0; i < KEY_LENGTH; i++)
    {
        char character = key[i];
        // Check for for letters
        if (!isalpha(character))
        {
            printf("Key must contain only alphabetic characters.\n");
            return 0;
        }
        // Check for repetition
        for (int j = i + 1; j < KEY_LENGTH; j++)
        {
            if (character == key[j])
            {
                printf("Key must not contain repeated characters.\n");
                return 0;
            }
        }
    }
    return 1;
}

string encrypt(string message, string key)
{
    // Encrypt the message
    for (int i = 0, length = strlen(message); i < length; i++)
    {
        // Current letter in the original message
        char character = message[i];

        // Chech if an alpha letter
        if (isalpha(character))
        {
            // Upper case
            if (isupper(character))
            {
                int index = message[i] - 'A';
                message[i] = key[index];
            }
            // Lower case
            else
            {
                int index = message[i] - 'a';
                message[i] = tolower(key[index]);
            }
        }
    }
    return message;
}
