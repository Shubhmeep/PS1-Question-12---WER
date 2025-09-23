import re

def tokenize(s):
    return re.findall(r"\w+", s.lower())

def wer(ref_str: str, hyp_str: str):
    ref = tokenize(ref_str)
    hyp = tokenize(hyp_str)
    n, m = len(ref), len(hyp)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): dp[i][0] = i   
    for j in range(m+1): dp[0][j] = j   

    for i in range(1, n+1):
        for j in range(1, m+1):
            sub_cost = 0 if ref[i-1] == hyp[j-1] else 1
            dp[i][j] = min(
                dp[i-1][j] + 1,         # deletion
                dp[i][j-1] + 1,         # insertion
                dp[i-1][j-1] + sub_cost # substitution 
            )

    # Backtrack to count S/I/D
    i, j = n, m
    S = I = D = 0
    while i > 0 or j > 0:
        if i>0 and j>0 and dp[i][j] == dp[i-1][j-1] + (ref[i-1] != hyp[j-1]):
            if ref[i-1] != hyp[j-1]:
                S += 1
            i -= 1; j -= 1
        elif i>0 and dp[i][j] == dp[i-1][j] + 1:
            D += 1; i -= 1
        else:
            I += 1; j -= 1

    wer_value = 100 * (S + I + D) / n if n else 0.0
    return wer_value, S, I, D, n

if __name__ == "__main__":
    REF = ("For fall break I want to go hiking by the lake and watch the sunset I also plan to attend the Inter Miami soccer game and I want to watch Messi play")
    HYP = ("For fall break I want to go hiking by the lake and watch the sunset I also plan to attend the ITA Magny soccer game and I want to watch messy play")

    w, S, I, D, N = wer(REF, HYP)
    print(f"REF words: {N}")
    print(f"S={S}, I={I}, D={D}")
    print(f"WER = {w:.2f}%")
