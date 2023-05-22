def buildLast(pattern):
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0

    buildLast_table = buildLast(pattern)
    shift = 0
    while shift <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            return shift
        else:
            if text[shift + j] in buildLast_table:
                shift += max(1, j - buildLast_table[text[shift + j]])
            else:
                shift += j + 1
    return -1

#print("Hallo ini test case untuk proses string matching")
#text = "Hallo Selamat pagi"
#pattern = "Selamate"
#print(boyer_moore(text, pattern))

