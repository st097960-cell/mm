def rod_cut_plan(n, prices):

    dp = [0] * (n + 1)          
    first_cut = [0] * (n + 1)   

    max_len = len(prices)

    for L in range(1, n + 1):
        best_val = float("-inf")
        best_k = 0

        for k in range(1, min(L, max_len) + 1):
            candidate = prices[k - 1] + dp[L - k]
            if candidate > best_val:
                best_val = candidate
                best_k = k
        dp[L] = best_val
        first_cut[L] = best_k

    plan = []
    rem = n
    while rem > 0 and first_cut[rem] > 0:
        k = first_cut[rem]
        plan.append(k)
        rem -= k

    return plan 
#Everything great