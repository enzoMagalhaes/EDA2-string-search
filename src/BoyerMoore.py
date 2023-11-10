class BM:
    def bad_character_table(pattern):
        table = {}
        m = len(pattern)

        for i in range(m - 1):
            table[pattern[i]] = m - 1 - i

        return table

    def good_suffix_table(pattern):
        m = len(pattern)
        table = [m] * m
        j = m - 1

        for i in range(m - 1, -1, -1):
            if i == m - 1 or pattern[i] == pattern[j]:
                table[j] = j - i + m - 1
                j -= 1

        for i in range(m - 1):
            table[i] = max(table[i], j - i + m)

        return table

    def search(text, pattern):
        if not text or not pattern:
            return -1

        n, m = len(text), len(pattern)
        bad_char_table = BM.bad_character_table(pattern)
        good_suffix_table_values = BM.good_suffix_table(pattern)

        i = m - 1
        while i < n:
            j = m - 1

            while j >= 0 and text[i] == pattern[j]:
                i -= 1
                j -= 1

            if j == -1:
                return i + 1  # Pattern found

            bad_char = bad_char_table.get(text[i], m)
            good_suffix = good_suffix_table_values[j]

            i += max(bad_char, good_suffix)

        return -1  # Pattern not found
