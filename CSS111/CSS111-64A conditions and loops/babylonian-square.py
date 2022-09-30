number = 2500

g = number / 4.0
g = 100
g2 = g + 1;
while(g != g2):
    n = number / g;
    g2 = g;
    g = (g + n) / 2;
    print(g)
