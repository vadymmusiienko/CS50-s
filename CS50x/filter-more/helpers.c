#include "helpers.h"
#include <math.h>

#include <stdio.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE *current_pixel;
    int avg, row, column;
    // Loop over each row
    for (row = 0; row < height; row++)
    {
        // Loop over each pixel
        for (column = 0; column < width; column++)
        {
            // Change to grayscale every pixel
            current_pixel = &image[row][column];
            avg = round(((*current_pixel).rgbtBlue + (*current_pixel).rgbtGreen +
                         (*current_pixel).rgbtRed) /
                        3.0);
            (*current_pixel).rgbtBlue = avg;
            (*current_pixel).rgbtGreen = avg;
            (*current_pixel).rgbtRed = avg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int middle = width / 2;
    int row, column;
    RGBTRIPLE buffer;
    // Loop over each row
    for (row = 0; row < height; row++)
    {
        // Loop over each pixel to the left
        for (column = 0; column < middle; column++)
        {
            // Swap the pixel on the left with the pixel on the right
            buffer = image[row][width - column - 1];
            image[row][width - column - 1] = image[row][column];
            image[row][column] = buffer;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    RGBTRIPLE new_image[height][width];
    int row, column, x, y, temp_sumb, temp_sumg, temp_sumr, temp_row, temp_column, avrb, avrg, avrr,
        count;
    // Loop over each row
    for (row = 0; row < height; row++)
    {
        // Loop over each pixel
        for (column = 0; column < width; column++)
        {
            temp_sumb = 0;
            temp_sumg = 0;
            temp_sumr = 0;
            count = 0;

            // Go around the pixel
            for (y = -1; y <= 1; y++)
            {
                for (x = -1; x <= 1; x++)
                {
                    temp_row = row + y;
                    temp_column = column + x;
                    if (0 <= temp_row & temp_row < height && 0 <= temp_column &&
                        temp_column < width)
                    {
                        temp_sumb += image[temp_row][temp_column].rgbtBlue;
                        temp_sumg += image[temp_row][temp_column].rgbtGreen;
                        temp_sumr += image[temp_row][temp_column].rgbtRed;
                        count++;
                    }
                }
            }

            // Find the avarage of r, g, b
            avrb = round(temp_sumb / (float) count);
            avrg = round(temp_sumg / (float) count);
            avrr = round(temp_sumr / (float) count);

            // Copy to the new array (new_image)
            new_image[row][column].rgbtBlue = avrb;
            new_image[row][column].rgbtGreen = avrg;
            new_image[row][column].rgbtRed = avrr;
        }
    }

    // Copy the new image to the old one
    for (row = 0; row < height; row++)
    {
        for (column = 0; column < width; column++)
        {
            image[row][column] = new_image[row][column];
        }
    }

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // New image
    RGBTRIPLE new_image[height][width];

    // Matricies for edges
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    // Varialbes
    int row, column, Xtemp_sumb, Xtemp_sumg, Xtemp_sumr, Ytemp_sumb, Ytemp_sumg, Ytemp_sumr, x, y,
        temp_row, temp_column, newb, newg, newr;

    // Loop over each row
    for (row = 0; row < height; row++)
    {
        // Loop over each pixel
        for (column = 0; column < width; column++)
        {
            // Variables for the current pixel
            Xtemp_sumb = 0;
            Xtemp_sumg = 0;
            Xtemp_sumr = 0;
            Ytemp_sumb = 0;
            Ytemp_sumg = 0;
            Ytemp_sumr = 0;

            // Go around the pixel
            for (y = -1; y <= 1; y++)
            {
                for (x = -1; x <= 1; x++)
                {
                    temp_row = row + y;
                    temp_column = column + x;

                    // Check if the pixel exists
                    if (0 <= temp_row & temp_row < height && 0 <= temp_column &&
                        temp_column < width)
                    {
                        Xtemp_sumb += image[temp_row][temp_column].rgbtBlue * Gx[y + 1][x + 1];
                        Ytemp_sumb += image[temp_row][temp_column].rgbtBlue * Gy[y + 1][x + 1];
                        Xtemp_sumg += image[temp_row][temp_column].rgbtGreen * Gx[y + 1][x + 1];
                        Ytemp_sumg += image[temp_row][temp_column].rgbtGreen * Gy[y + 1][x + 1];
                        Xtemp_sumr += image[temp_row][temp_column].rgbtRed * Gx[y + 1][x + 1];
                        Ytemp_sumr += image[temp_row][temp_column].rgbtRed * Gy[y + 1][x + 1];
                    }
                }
            }
            // Calculate sqrt(Gx^2 + Gy^2)
            newb = round(sqrt(pow(Xtemp_sumb, 2) + pow(Ytemp_sumb, 2)));
            if (newb > 255)
            {
                newb = 255;
            }
            newg = round(sqrt(pow(Xtemp_sumg, 2) + pow(Ytemp_sumg, 2)));
            if (newg > 255)
            {
                newg = 255;
            }
            newr = round(sqrt(pow(Xtemp_sumr, 2) + pow(Ytemp_sumr, 2)));
            if (newr > 255)
            {
                newr = 255;
            }

            new_image[row][column].rgbtBlue = newb;
            new_image[row][column].rgbtGreen = newg;
            new_image[row][column].rgbtRed = newr;
        }
    }

    // Copy the new image to the old one
    for (row = 0; row < height; row++)
    {
        for (column = 0; column < width; column++)
        {
            image[row][column] = new_image[row][column];
        }
    }

    return;
}
