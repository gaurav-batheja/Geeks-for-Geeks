Geek is a chemical scientist who is performing an experiment to find an antidote to a poison. 
The experiment involves mixing some solutions in a flask. Based on the theoretical research Geek has done,
he came up with an n * 2 array 'mix', where mix[i] = {X, Y} denotes solutions X and Y that needs to be mixed.
Also, from his past experience, it has been known that mixing some solutions leads to an explosion and thereby completely ruining the experiment. 
The explosive solutions are also provided as a m * 2 array 'danger' where danger[i] = {P, Q}
denotes that if somehow solutions P and Q get into the same flask it will result in an explosion.
Help the Geek by returning an array 'answer' of size n, where answer[i] = "Yes" if it is safe to mix solutions in 'mix[i]' or else answer[i] = "No".
Note: Geek should follow the order of mixing of solutions as it is in 'mix' otherwise the antidote will be ineffective.
Also, Geek will not mix the solutions in 'mix[i]' once he gets to know that mixing them will result in an explosion.
Mixing a solution will effect the other solutions which will appear after it. 
def avoidExlosion(self, mix, n, danger, m):
    ds = list(range(n))
    def find(a):
        if ds[a] != a:
            ds[a] = find(ds[a])
        return ds[a]

    res = []
    for x, y in mix:
        x, y = find(x-1), find(y-1)
        for p, q in danger:
            p, q = find(p-1), find(q-1)
            if (x, y) == (p, q) or (x, y) == (q, p):
                res.append('No')
                break
        else:
            res.append('Yes')
            ds[x] = y

    return res
