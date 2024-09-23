#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool cycle(int current_loser, bool seen[]);

// Main
int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // Check if the name is valid
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i]) == 0)
        {
            // Update candidates ranking
            ranks[rank] = i;
            return true;
        }
    }

    // Candidate does not exist
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // Update preferences array
    for (int i = 0; i < candidate_count; i++)

    { // The candidate we are currently looking at (i is his place/ranking)
        int current_candidate = ranks[i];

        // Candidate preference (he is over ...)
        for (int j = i + 1; j < candidate_count; j++)
        {
            preferences[current_candidate][ranks[j]]++;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    pair_count = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            if (preferences[i][j] > preferences[j][i])
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pair_count++;
            }
            else if (preferences[i][j] < preferences[j][i])
            {
                pairs[pair_count].winner = j;
                pairs[pair_count].loser = i;
                pair_count++;
            }
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // Variables for the sort algorithm
    int strongest;
    int current_strength;
    int index;
    pair before;
    pair after;

    // Selection sort
    for (int left = 0; left < pair_count; left++)
    {
        // Set the left pointer
        strongest = preferences[pairs[left].winner][pairs[left].loser] -
                    preferences[pairs[left].loser][pairs[left].winner];
        index = left;

        // Find the biggest strength and its index
        for (int right = left + 1; right < pair_count; right++)
        {
            current_strength = preferences[pairs[right].winner][pairs[right].loser] -
                               preferences[pairs[right].loser][pairs[right].winner];
            if (current_strength > strongest)
            {
                strongest = current_strength;
                index = right;
            }
        }

        // Swap the first element and the biggest
        before = pairs[left];
        pairs[left] = pairs[index];
        pairs[index] = before;
    }

    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    bool seen_candidates[candidate_count];
    // Lock in each pair
    for (int i = 0; i < pair_count; i++)
    {
        // create a seen array with seen candidates
        for (int j = 0; j < candidate_count; j++)
        {
            seen_candidates[j] = false;
        }
        for (int z = 0; z <= i; z++)
        {
            seen_candidates[pairs[z].winner] = true;
        }

        // Check if creates a cycle, if not - lock in a pair
        if (!cycle(pairs[i].loser, seen_candidates))
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
    }

    return;
}

// Determine whether there is a cycle or not (recursion)
bool cycle(int current_loser, bool seen[])
{
    // Check if there are arrows from this candidate
    for (int i = 0; i < pair_count; i++)
    {
        if (locked[current_loser][i] == true)
        {
            // indicate that we've seen this person (current_pair.loser)
            seen[current_loser] = true;

            // Check whether we have seen this person in a cycle before (Base case)
            if (seen[i])
            {
                return true;
            }

            // Recursive case
            return cycle(i, seen);
        }
    }

    // No arrows from the loser to someone else
    return false;
}

// Print the winner of the election
void print_winner(void)
{
    int counter;
    for (int i = 0; i < pair_count; i++)
    {
        counter = 0;
        for (int j = 0; j < pair_count; j++)
        {
            if (!locked[j][i])
            {
                counter++;
            }
        }

        if (counter == pair_count)
        {
            printf("%s\n", candidates[i]);
            return;
        }
    }

    return;
}
