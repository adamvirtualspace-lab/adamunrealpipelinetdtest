def print_pattern():
    cols = 30
    rows = 30
    mid = rows // 2  # 15

    for r in range(rows):
        row = ['xx'] * cols

        for c in range(cols):

            # top diagonal (r 1-4)
            if 1 <= r <= 4:
                if c == mid - r or c == mid + r - 1:
                    row[c] = '--'

            # top horizontal (r 5)
            if r == 5:
                if 5 <= c <= 10 or cols - 11 <= c <= cols - 6:
                    row[c] = '--'

            # middle section (r 6-23): two parts
            # outer vertical fixed at col 5 (rows 6-10 and 19-23)
            # inner diamond continuing inward (rows 11-14 and 15-18)
            if 6 <= r <= 23:
                dist = abs(r - mid)  # distance from center (mid=15)
                left_c = 5 if dist >= 5 else dist
                right_c = cols - 6 if dist >= 5 else cols - 1 - dist
                if c == left_c or c == right_c:
                    row[c] = '--'

            # bottom horizontal (r 24)
            if r == 24:
                if 5 <= c <= 10 or cols - 11 <= c <= cols - 6:
                    row[c] = '--'

            # bottom diagonal (r 25-28)
            if 25 <= r <= 28:
                mirror_r = rows - 1 - r
                if c == mid - mirror_r or c == mid + mirror_r - 1:
                    row[c] = '--'

        print(''.join(row))

print_pattern()