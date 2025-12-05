def print_levenshtein_matrix(s: str, t: str, d: list[list[int]]) -> None:
    m = len(s)
    n = len(t)

    print('   ', ' '.join(list(t)))

    for i in range(m + 1):
        for j in range(n + 1):
            if j == 0:
                if i > 0:
                    print(s[i - 1], end=' ')
                else:
                    print('  ', end='')
            print(d[i][j], end=' ' if j < n else '')
        print()


def levenshtein_distance(s: str, t: str) -> int:
    m = len(s)
    n = len(t)

    # for all i and j, d[i,j] will hold the Levenshtein distance between
    # the first i characters of s and the first j characters of t
    # set each element in d to zero
    d: list[list[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # source prefixes can be transformed into empty string by
    # dropping all characters
    for i in range(m + 1):
        d[i][0] = i

    # target prefixes can be reached from empty source prefix
    # by inserting every character
    for j in range(n + 1):
        d[0][j] = j

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            substitution_cost: int

            if s[i - 1] == t[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            d[i][j] = min(
                d[i-1][j] + 1,                  # deletion
                d[i][j-1] + 1,                  # insertion
                d[i-1][j-1] + substitution_cost # substitution
            )

    # print_levenshtein_matrix(s, t, d)
    return d[m][n]


unit_tests: list[tuple[str, str, int]] = [
    ('', '', 0),
    ('Different', 'Different', 0),
    ('A', '', 1),
    ('', 'w', 1),
    ('Java', 'JavaScript', 6),
    ("atomic", "atom", 2),
    ("object", "inject", 2),
    ("flaw", "lawn", 2),
    ("A", "Z", 1),
    ('gattaca', 'tataa', 3),
    ('attaca', 'tataa', 3),
    ('bullfrog', 'frogger', 7),
    ('sitting', 'kitten', 3),
    ('Sunday', 'Saturday', 3)
]


def main(run_unit_tests: bool) -> None:
    if run_unit_tests:
        passed: int = 0
        total: int = len(unit_tests)
        for unit_test in unit_tests:
            str1: str = unit_test[0]
            str2: str = unit_test[1]
            expected_cost: int = unit_test[2]

            actual_cost: int = levenshtein_distance(str1, str2)
            if actual_cost == expected_cost:
                print(f'\033[92m✓\033[0m PASS: ({actual_cost} = {expected_cost})')
                passed += 1
            else:
                print(f'\033[91m✗\033[0m FAIL: ({actual_cost} ≠ {expected_cost})')

        if passed == total:
            print(f'\033[92m{passed}\033[0m/{total} Passed')
        else:
            print(f'\033[91m{passed}\033[0m/{total} Failed')


if __name__ == "__main__":
    main(True)
