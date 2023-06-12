import time

# Without memoization, time complexity is O(n^n) & space complexity is O(n) due to rec stack. With this input, it takes
# 5 seconds on average to run.
# With memoization, time complexity is O(n^2) due to worst case scenario. Space complexity is O(n) due to cache.
# With this input & memo, it takes 0 seconds on average to run.


def word_break(string: str, w_set: set[str], cache=None, start=0) -> bool:

    # BASE CASE
    if start == len(string):
        return True

    if cache is None:
        cache = {}

    if start in cache:
        return cache[start]

    for end in range(start + 1, len(string) + 1):
        selected = string[start:end]
        if selected in w_set and word_break(string, w_set, cache, end):
            cache[start] = True
            return True

    cache[start] = False
    return False


st = time.time()
print(word_break(   'abcdefghijklmnopqrstuvwxyz', {'a', 'b', 'c', 'd', 'e,' 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                    'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqr', 'abcdefghijklmnopq', 'abcdefghijklmnop', 'abcdefghijklmno', 'abcdefghijklmn', 'abcdefghijklm', 'abcdefghijkl', 'abcdefghijk', 'abcdefghij', 'abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab'
                    'bcdefghijklmnopqrstuvwxy', 'bcdefghijklmnopqrstuvwx', 'bcdefghijklmnopqrstuvw', 'bcdefghijklmnopqrstuv', 'bcdefghijklmnopqrstu', 'bcdefghijklmnopqrst', 'bcdefghijklmnopqrs', 'bcdefghijklmnopqr', 'bcdefghijklmnopq', 'bcdefghijklmnop', 'bcdefghijklmno', 'bcdefghijklmn', 'bcdefghijklm', 'bcdefghijkl', 'bcdefghijk', 'bcdefghij', 'bcdefghi', 'bcdefgh', 'bcdefg', 'bcdef', 'bcde', 'bcd', 'bc',
                    'cdefghijklmnopqrstuvwxy', 'cdefghijklmnopqrstuvwx', 'cdefghijklmnopqrstuvw', 'cdefghijklmnopqrstuv', 'cdefghijklmnopqrstu', 'cdefghijklmnopqrst', 'cdefghijklmnopqrs', 'cdefghijklmnopqr', 'cdefghijklmnopq', 'cdefghijklmnop', 'cdefghijklmno', 'cdefghijklmn', 'cdefghijklm', 'cdefghijkl', 'cdefghijk', 'cdefghij', 'cdefghi', 'cdefgh', 'cdefg', 'cdef', 'cde', 'cd',
                    'defghijklmnopqrstuvwxy', 'defghijklmnopqrstuvwx', 'defghijklmnopqrstuvw', 'defghijklmnopqrstuv', 'defghijklmnopqrstu', 'defghijklmnopqrst', 'defghijklmnopqrs', 'defghijklmnopqr', 'defghijklmnopq', 'defghijklmnop', 'defghijklmno', 'defghijklmn', 'defghijklm', 'defghijkl', 'defghijk', 'defghij', 'defghi', 'defgh', 'defg', 'def', 'de',
                    'efghijklmnopqrstuvwxy', 'efghijklmnopqrstuvwx', 'efghijklmnopqrstuvw', 'efghijklmnopqrstuv', 'efghijklmnopqrstu', 'efghijklmnopqrst', 'efghijklmnopqrs', 'efghijklmnopqr', 'efghijklmnopq', 'efghijklmnop', 'efghijklmno', 'efghijklmn', 'efghijklm', 'efghijkl', 'efghijk', 'efghij', 'efghi', 'efgh', 'efg', 'ef',
                    'fghijklmnopqrstuvwxy', 'fghijklmnopqrstuvwx', 'fghijklmnopqrstuvw', 'fghijklmnopqrstuv', 'fghijklmnopqrstu', 'fghijklmnopqrst', 'fghijklmnopqrs', 'fghijklmnopqr', 'fghijklmnopq', 'fghijklmnop', 'fghijklmno', 'fghijklmn', 'fghijklm', 'fghijkl', 'fghijk', 'fghij', 'fghi', 'fgh', 'fg',
                    'ghijklmnopqrstuvwxy', 'ghijklmnopqrstuvwx', 'ghijklmnopqrstuvw', 'ghijklmnopqrstuv', 'ghijklmnopqrstu', 'ghijklmnopqrst', 'ghijklmnopqrs', 'ghijklmnopqr', 'ghijklmnopq', 'ghijklmnop', 'ghijklmno', 'ghijklmn', 'ghijklm', 'ghijkl', 'ghijk', 'ghij', 'ghi', 'gh',
                    'hijklmnopqrstuvwxy', 'hijklmnopqrstuvwx', 'hijklmnopqrstuvw', 'hijklmnopqrstuv', 'hijklmnopqrstu', 'hijklmnopqrst', 'hijklmnopqrs', 'hijklmnopqr', 'hijklmnopq', 'hijklmnop', 'hijklmno', 'hijklmn', 'hijklm', 'hijkl', 'hijk', 'hij', 'hi',
                    'ijklmnopqrstuvwxy', 'ijklmnopqrstuvwx', 'ijklmnopqrstuvw', 'ijklmnopqrstuv', 'ijklmnopqrstu', 'jklmnopqrst', 'ijklmnopqrs', 'ijklmnopqr', 'ijklmnopq', 'ijklmnop', 'ijklmno', 'ijklmn', 'ijklm', 'ijkl', 'ijk', 'ij',
                    'jklmnopqrstuvwxy', 'jklmnopqrstuvwx', 'jklmnopqrstuvw', 'jklmnopqrstuv', 'jklmnopqrstu', 'jklmnopqrst', 'jklmnopqrs', 'jklmnopqr', 'jklmnopq', 'jklmnop', 'jklmno', 'jklmn', 'jklm', 'jkl', 'jk',
                    'jklmnopqrstuvwx', 'jklmnopqrstuvw', 'jklmnopqrstuv', 'jklmnopqrstu', 'jklmnopqrst', 'jklmnopqrs', 'jklmnopqr', 'jklmnopq', 'jklmnop', 'jklmno', 'jklmn', 'jklm', 'jkl', 'jk',
                    'klmnopqrstuvwx', 'klmnopqrstuvw', 'klmnopqrstuv', 'klmnopqrstu', 'klmnopqrst', 'klmnopqrs', 'klmnopqr', 'klmnopq', 'klmnop', 'klmno', 'klmn', 'klm', 'kl',
                    'lmnopqrstuvwx', 'lmnopqrstuvw', 'lmnopqrstuv', 'lmnopqrstu', 'lmnopqrst', 'lmnopqrs', 'lmnopqr', 'lmnopq', 'lmnop', 'lmno', 'lmn', 'lm',
                    'mnopqrstuvwx', 'mnopqrstuvw', 'mnopqrstuv', 'mnopqrstu', 'mnopqrst', 'mnopqrs', 'mnopqr', 'mnopq', 'mnop', 'mno', 'mn',
                    'nopqrstuvwx', 'nopqrstuvw', 'nopqrstuv', 'nopqrstu', 'nopqrst', 'nopqrs', 'nopqr', 'nopq', 'nop', 'no',
                    'opqrstuvwx', 'opqrstuvw', 'opqrstuv', 'opqrstu', 'opqrst', 'opqrs', 'opqr', 'opq', 'op',
                    'pqrstuvwx', 'pqrstuvw', 'pqrstuv', 'pqrstu', 'pqrst', 'pqrs', 'pqr', 'pq',
                    'qrstuvwx', 'qrstuvw', 'qrstuv', 'qrstu', 'qrst', 'qrs', 'qr',
                    'rstuvwx', 'rstuvw', 'rstuv', 'rstu', 'rst', 'rs',
                    'stuvwx', 'stuvw', 'stuv', 'stu', 'st',
                    'tuvwx', 'tuvw', 'tuv', 'tu',
                    'uvwx', 'uvw', 'uv',
                    'vwx', 'vw'}))
en = time.time()
elap = en - st
print(elap)