def is_valid(s, rules, terminal, visited, target):
    if len(target) < len(s):
        return False

    if s == target:
        return True

    for i in range(0, len(s)):
        if s[i] in terminal or not s[i] in rules:
            continue

        for r in rules[s[i]]:
            ns = s[0:i] + r + s[i + 1:]
            if ns in visited:
                continue

            visited.add(ns)
            if is_valid(ns, rules, terminal, visited, target):
                return True

    return False


d = dict([("S", "E"), ("E", ["(EE)", "i"])])
print(is_valid("S", d, ["i"], set(), "((ii)i)"))
