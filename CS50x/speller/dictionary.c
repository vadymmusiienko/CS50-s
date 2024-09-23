// Implements a dictionary's functionality
#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Choose number of buckets in hash table
const unsigned int N = 100000;

// Prototypes
bool free_list(node *cursor);

// Count words in the dictionary
unsigned int count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Find the index
    int hash_value = hash(word);

    // Make case-insensetive
    for (int i = 0; word[i] != 0; i++)
    {
        if (word[i] != tolower(word[i]))
        {
            hash_value -= word[i];
            hash_value += tolower(word[i]);
        }
    }
    unsigned int ind = hash_value % N;

    // Check if in the dictionary
    node *pnt = table[ind];
    while (pnt != NULL)
    {
        if (strcasecmp(pnt->word, word) == 0)
        {
            return true;
        }
        pnt = pnt->next;
    }
    // Not in the dictionary
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Add up all characters (their int value)
    unsigned int temp_sum = 0;
    for (int i = 0; word[i] != 0; i++) // Just word[i]??
    {
        temp_sum += word[i];
        // Empty body
    }

    // return the hash number (mod of a temp_sum)
    return temp_sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Initialize table array to NULL
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    // Open the dictionary
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        return false;
    }

    // Read each word in the file
    char buffer[LENGTH + 1];
    while (fscanf(source, "%s", buffer) != EOF)
    {
        // Create a node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(source);
            unload();
            return false;
        }

        // Put the word into the node
        strcpy(n->word, buffer);

        // Hash function
        unsigned int ind = hash(buffer);

        // Add the node
        n->next = table[ind];
        table[ind] = n;

        // Count the word
        count++;
    }
    // Close the file
    fclose(source);

    // Return true
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        if (!free_list(table[i]))
        {
            return false;
        }
    }

    return true;
}

bool free_list(node *cursor)
{
    if (cursor != NULL)
    {
        free_list(cursor->next);
        free(cursor);
    }

    return true;
}
