colors = (i + j for j in 'o<.' for i in 'bgrcmyk')
labels = 'one two three four five six seven eight nine ten'.split()
x = linspace(0, 2*pi, 3000)
d = (2+random((2,3000))) * c_[sin(x), cos(x)].T
for i, l, c  in zip(range(10), labels, colors):
    start, stop = i * 300, (i + 1) * 300
    plot(d[0, start:stop], d[1, start:stop], c, label=l)
legend(loc='lower left')
show()
