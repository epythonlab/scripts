## Avoiding Over-Optimization

---

### 

```
# Clear and Maintainable Code
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
```

---

###

```
# Premature Optimization (Less Clear)
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n in (0, 1):
        return 1
    else:
        return n * factorial(n - 1)
```

---

### Subscribe, Like, share, and comment
### Thanks for watching
---