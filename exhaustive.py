#!/usr/bin/env python3

# "Universally recognized" clusters from John Algeo (1978) What Consonant
# Clusters Are Possible, Word, 29:3, 206-224,
# DOI: 10.1080/00437956.1978.11435661
ONSET_CLUSTERS = ["bl", "br", "dr", "dw", "fl", "fr", "gl", "gr", "kl", "kr",
                  "kw", "pl", "pr", "sk", "skr", "skw", "sl", "sm", "sn", "sp",
                  "spl", "spr", "st", "str", "sw", "shr", "tr", "sw", "thr",
                  "thw",]
CODA_CLUSTERS = ["dz", "ft", "ks", "lb", "lch", "ld", "lf", "lk", "lp", "lt",
                 "nch", "nd", "nt", "nz", "ps", "pt", "sk", "sp", "st", "kt",
                 "lm", "lv", "mp", "nj", "nk", ]

# Extras from the same paper
ONSET_CLUSTERS += ["bw", "dy", "fy", "gw", "gy", "ky", "mw", "my", "nw", "ny",
                   "pf", "py", "sf", "shl", "shm", "shn", "shp", "sht", "shw",
                   "skl", "sky", "smy", "spy", "sw", "vl", "vr", "vy", "zh", ]

CODA_CLUSTERS += ["rb", "rch", "rd", "rf", "rg", "rj", "rk", "rl", "rm", "rn",
                  "rp", "rs", "rsh", "rsht", "rt", "rth", "rv", "nsk", "nf",
                  "nsh", "pf", "rnst", "rpst", "rzh", "rsk", ]

ONSET_SINGLETONS = ["b", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r",
                    "s", "t", "v", "w", "y", "z",]
CODA_SINGLETONS = ["b", "d", "f", "g", "j", "k", "l", "m", "n", "p", "r", "s",
                   "t", "v", "z",]

# Incomplete
VOWELS = ["a", "e", "i", "o", "u", "ay", "ee", "eye", "oh", "oo", "oi",]

FRONT = ONSET_SINGLETONS + ONSET_CLUSTERS
BACK = CODA_SINGLETONS + CODA_CLUSTERS

print(len(FRONT) * len(VOWELS) * len(BACK))
