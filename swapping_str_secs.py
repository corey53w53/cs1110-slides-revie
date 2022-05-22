def swap_str_section(word,a,b):
    if not a in word or not b in word:
        return str(word)
    a_start = word.find(a)
    b_start = word.find(b)
    a_end = a_start + len(a) - 1
    b_end = b_start + len(b) - 1
    if a_start>=b_start and a_start<=b_end:
        return str(word)
    if a_end>=b_start and a_end<=b_end:
        return str(word)
    if b_start>=a_start and b_start<=a_end:
        return str(word)
    if b_end>=a_start and b_end<=a_end:
        return str(word)
    if b_start<a_start:
        temp = b_start
        b_start = a_start
        a_start = temp
        temp = b_end
        b_end = a_end
        a_end = temp
    s = word[:a_start] + b + word[a_end+1:b_start] + a + word[b_end+1:]
    return s

print(swap_str_section("hello","el","ll"))