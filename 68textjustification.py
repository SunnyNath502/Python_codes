class Solution:
    def fullJustify(self, words, maxWidth):
        ans = []
        n = len(words)
        i = 0

        while i < n:
            line_length = len(words[i])
            j = i + 1
            # Keep adding words until the line exceeds the maximum width
            while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1
            num_words = j - i
            num_spaces = maxWidth - line_length
            # Construct justified line
            line = ""

            if num_words == 1 or j == n:
                line = words[i]
                for k in range(i + 1, j):
                    line += ' ' + words[k]
                line += ' ' * (maxWidth - len(line))
            else:
                space_between_words = num_spaces // (num_words - 1)
                extra_spaces = num_spaces % (num_words - 1)

                line = words[i]
                for k in range(i + 1, j):
                    line += ' ' * space_between_words
                    if extra_spaces > 0:
                        line += ' '
                        extra_spaces -= 1
                    line += words[k]
            ans.append(line)
            i = j

        return ans
