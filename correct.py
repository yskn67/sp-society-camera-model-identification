#! /usr/bin/env python

from collections import defaultdict
from sklearn.externals import joblib
FILES = [
    "add some submissions",
]

data = defaultdict(set)
for fname in FILES:
    with open(fname, "rt") as f:
        header = f.readline()
        for line in f:
            d = line.strip().split(",")
            data[d[0]].add(d[1])

cnt = defaultdict(int)
res = {}
for k, v in data.items():
    if len(v) == 1:
        model = list(v)[0]
        cnt[model] += 1
        res[k] = model
        #print(k, list(v)[0])
joblib.dump(res, "test_correct.pkl")

all_v = sum(cnt.values())
for k, v in cnt.items():
    print(k, v, v / all_v)
