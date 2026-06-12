# coderutils

A lightweight Python utility package that provides a simple `reverse()` function for reversing strings and integers.

## Features

- Reverse strings
- Reverse positive integers
- Reverse negative integers while preserving the sign
- Beginner-friendly API
- No external dependencies
- Lightweight and fast

---

## Installation

Install the package using pip:

```bash
pip install coderutils
```

---

## Usage

### Import the function

```python
from coderutils import reverse
```

---

### Reverse a String

```python
from coderutils import reverse

print(reverse("Hello Coder"))
```

Output:

```text
redoC olleH
```

---

### Reverse a Positive Integer

```python
from coderutils import reverse

print(reverse(12345))
```

Output:

```text
54321
```

---

### Reverse a Negative Integer

```python
from coderutils import reverse

print(reverse(-987))
```

Output:

```text
-789
```

---

## Supported Input Types

| Input Type | Example | Output |
|------------|---------|---------|
| String | `"Hello"` | `"olleH"` |
| Positive Integer | `12345` | `54321` |
| Negative Integer | `-987` | `-789` |

---

## Common Error

If you get:

```python
NameError: name 'reverse' is not defined
```

you forgot to import the function.

Use:

```python
from coderutils import reverse
```

before calling `reverse()`.

---

## Example

```python
from coderutils import reverse

print(reverse("Python"))
print(reverse(2025))
print(reverse(-456))
```

Output:

```text
nohtyP
5202
-654
```

---

## Project Links

- GitHub Repository: https://github.com/PrabhakarVishwakarma/coderutils
- PyPI Package: https://pypi.org/project/coderutils/

---

## Author

**Prabhakar Vishwakarma**

---

## License

This project is licensed under the MIT License.