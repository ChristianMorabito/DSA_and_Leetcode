def lcs_rec(str1, str2, i=0, j=0, cache=None) -> int:

    if cache is None:
        cache = {}

    key = str(i) + " " + str(j)
    if key in cache:
        return cache[key]

    if i == len(str1) or j == len(str2):
        return 0

    if str1[i] == str2[j]:
        return 1 + lcs_rec(str1, str2, i+1, j+1, cache)

    result = max(lcs_rec(str1, str2, i, j+1, cache), lcs_rec(str1, str2, i+1, j, cache))
    cache[key] = result
    return cache[key]


print(lcs_rec('BAC', 'BDADC'))
# Refer to Longest_Common_Subsequence_Memoized.png
# for visualization of this recursive call
