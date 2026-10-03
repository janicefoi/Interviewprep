#!/bin/python3
# =====================================================================
#  MOCK TEST 1  -  60 minutes  -  2 questions  -  Python 3, no imports
#  1. Start a 60-minute timer.
#  2. Write your code inside the two functions below (delete "pass").
#  3. Run this file. It grades you like HackerRank's Submit button.
# =====================================================================


# ---------------------------------------------------------------------
#  QUESTION 1: Alert Deduplication
# ---------------------------------------------------------------------
#  A monitoring system receives alerts as [timestamp, service] pairs,
#  in no particular order. To reduce noise, alerts are processed in
#  timestamp order. For each service, an alert is KEPT if it is the
#  first alert for that service, or if its timestamp is MORE THAN k
#  seconds after the last KEPT alert for that same service. Otherwise
#  it is suppressed.
#
#  Return the number of kept alerts.
#
#  Function Description
#    suppressAlerts has the following parameters:
#      alerts[n][2]: each alert is [timestamp (int), service (str)]
#      k (int): the suppression window in seconds
#    Returns
#      int: the number of kept alerts
#
#  Example
#    k = 10
#    alerts = [[5,"db"], [12,"db"], [16,"db"], [3,"api"], [14,"api"], [20,"db"]]
#    In time order:
#      3  api -> kept       (first api)
#      5  db  -> kept       (first db)
#      12 db  -> suppressed (12 - 5 = 7 <= 10)
#      14 api -> kept       (14 - 3 = 11 > 10)
#      16 db  -> kept       (16 - 5 = 11 > 10)
#      20 db  -> suppressed (20 - 16 = 4 <= 10)
#    Return 4.
#
#  Constraints
#    1 <= n <= 10^5
#    0 <= timestamp <= 10^9,  0 <= k <= 10^9
#    service names are lowercase strings
# ---------------------------------------------------------------------

def suppressAlerts(alerts, k):
    # Write your code here
    ordered = sorted(alerts)
    last_kept = {}
    kept = 0

    for timestamp, service in ordered:
        if service not in last_kept or timestamp - last_kept[service] > k:
            kept += 1
            last_kept[service] = timestamp
    return kept
    


# ---------------------------------------------------------------------
#  QUESTION 2: Shortest Error Burst
# ---------------------------------------------------------------------
#  errors[i] is the number of errors logged in minute i (all values
#  are positive). Find the length of the SHORTEST contiguous stretch
#  of minutes whose total number of errors is AT LEAST threshold.
#  If no such stretch exists, return 0.
#
#  Function Description
#    shortestBurst has the following parameters:
#      errors[n] (int): errors per minute
#      threshold (int): the minimum total to count as a burst
#    Returns
#      int: the length of the shortest burst, or 0
#
#  Example
#    errors = [2, 3, 1, 2, 4, 3], threshold = 7
#    [4, 3] sums to 7 and has length 2. No single minute reaches 7.
#    Return 2.
#
#  Constraints
#    1 <= n <= 10^5
#    1 <= errors[i] <= 10^4
#    1 <= threshold <= 10^9
# ---------------------------------------------------------------------

def shortestBurst(errors, threshold):
    # Write your code here
    left = 0
    total = 0
    best = len(errors) + 1

    for right in range(len(errors)):
        total += errors[right]
        
        while total >= threshold:
            best = min(best, right - left + 1)
            total -= errors[left]
            left += 1
    
    return 0 if best == len(errors) + 1 else best


# ---------------------------------------------------------------------
#  SCRATCH AREA ("Test against custom input"): try your own inputs.
#  Uncomment a line to print your function's result.
# ---------------------------------------------------------------------
# print(suppressAlerts([[5,"db"], [12,"db"], [3,"api"]], 10))
# print(shortestBurst([2, 3, 1, 2, 4, 3], 7))


# =====================================================================
#  DO NOT EDIT BELOW THIS LINE: this is the grader (like HackerRank's
#  "Submit"). Your solutions above must not use imports.
# =====================================================================
import copy, threading, time, os

TIME_LIMIT = 3.0   # seconds per test case

def _rng(seed):
    s = seed
    def nxt(a, b):
        nonlocal s
        s = (s * 1103515245 + 12345) % 2147483648
        return a + s % (b - a + 1)
    return nxt

def _cs(lst):
    total = 0
    for i, v in enumerate(lst):
        total = (total + (i + 1) * (v + 7)) % 1000000007
    return total

def build_q1():
    cases = [
        ([[[5,"db"],[12,"db"],[16,"db"],[3,"api"],[14,"api"],[20,"db"]], 10], True),
        ([[[1,"a"]], 5], True),
        ([[[4,"x"],[4,"x"],[9,"x"],[10,"x"]], 5], False),
        ([[[0,"a"],[0,"b"],[0,"c"]], 0], False),
        ([[[10,"a"],[0,"a"],[5,"a"]], 4], False),
        ([[[7,"web"],[7,"web"],[7,"web"]], 0], False),
        ([[[100,"a"],[50,"b"],[0,"a"],[60,"b"],[101,"a"]], 100], False),
        ([[[0,"a"],[1,"a"],[2,"a"],[3,"a"]], 1], False),
    ]
    for seed, n, svc, tmax, k in [(1,30,3,60,7),(2,200,5,1000,40),(3,500,26,5000,0),(4,1000,4,100,1000000000)]:
        r = _rng(seed)
        cases.append(([[[r(0,tmax), "s"+str(r(1,svc))] for _ in range(n)], k], False))
    cases.append(([[[i,"svc"] for i in range(100000)], 0], False))
    r = _rng(9)
    cases.append(([[[r(0,10**9), "s"+str(r(1,50))] for _ in range(100000)], 5000000], False))
    r = _rng(10)
    cases.append(([[[100000-i, "s"+str(i%3)] for i in range(100000)], 2], False))
    return cases

