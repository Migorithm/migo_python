from collections import defaultdict

dd = defaultdict(list)

dd["dogs"].append("Kathrin")
dd["dogs"].append("Mr Sniffles")

print(dd)

ii = defaultdict(int)
ii["a"] += 1
ii["A"] +=5
ii["a"] +=5

print(ii)