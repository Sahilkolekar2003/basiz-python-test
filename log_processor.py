def count_error_lines(file):
    count = 0

    with open(file, 'r') as f:
        for line in f:
            if "ERROR" in line:
                count += 1
    return count

print(count_error_lines("large_log.txt"))