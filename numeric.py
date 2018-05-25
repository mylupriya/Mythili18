s = "abc.123"
print len([c for c in s if c.isdigit()])
print [c.isdigit() for c in s].count(True)
print sum(c.isdigit() for c in s)
