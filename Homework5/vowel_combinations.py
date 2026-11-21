# First we define the three helper functions to check 1,2 or 3 symbols

# True if a "." starts at offset
def vowel_at_position_with_len_1(offset, morse_code_list):
    E = "."
    if offset < len(morse_code_list):
        if morse_code_list[offset] == E:
            return True
    return False

# True if a ".." or ".-" starts at offset
def vowel_at_position_with_len_2(offset, morse_code_list):
    I = ".."
    A = ".-"
    if offset < len(morse_code_list) - 1:
        # Also make sure there are enough symbols left
        current_two_char_value = morse_code_list[offset] + morse_code_list[offset + 1]
        if current_two_char_value == A or current_two_char_value == I:
            return True
    return False

# True if a "..-" or "---" starts at offset
def vowel_at_position_with_len_3(offset, morse_code_list):
    O = "---"
    U = "..-"
    if offset < len(morse_code_list) - 2:
        # Also make sure there are enough symbols left
        current_three_char_value = (morse_code_list[offset]
                                    + morse_code_list[offset + 1]
                                    + morse_code_list[offset + 2])
        if current_three_char_value == O or current_three_char_value == U:
            return True
    return False

def reverse_vowel_at_diagonal_position(offset, num_vowels_matrix):
    """P(offset) = M[1][offset-1] + M[2][offset-2] + M[3][offset-3].
        Terms with a negative index are left out.
        The matrix has one row per offset: M[len][offset] is num_vowels_matrix[offset][len-1].
        """
    total = 0
    if offset - 1 >= 0:
        total += num_vowels_matrix[offset - 1][0]
    if offset - 2 >= 0:
        total += num_vowels_matrix[offset - 2][1]
    if offset - 3 >= 0:
        total += num_vowels_matrix[offset - 3][2]
    return total

def vowel_combinations(morse_code_list):
    n = len(morse_code_list)
    # one row per offset, three columns for vowels lengths 1,2,3
    num_vowels_matrix = [[0, 0, 0] for _ in range(n)]

    for offset in range(n):
        # P(offset): ways to decode everything before this offset
        if offset == 0:
            ways_before = 1     # base case: P(0) = 1
        else:
            ways_before = reverse_vowel_at_diagonal_position(offset, num_vowels_matrix)

        if vowel_at_position_with_len_1(offset, morse_code_list):
            num_vowels_matrix[offset][0] = ways_before
        if vowel_at_position_with_len_2(offset, morse_code_list):
            num_vowels_matrix[offset][1] = ways_before
        if vowel_at_position_with_len_3(offset, morse_code_list):
            num_vowels_matrix[offset][2] = ways_before

    # answer = P(n) : the same diagonal, one column past the end
    return reverse_vowel_at_diagonal_position(n, num_vowels_matrix)


def main():
    n = int(input())                          # first line: length
    morse_code_list = list(input().strip())   # second line, as a list of symbols
    print("The Number of Vowel combinations is:", vowel_combinations(morse_code_list))


if __name__ == "__main__":
    main()




