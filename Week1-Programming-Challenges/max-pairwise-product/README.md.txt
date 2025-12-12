# Max Pairwise Product — Algorithm Testing with Python

> Notes and code inspired by *Algorithmic Toolbox (Part 1)* from **UC San Diego** and **HSE University**, taught by  
> Daniel M. Kane, Alexander Kulikov, Pavel Pevzner, Michael Levin, and Neil Rhodes.

---

## Overview

This repository demonstrates how to **design, optimize, and test algorithms** in Python — focusing on the classic **Maximum Pairwise Product** problem.

It includes:
- A **naive O(n²)** reference implementation  
- An **optimized O(n)** solution  
- A **reproducible test generator**  
- An **automated stress tester**

All scripts are implemented using only Python’s **standard library**.

---

##  Problem Definition

Find the maximum product of two distinct elements in an array:

\[
\max(a_i \times a_j) \quad \text{for } 1 \le i < j \le n
\]

---

##  Project Files

| File | Description |
|------|--------------|
| `model.py` | Naive baseline solution (O(n²)) |
| `main.py` | Optimized solution (O(n)) |
| `gen.py` | Random input generator |
| `test.py` | Stress testing script |
| `notes/Algorithmic_Toolbox_Part1.md` | Personal notes and learning reflections |

---

## How to Run

###  Generate Input
```bash
python gen.py 3 42 > input.txt