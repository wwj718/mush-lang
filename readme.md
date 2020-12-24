# readme

> LISP 是一种构建材料 -- Alan Kay

为了更好地探索 Linda 的可能性，我们围绕 Linda 的基本原语，构建了一门简单的语言 -- mush-lang。

mush-lang 采用 LISP 风格的语法，可以视为 LISP 的一门玩具方言。 LISP 因其同构性(内外表示一致)，可能是所有语言中最简单的。 这对于探索新想法非常方便。

mush-lang 目前在 Python 中实现。

我们未来也打算基于这个它探索类似 Erlang 的语言（[Linda: 比 Actor 更好的并发模型](http://wwj718.github.io/post/编程/linda-intro/)）

# usage
`pip install mush_lang`

如果要使用 linda 原语，确保已经运行 [CodeLab Adapter](http://adapter.codelab.club/) (Linda服务运行在 CodeLab Adapter)

## REPL
```bash
# ctrl-D 退出
mush-lang
```

## 运行脚本
```bash
mush-lang examples/factorial.mu
```

## 开发环境(dev)

### 安装依赖

推荐在 Python 虚拟环境中做实验

```bash
pip install -r requirements.txt
python setup.py install
```

### 测试
```bash
python tests/lispytest.py
python tests/linda_test.py
```

# 参考
*  [mal](https://github.com/kanaka/mal/blob/master/process/guide.md)
    *  [Python.2 (3.X)](https://github.com/kanaka/mal#python2-3x)
        *  [Arpeggio](https://github.com/textX/Arpeggio)
    *  [Python (2.X and 3.X)](https://github.com/kanaka/mal#python-2x-and-3x)
    *  [RPython](https://github.com/kanaka/mal#rpython)
*  [(How to Write a (Lisp) Interpreter (in Python))](http://norvig.com/lispy.html)
*  [(An ((Even Better) Lisp) Interpreter (in Python))](http://norvig.com/lispy2.html)
*  [lithp](https://github.com/fogus/lithp): McCarthy Lisp interpreter