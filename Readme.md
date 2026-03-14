
# ♾️ The Perfect Number Research Archive

### 📝 Project Note
*   **Original Research:** This project was originally developed in **March 2024**.
*   **Restoration:** These files were restored and archived on GitHub in **2026** to preserve the research.
*   **Documentation:** This README and the file mappings were generated with the assistance of **AI**. While every effort was made to categorize the logic accurately, some minor mismatches in file mapping or descriptions may exist compared to the original 2024 intent.

Thank you for visiting the archive!

A comprehensive collection of algorithms and mathematical proofs dedicated to the discovery, verification, and visualization of **Perfect Numbers** and **Mersenne Primes**. This repository spans the evolution of number theory research, from classic trial division to high-performance deterministic tests like Lucas-Lehmer and AKS.

## 📂 Repository Structure

To navigate the 19-file collection, the repository is organized by computational logic:

*   **`/primes`**: Foundational primality testing (Trial Division, Wilson’s Theorem, AKS).
*   **`/generators`**: Master scripts for discovering Mersenne Primes and Perfect Numbers.
*   **`/verifiers`**: Tools for checking specific candidates and benchmarking accuracy.
*   **`/high-performance`**: Optimized, silent, and batch-processing scripts for large-scale searches.
*   **`/visualization`**: Geometric mapping of prime distributions (Ulam Spiral).

---

## 📜 Algorithm Master List


| Filename | Category | Logic Used | Speed / Notes |
| :--- | :--- | :--- | :--- |
| `dp.1.py` | **Trial Division** | $\sqrt{n}$ + Digit Filtering | Practical for general-purpose prime lists. |
| `dpp3.py` | **Wilson's Theorem** | $(n - 1)! \equiv -1 \pmod{n}$ | Theoretical; limited by $n!$ growth. |
| `P.1.py` | **Library Baseline** | Miller-Rabin & Lucas Tests | **Gold Standard.** Used for verification. |
| `P.2.py` | **Divisor Summation** | Brute Force ($1$ to $n$) | Targeted at **33,550,336** (5th Perfect). |
| `P.3.py` | **Negative Test** | Proper Divisor Summation | Verified **86,619,373** is **not** perfect. |
| `P.4.py` | **Lucas-Lehmer (LLT)** | $S_{i} = (S_{i-1}^2 - 2) \pmod{M_n}$ | Finds Mersenne Primes efficiently. |
| `P.5.py` | **Master Generator** | LLT + Euclid-Euler | **Full Pipeline.** Generates perfect numbers. |
| `P.6.py` | **Optimized Search** | $\sqrt{n}$ Divisor Pairing | **1,000x faster** than P.2. Direct check. |
| `P.7.py` | **Interactive Verifier**| $\sqrt{n}$ + `tqdm` + Loop | **Final UI Version.** Best for repeated testing. |
| `PP.1.py` | **Continuous Search** | LLT + Internal Math Logging | **Verbose Mode.** Shows internal math growth. |
| `PP.2.py` | **Probabilistic Scan** | Miller-Rabin + Bitwise Ops | **Fastest.** Best for huge candidate ranges. |
| `PP.3.py` | **AKS Polynomial** | $(x-1)^n \equiv (x^n-1) \pmod{n}$ | **Mathematical Masterpiece.** Deterministic. |
| `PP.4.py` | **Mersenne Brute** | Trial Division ($\sqrt{2^i-1}$) | Validates first 80 exponents for accuracy. |
| `PP.5.py` | **Range Benchmark** | Iterative Modular Reductions | Measures performance across specific ranges. |
| `PP.6.py` | **Large-Scale Search**| Batch LLT (No Logs) | **Most Aggressive.** Optimized for 800k+. |
| `PP.7.py` | **Modular Sieve** | Hardcoded Prime List | **"Security Guard."** Filters composites early. |
| `PPP.2.py` | **Official Benchmark** | Silent Miller-Rabin | **Scientific Testing.** Multi-stage timing. |
| `PR1.py` | **Two-Stage Search** | Last-Digit Filter ($L2$) | **UI Optimized.** Skips evens/5s automatically. |
| `PR2.py` | **Visualization** | **Ulam Spiral Algorithm** | **Pattern Seeking.** Maps primes to a 2D grid. |

---

## 🚀 Featured Highlights

### 1. The High-Performance Pipeline (`PP.6` + `PP.7`)
For large-scale discovery, this project uses a three-tier filtering system:
1.  **Sieve (`PP.7`)**: Immediately discards 60% of candidates using a hardcoded list of 1,200 primes.
2.  **Probabilistic (`PP.2`)**: Rapidly screens remaining candidates using Miller-Rabin.
3.  **Deterministic (`PP.6`)**: Performs the final Lucas-Lehmer verification without logging overhead.

### 2. Theoretical Accuracy (`PP.3`)
Includes a full implementation of the **AKS Primality Test**, proving that primality can be determined in polynomial time ($P$). While computationally heavy, it ensures 100% mathematical certainty.

### 3. Visual Analysis (`PR2`)
The **Ulam Spiral** generator allows for the study of prime clustering. By mapping primes onto a coordinate system, we can visually inspect for patterns that may correlate with the spacing of Mersenne exponents.

---

## 🛠️ Requirements & Installation

Most scripts require standard Python 3.x. Advanced UI features require `tqdm`.

```bash
# Clone the repository
git clone https://github.com

# Install dependencies
pip install tqdm sympy matplotlib.

---

## Author
**Krishna** — Experimenting with Perfect Numbers and researching the most efficient methods for primality testing.


