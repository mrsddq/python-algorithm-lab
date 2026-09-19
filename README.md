# Python Algorithm Lab

Extensive Python and data structures/algorithms learning repository.

This repo has two jobs:

- preserve the original course/practice archive under `ITP/`, `DSA/`, and `revision/`
- provide a clean, tested reference layer under `src/dsa/` for optimized implementations

## Structure

```text
DSA/                 original DSA practice files
ITP/                 introduction-to-python practice files
revision/            merged revision material
src/dsa/             clean reference implementations
tests/               tests for reference implementations
docs/
  learning-roadmap.md
  problem-index.md
```

## Clean Reference Implementations

Requires Python 3.11+. From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements-dev.txt
python -m pytest
```

`make test` runs the same pytest suite. Collection is restricted to `tests/`:
original exercises may read stdin or run demonstrations on import.

The reference suite checks exhaustive small input combinations against Python's
built-in search/sort behavior, stable sorting with custom `__lt__` objects,
non-mutation, and stack/queue lifecycle errors. GitHub Actions exercises Python
3.11–3.13; AWS CodeBuild uses the same tests.

| Operation | Time | Extra space | Contract |
| --- | --- | --- | --- |
| Linear search | O(n) | O(1) | First matching index, or -1 |
| Binary search | O(log n) | O(1) | Ascending input; any matching index, or -1 |
| Merge sort | O(n log n) | O(n) | Stable new list; mutually orderable elements |
| Stack push / pop | O(1) amortized | O(n) storage | LIFO; empty pop/peek raises IndexError |
| Queue enqueue / dequeue | O(1) | O(n) storage | FIFO; empty dequeue raises IndexError |

Current reference modules:

- `src/dsa/searching.py`
- `src/dsa/sorting.py`
- `src/dsa/stack.py`
- `src/dsa/queue.py`

## Learning Philosophy

For every topic:

1. Understand the brute-force approach.
2. Write the simple implementation.
3. Optimize time and space complexity.
4. Add tests for edge cases.
5. Document the pattern in `docs/problem-index.md`.

## Status

This is the primary home for Python algorithm, DSA, and revision work.

The archived exercises are historical learning material; the supported, CI-tested surface is `src/dsa/`.
