
def regula_falsi(f, a, b, ε):
  """
  מחשב את שורש הפונקציה f בתחום [a, b] באמצעות שיטת רגולה פולסי.

  Args:
      f: פונקציה רציפה
      a: קצה שמאלי של תחום החיפוש
      b: קצה ימני של תחום החיפוש
      ε: דיוק רצוי

  Returns:
      הערכה לשורש הפונקציה
  """

  while abs(b - a) > ε:
    m = (a * f(b) - b * f(a)) / (f(b) - f(a))
    if f(m) == 0:
      return m
    elif f(m) * f(a) < 0:
      b = m
    else:
      a = m
  return (a + b) / 2

# דוגמה לשימוש
def f(x):
  return x**2 - 2

a = 0
b = 2
ε = 0.01

root = regula_falsi(f, a, b, ε)

print(f"הערכה לשורש: {root}")