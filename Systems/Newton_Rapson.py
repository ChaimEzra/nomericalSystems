


def newton_raphson(f, fprime, x0, ε=1e-5, max_iter=100):
    """
    פונקציה זו פותרת משוואה לא לינארית f(x) = 0 באמצעות שיטת ניוטון-רפסון.

    Args:
      f: פונקציה ממשית חד-מימדית.
      fprime: נגזרת הפונקציה f.
      x0: ניחוש ראשוני עבור השורש.
      tol: סובלנות (דיוק) רצוי.
      max_iter: מספר איטרציות מקסימלי.

    Returns:
      קירוב לשורש של f.
    """

    for i in range(max_iter):
        x1 = x0 - f(x0) / fprime(x0)
        if abs(x1 - x0) < ε:
            return x1
        x0 = x1

    raise RuntimeError("שיטת ניוטון-רפסון לא התכנסה לאחר {} איטרציות".format(max_iter))


# דוגמה

def f(x):
    return x ** 2 - 2


def fprime(x):
    return 2 * x


x0 = 1

root = newton_raphson(f, fprime, x0)

print("קירוב לשורש:", root)