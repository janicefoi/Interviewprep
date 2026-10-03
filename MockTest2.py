#!/bin/python3
# =====================================================================
#  MOCK TEST 2  -  60 minutes  -  2 questions  -  Python 3, no imports
#  1. Start a 60-minute timer.
#  2. Write your code inside the two functions below (delete "pass").
#  3. Run this file. It grades you like HackerRank's Submit button.
# =====================================================================


# ---------------------------------------------------------------------
#  QUESTION 1: Wait for Higher Latency
# ---------------------------------------------------------------------
#  latency[i] is the response time of request i. For each request,
#  find how many requests later the first request with a STRICTLY
#  HIGHER latency arrives. If there is none, use 0.
#
#  Return a list of the same length as latency.
#
#  Function Description
#    waitForHigher has the following parameter:
#      latency[n] (int): response times in arrival order
#    Returns
#      int[n]: for each request, the distance to the next higher one
#
#  Example
#    latency = [73, 74, 75, 71, 69, 72, 76, 73]
#    For 75 (index 2), the next higher value is 76 (index 6): 6 - 2 = 4.
#    For 76 and the last 73, nothing higher comes later: 0.
#    Return [1, 1, 4, 2, 1, 1, 0, 0].
#
#  Constraints
#    1 <= n <= 10^5
#    1 <= latency[i] <= 10^9
# ---------------------------------------------------------------------

def waitForHigher(latency):
    # Write your code here
    pass


# ---------------------------------------------------------------------
#  QUESTION 2: Memory Drift Windows
# ---------------------------------------------------------------------
#  deltas[i] is the change in a service's memory usage during minute i.
#  Values can be positive, negative, or zero. Count how many CONTIGUOUS
#  windows of minutes have a total change EXACTLY equal to target.
#
#  Function Description
#    countDriftWindows has the following parameters:
#      deltas[n] (int): memory change per minute
#      target (int): the total change to look for
#    Returns
#      int: the number of windows whose sum equals target
#
#  Example
#    deltas = [3, -1, -2, 4, -4], target = 0
#    Windows summing to 0: [3, -1, -2], [4, -4], [3, -1, -2, 4, -4]
#    Return 3.
#
#  Constraints
#    1 <= n <= 10^5
#    -10^4 <= deltas[i] <= 10^4
#    -10^9 <= target <= 10^9
# ---------------------------------------------------------------------

def countDriftWindows(deltas, target):
    # Write your code here
    pass


# ---------------------------------------------------------------------
#  SCRATCH AREA ("Test against custom input"): try your own inputs.
#  Uncomment a line to print your function's result.
# ---------------------------------------------------------------------
# print(waitForHigher([73, 74, 75, 71, 69, 72, 76, 73]))
# print(countDriftWindows([3, -1, -2, 4, -4], 0))


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

_SAMPLE_EXPECTED = {1: {0: [1, 1, 4, 2, 1, 1, 0, 0], 1: [0]}, 2: {0: 3, 1: 2}}

if __name__ == '__main__':
    total_p = total_n = 0
    p, n = _grade(1, 'Wait for Higher Latency', waitForHigher, build_q3(), [286, 7, 42, 105, 45, 121, 168, 920, 172987, 5955598, 349755, 299720, 930494644, 583553917, 624266682], True)
    total_p += p; total_n += n
    p, n = _grade(2, 'Memory Drift Windows', countDriftWindows, build_q4(), [3, 2, 6, 0, 4, 1, 3, 13, 684, 20582, 12, 5000050000, 6678829, 50001, 0], False)
    total_p += p; total_n += n
    print("\n" + "=" * 62)
    print("TOTAL: %d/%d test cases passed" % (total_p, total_n))
    print("=" * 62)
    os._exit(0)