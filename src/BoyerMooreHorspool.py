class BMH:
    def bad_character_table(pattern):
        table = {}
        m = len(pattern)

        for i in range(m - 1):
            table[pattern[i]] = m - 1 - i

        return table

    def search(text, pattern):
        if not text or not pattern:
            return -1

        n, m = len(text), len(pattern)
        bad_char_table = BMH.bad_character_table(pattern)

        i = m - 1
        while i < n:
            j = m - 1

            while j >= 0 and text[i] == pattern[j]:
                i -= 1
                j -= 1

            if j == -1:
                return i + 1  # Pattern found

            bad_char = bad_char_table.get(text[i], m)

            i += bad_char

        return -1  # Pattern not found
