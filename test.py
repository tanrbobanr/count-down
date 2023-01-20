from src import countdown


c = countdown.Countdown(
    "T{z}{wL.w}{p.w}{wR.w}{w}{wL}{p}{wR}{d}{dL}{P}{dR}{h}{hL}{ep}{hR}{M}{ML}{eP}{MR}{s}{sL}{Ep}{sR}{m}{mL}{EP}{mR}{u}",
    wL="w[",
    wR="] ",
    dL="d[",
    dR="] ",
    hL="h[",
    hR="] ",
    ML="m[",
    MR="] ",
    sL="s[",
    sR="] ",
    mL="ms[",
    mR="] "
)
kwargs = {
    "z": "+",
    "w": 204128,
    "_w__wR": "] ",
    "_w__wL": "w[",
    "_w__p": "s",
    "d": 2,
    "_d__dR": "] ",
    "_d__dL": "d[",
    "_d__P": "S",
    "h": 1,
    "_h__hR": "] ",
    "_h__hL": "h[",
    "_h__ep": "",
    "M": 22,
    "_M__MR": "] ",
    "_M__ML": "m[",
    "_M__eP": "eS",
    "s": 3,
    "_s__sR": "] ",
    "_s__sL": "s[",
    "_s__Ep": "Es",
    "m": 456,
    "_m__mR": "] ",
    "_m__mL": "ms[",
    "_m__EP": "ES",
    "u": 789
}
kwargs2 = {
    "z": "+",
    "w": 204128,
    "_w__wR": "] ",
    "_w__wL": "w[",
    "_w__p": "s",
    "d": 2,
    "_d__dR": "] ",
    "_d__dL": "d[",
    "_d__P": "S",
    "h": 1,
    "_h__hR": "] ",
    "_h__hL": "h[",
    "_h__ep": "",
    "M": 22,
    "_M__MR": "] ",
    "_M__ML": "m[",
    "_M__eP": "eS",
    "s": 3,
    "_s__sR": "] ",
    "_s__sL": "s[",
    "_s__Ep": "Es",
    "m": 456,
    "_m__mR": "] ",
    "_m__mL": "ms[",
    "_m__EP": "ES",
    "u": 789
}

k = {
    "_w__wL": 1,
    "w": 2
}

print("T{z}{_w__wL}{_w__p}{_w__wR}{w}{_w__wL}{_w__p}{_w__wR}".format(**kwargs))
# print("T{z}{_w__wL}{_w__p}{_w__wR}{w}{_w__wL}{_w__p}{_w__wR}{d}{_d__dL}{_d__P}{_d__dR}{h}{_h__hL}{_h__ep}{_h__hR}{M}{_M__ML}{_M__eP}{_M__MR}{s}{_s__sL}{_s__Ep}{_s__sR}{m}{_m__mL}{_m__EP}{_m__mR}{u}".format(_w__wL="w["))
# print(c.fmt)
# print(c.orig_fmt)
# print(c.fmt)
# print(c.format(123456792123456789))
# assert c.format(123456792123456789) == "T+[s]204128w[s] 2d[S] 1h[] 22m[eS] 3s[Es] 456ms[ES] 789"