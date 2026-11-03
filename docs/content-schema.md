# Question bank format

Source files: `content/bank/<section>/<topic>.jsonl` (large topics may split: `<topic>-2.jsonl`). One JSON object per line, UTF-8. Sections, topics, id prefixes and targets are in `content/blueprint.json`.

```json
{"id":"mc-t0001","pool":"test","level":2,"stem":"...","options":["...","...","...","...","..."],"answer":1,"explanation":"..."}
```
| Field | Rule |
|---|---|
| `id` | `<prefix>-t0001` for the mock pool, `<prefix>-p0001` for practice; prefix is in the blueprint |
| `pool` | `test` (goes into the 10 mock papers) or `practice` (subject practice only). Never reuse an item across pools |
| `level` | 1 easy, 2 medium, 3 hard. Aim for about 25 / 55 / 20 % |
| `options` | exactly 4 strings (single best answer, options A-D) |
| `answer` | index 0-3 of the correct option. Spread evenly; never a pattern |
| `explanation` | why the answer is right and why the most tempting wrong option is wrong. 2-4 sentences |
| `table` | optional: rows of strings, first row is the header. Lab panels only, when they read better as a table |
