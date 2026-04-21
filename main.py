import unittest
import os

def run_tests(test_dir):
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    runner = unittest.TextTestRunner()
    runner.run(discover)

def main():
    test_dir = 'tests'
    if os.path.exists(test_dir):
        run_tests(test_dir)
    else:
        print('Test directory not found')

if __name__ == '__main__':
    main()
```

```python
# tests/test_example.py
import unittest

class TestExample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)

    def test_sub(self):
        self.assertEqual(2 - 2, 0)

if __name__ == '__main__':
    unittest.main()
```

```bash
# tests
test_example.py
```

```bash
# main.py
python main.py
```

```bash
# output
.....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
