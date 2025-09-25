class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        n = len(s)

        word_freq = Counter(words)
        result = []

        # There are word_len different starting alignments
        for i in range(word_len):
            left = i
            seen = Counter()
            count = 0

            for j in range(i, n - word_len + 1, word_len):
                word = s[j:j+word_len]

                if word in word_freq:
                    seen[word] += 1
                    count += 1

                    # If word appears too many times, shrink window
                    while seen[word] > word_freq[word]:
                        left_word = s[left:left+word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len

                    # If we found a valid substring
                    if count == word_count:
                        result.append(left)

                else:
                    seen.clear()
                    count = 0
                    left = j + word_len

        return result
