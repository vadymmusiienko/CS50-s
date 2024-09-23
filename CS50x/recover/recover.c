#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Constants
const int BLOCK_SIZE = 512;
const int FILE_NAME_SIZE = 8;

// Structures
typedef uint8_t BYTE;
int main(int argc, char *argv[])
{
    // Make sure there is only one comand-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    // Create a buffer for a block of data
    BYTE buffer[BLOCK_SIZE];

    // Create a dynamic filename
    int count = 0;
    char *filename = malloc(FILE_NAME_SIZE);
    if (filename == NULL)
    {
        printf("Not enough memory.\n");
        fclose(card);
        return 2;
    }

    // While there's still data left to read from the memory card
    FILE *img;
    while (fread(buffer, BLOCK_SIZE, 1, card) != 0)
    {
        // First encounter with a jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            // Close previous file (if not first)
            if (count != 0)
            {
                fclose(img);
            }

            // Update the file name
            sprintf(filename, "%03i.jpg", count);

            // Open new file
            img = fopen(filename, "w");
            if (img == NULL)
            {
                printf("Could not open %s.\n", filename);
                fclose(card);
                free(filename);
                return 3;
            }

            // Write an image
            fwrite(buffer, BLOCK_SIZE, 1, img);

            // Add one to the file counter
            count++;
        }
        // Keep writing into the jpeg
        else if (count != 0)
        {
            // Write a block
            fwrite(buffer, BLOCK_SIZE, 1, img);
        }
    }
    // Free mallocs and close the files
    fclose(img);
    fclose(card);
    free(filename);
    return 0;
}
