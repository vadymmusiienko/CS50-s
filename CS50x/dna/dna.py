import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: dna.py [STR data base] [DNA sequence]")
        sys.exit(1)

    # Read database file into a variable
    database_file = open(sys.argv[1], "r")
    database = list(csv.DictReader(database_file))

    # Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as dna_file:
        dna = dna_file.read()

    # Find longest match of each STR in DNA sequence
    subsequences = list(database[0].keys())
    subsequences.pop(0)
    counts = {}
    for i in range(0, len(subsequences)):
        counts[subsequences[i]] = longest_match(dna, subsequences[i])

    # Check database for matching profiles
    for row in database:
        for subsequence in subsequences:
            if int(row[subsequence]) != counts[subsequence]:
                break
        else:
            print(row["name"])
            database_file.close()
            return

    print("No match")
    database_file.close()
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
