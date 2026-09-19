# Reference algorithm verification

```bash
python -m pip install -r requirements-dev.txt
make test
make compile
```

Pytest collection is limited to `tests/`; historical exercises can run input or
print operations on import. Add new maintained algorithms under `src/dsa/` and
cover empty inputs, duplicates, non-mutation, and declared ordering contracts.
Binary search assumes ascending data and may return any duplicate match.
Exhaustive small-domain tests compare search and sorting results to built-in
oracles; queue and stack tests exercise reuse and underflow.
