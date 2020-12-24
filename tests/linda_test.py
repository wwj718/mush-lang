from __future__ import print_function, division
import uuid

test_uuid = "abc" + uuid.uuid4().hex[:8]

linda_tests = [
    (f"(linda-out '({test_uuid} 2))", [test_uuid,2]),
    (f"(linda-rd '({test_uuid} *))", [test_uuid,2]),
    (f"(linda-rdp '({test_uuid} *))", [test_uuid,2]),
    (f"(linda-in '({test_uuid} *))", [test_uuid,2]),
    (f"(linda-inp '({test_uuid} *))", []),
    (f"(linda-out '({test_uuid} 2))", [test_uuid,2]),
    (f"(linda-inp '({test_uuid} *))", [test_uuid,2]),
]

def test(tests, name=''):
    "For each (exp, expected) test case, see if eval(parse(exp)) == expected."
    fails = 0
    for (x, expected) in tests:
        try:
            result = eval(parse(x))
            print(x, '=>', to_string(result))
            ok = (result == expected)
        except Exception as e:
            print(x, '=raises=>', type(e).__name__, e)
            ok = issubclass(expected, Exception) and isinstance(e, expected)
        if not ok:
            fails += 1
            print('FAIL!!!  Expected', expected)
    print('%s %s: %d out of %d tests fail.' % ('*'*45, name, fails, len(tests)))


if __name__ == '__main__':
    from mush_lang.mush_lang import *
    test(linda_tests, 'mush_lang.py')