class RK:
    def search(text, pattern, prime=101):
        if not text or not pattern:
            return -1

        n, m = len(text), len(pattern)
        pattern_hash = 0
        text_hash = 0
        h = 1  # Hash multiplier

        # Calculate hash multiplier
        for i in range(m - 1):
            h = (h * 256) % prime

        # Calculate hash values for the pattern and the first window in the text
        for i in range(m):
            pattern_hash = (256 * pattern_hash + ord(pattern[i])) % prime
            text_hash = (256 * text_hash + ord(text[i])) % prime

        # Slide the pattern over the text and compare hashes
        for i in range(n - m + 1):
            if pattern_hash == text_hash:
                # Check character by character to avoid hash collisions
                if text[i : i + m] == pattern:
                    return i

            # Calculate hash for the next window in the text
            if i < n - m:
                text_hash = (
                    256 * (text_hash - ord(text[i]) * h) + ord(text[i + m])
                ) % prime
                if text_hash < 0:
                    text_hash += prime

        return -1  # Pattern not found
