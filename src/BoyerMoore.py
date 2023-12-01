class BM:
    def generate_bad_char_table(pattern):
        table = {}
        pattern_length = len(pattern)

        for i in range(pattern_length - 1):
            table[pattern[i]] = pattern_length - 1 - i

        return table

    def generate_good_suffix_table(pattern):
        pattern_length = len(pattern)
        suffixes = [0] * pattern_length
        last_prefix_position = pattern_length

        for i in range(pattern_length - 1, -1, -1):
            if BM.is_suffix(pattern, i + 1):
                last_prefix_position = i + 1
            suffixes[i] = last_prefix_position - (pattern_length - 1 - i)

        for i in range(pattern_length - 1):
            j = BM.compute_prefix(pattern, i)
            if i + j < pattern_length and pattern[i + j] != pattern[j]:
                suffixes[pattern_length - 1 - j] = pattern_length - 1 - i + j

        return suffixes

    def is_suffix(pattern, i):
        pattern_length = len(pattern)
        suffix_length = pattern_length - i
        suffix = pattern[i:pattern_length]
        return suffix == pattern[0:suffix_length]

    def compute_prefix(pattern, i):
        j = 0
        pattern_length = len(pattern)

        while i + j < pattern_length and pattern[i + j] == pattern[j]:
            j += 1

        return j

    def search(text, pattern):
        bad_char_table = BM.generate_bad_char_table(pattern)
        good_suffix_table = BM.generate_good_suffix_table(pattern)

        text_length = len(text)
        pattern_length = len(pattern)
        i = 0

        while i <= text_length - pattern_length:
            j = pattern_length - 1

            while j >= 0 and pattern[j] == text[i + j]:
                j -= 1

            if j < 0:
                return i  # Match found

            bad_char = bad_char_table.get(text[i + j], pattern_length)
            good_suffix = good_suffix_table[j]

            i += max(bad_char, good_suffix)

        return -1  # No match found
