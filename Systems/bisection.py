def bisection(f, a, b, max_iter=100):
    """
    פונקציה זו פותרת משוואה לא לינארית f(x) = 0 באמצעות שיטת החצייה.

    Args:
      f: פונקציה ממשית חד-מימדית.
      a: קצה שמאלי של מרווח החיפוש.
      b: קצה ימני של מרווח החיפוש.
      tol: סובלנות (דיוק) רצוי.
      max_iter: מספר איטרציות מקסימלי.

    Returns:
      קירוב לשורש של f.
    """

    for i in range(max_iter):

        m = (a + b) / 2
        if f(m) == 0:
            return m
        elif f(m) * f(a) < 0:
            b = m
        else:
            a = m

    raise RuntimeError("שיטת החצייה לא התכנסה לאחר {} איטרציות".format(max_iter))


# דוגמה

def f(x):
    return x ** 2 - 2


a = 1
b = 2

root = bisection(f, a, b)

print("קירוב לשורש:", root)
