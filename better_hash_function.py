def hash_string(keyword, buckets):
    current_letter = ""
    i = 0
    total = 0
    for c in keyword:
        current_letter = ord(c)
        total += current_letter
        mod_total = total % buckets
    return mod_total

print(hash_string('udacity', 12))
