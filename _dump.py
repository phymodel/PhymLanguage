import io, sys

files = sys.argv[1:]
for p in files:
    lines = io.open(p, encoding="utf-8").read().split("\n")
    print("#### %s (%d lines)" % (p, len(lines)))
    infence = False
    hidden = 0
    fstart = 0
    skip = False
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if s.startswith("```"):
            if not infence:
                infence = True
                hidden = 0
                fstart = i
                skip = (s == "```phymodel" or s.startswith("```"))
            else:
                infence = False
                if fstart:
                    print("%3d|   <fenced block %d..%d, %d lines>" % (fstart, fstart, i, i - fstart + 1))
                fstart = 0
            continue
        if infence:
            continue
        print("%3d|%s" % (i, l))
    print()
