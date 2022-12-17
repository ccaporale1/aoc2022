def compare(left, right):
    for l,r in zip(left.split(","), right.split(",")):
        dl, dr = l.count("[") - l.count("]"), r.count("[") - r.count("]")
        l,r = l.strip("[]").strip('\n').strip(']'), r.strip("[]").strip('\n').strip(']')
        if l != r:
            if l and r:
                return int(l) - int(r)
            return bool(l) - bool(r)
        if dl != dr:
            return dl - dr
    return len(left) - len(right)

with open('./inputs/day13_input.txt') as f:
    swapped, index2, index6 = 0, 1, 2
    for i,(left,right,_) in enumerate(zip(f,f,f)):
        swapped += (compare(left, right) < 0) * (i+1)
        index2 += (compare("2", left) > 0) + (compare("2", right) > 0)
        index6 += (compare("6", left) > 0) + (compare("6", right) > 0)
    print(swapped, index2 * index6)