def build_q2():
    cases = [
        ([[2,3,1,2,4,3], 7], True),
        ([[1,1,1], 10], True),
        ([[10], 10], False),
        ([[1,4,4], 4], False),
        ([[1,2,3,4,5], 11], False),
        ([[1,2,3,4,5], 15], False),
        ([[5,1,3,5,10,7,4,9,2,8], 15], False),
    ]
    for seed, n, vmax, T in [(11,20,10,30),(12,300,50,1000),(13,1000,3,2500),(14,2000,100,10**9)]:
        r = _rng(seed)
        cases.append(([[r(1,vmax) for _ in range(n)], T], False))
    cases.append(([[1]*100000, 100000], False))
    r = _rng(15)
    cases.append(([[r(1,10000) for _ in range(100000)], 2000000], False))
    cases.append(([[1]*99999 + [10000], 10000], False))
    cases.append(([[10000]*100000, 10**9], False))
    return cases

def build_q3():
    cases = [
        ([[73,74,75,71,69,72,76,73]], True),
        ([[5]], True),
        ([[3,3,3]], False),
        ([[5,4,3,2,1]], False),
        ([[1,2,3]], False),
        ([[2,1,2,1,3]], False),
        ([[1,3,2,4,1,5]], False),
    ]
    for seed, n, vmax in [(21,15,10),(22,200,5),(23,1000,1000)]:
        r = _rng(seed)
        cases.append(([[r(1,vmax) for _ in range(n)]], False))
    cases.append(([list(range(100000, 0, -1))], False))
    cases.append(([list(range(1, 100001))], False))
    r = _rng(24)
    cases.append(([[r(1,10**9) for _ in range(100000)]], False))
    cases.append(([[1]*50000 + [2]*50000], False))
    cases.append(([[100000 - (i % 1000) for i in range(100000)]], False))
    return cases

def build_q4():
    cases = [
        ([[3,-1,-2,4,-4], 0], True),
        ([[1,1,1], 2], True),
        ([[0,0,0], 0], False),
        ([[5], 3], False),
        ([[1,-1,1,-1], 0], False),
        ([[-2,-3,5,1,-1], -5], False),
        ([[10,2,-2,-20,10], -10], False),
    ]
    for seed, n, lo, hi, t in [(31,20,-3,3,0),(32,300,-10,10,5),(33,1000,-1,1,0),(34,2000,-10000,10000,7)]:
        r = _rng(seed)
        cases.append(([[r(lo,hi) for _ in range(n)], t], False))
    cases.append(([[0]*100000, 0], False))
    r = _rng(35)
    cases.append(([[r(-5,5) for _ in range(100000)], 3], False))
    cases.append(([[1]*100000, 50000], False))
    cases.append(([[10000]*100000, -1], False))
    return cases


def _run_case(fn, args):
    box = {}
    def target():
        try:
            t0 = time.time()
            box["out"] = fn(*args)
            box["t"] = time.time() - t0
        except Exception as e:
            box["err"] = type(e).__name__ + ": " + str(e)
    th = threading.Thread(target=target, daemon=True)
    th.start()
    th.join(TIME_LIMIT)
    if th.is_alive():
        return "timeout", None, None
    if "err" in box:
        return "error", box["err"], None
    return "ok", box["out"], box["t"]

def _grade(num, title, fn, cases, expected, is_list):
    print("\n" + "=" * 62)
    print("Question %d: %s" % (num, title))
    print("=" * 62)
    passed = 0
    timed_out = False
    for i, ((args, sample), exp) in enumerate(zip(cases, expected)):
        label = ("Sample Test Case %d" % i) if sample else ("Test Case %d" % i)
        if timed_out:
            print("  %-22s NOT RUN (an earlier case timed out)" % label)
            continue
        status, out, t = _run_case(fn, copy.deepcopy(args))
        if status == "timeout":
            timed_out = True
            print("  %-22s FAIL  Terminated due to timeout (> %.0fs)" % (label, TIME_LIMIT))
            continue
        if status == "error":
            print("  %-22s FAIL  Runtime Error -> %s" % (label, out))
            continue
        got = _cs(out) if (is_list and isinstance(out, list)) else out
        if got == exp:
            passed += 1
            print("  %-22s PASS  (%.2fs)" % (label, t))
        else:
            print("  %-22s FAIL  Wrong Answer" % label)
            if sample:
                print("      input:    %r" % (args,))
                print("      expected: %r" % (_SAMPLE_EXPECTED[num][i],))
                print("      your out: %r" % (out,))
    print("  " + "-" * 40)
    print("  Result: %d/%d test cases passed" % (passed, len(cases)))
    return passed, len(cases)

_SAMPLE_EXPECTED = {1: {0: 4, 1: 1}, 2: {0: 2, 1: 0}}

if __name__ == '__main__':
    total_p = total_n = 0
    p, n = _grade(1, 'Alert Deduplication', suppressAlerts, build_q1(), [4, 1, 2, 3, 3, 1, 3, 2, 15, 81, 495, 2, 100000, 4771, 100000], False)
    total_p += p; total_n += n
    p, n = _grade(2, 'Shortest Error Burst', shortestBurst, build_q2(), [2, 0, 1, 1, 3, 5, 2, 5, 35, 0, 0, 100000, 364, 1, 100000], False)
    total_p += p; total_n += n
    print("\n" + "=" * 62)
    print("TOTAL: %d/%d test cases passed" % (total_p, total_n))
    print("=" * 62)
    os._exit(0)