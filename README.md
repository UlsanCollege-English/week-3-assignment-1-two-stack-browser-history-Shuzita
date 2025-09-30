[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/B9GOCrEG)
# HW1 — Browser History (Two Stacks)

## Story
You’re building a tiny browser history for a kiosk in the library. Visitors can click links freely, hit **Back**, and go **Forward**—but there’s no address bar and no tabs. It just needs to remember where they were and move sensibly.

## Task (Technical)
Implement a `BrowserHistory` with:
- `visit(url)`: loads a new page; clears the forward history
- `back() -> str`: moves one step back; error if already at the earliest page
- `forward() -> str`: moves one step forward; error if no forward page
- `current() -> str`: returns the current page

**Required approach:** use **two stacks** under the hood (e.g., `back_stack`, `fwd_stack`).  
Start on `"home"` by default.

## Hints
1) When you `visit(new)`, push the **current** page onto the **back stack**, set current to `new`, and **clear** the forward stack.  
2) `back()` pops from the back stack → becomes new current; push the old current onto the **forward** stack.  
3) Symmetrically, `forward()` pops from the **forward** stack and pushes the old current onto **back**.

## Run tests locally
```bash
python -m pytest -q
```
## Submit
Push to GitHub Classroom

Commit → push → check Actions.

## Common problems
- Forgetting to clear forward history on visit.
- Returning None instead of raising on invalid back/forward.
- Mutating stacks in the wrong order (swap bug).