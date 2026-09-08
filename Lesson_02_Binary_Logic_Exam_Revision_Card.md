# 🎓 NIOS Senior Secondary (Class 12) — Computer Science (Code 330)
## 📌 Fast-Track Exam Revision Card — Lesson 2: Binary Logic
*Weightage in Theory Board Exam: 5 to 8 Marks | Expected Question Types: 1-Mark Definitions, 2-Mark Truth Tables, Universal Gates*

---

### 🌟 1. Core Definitions (Write These Exact 1-Liners for Full Marks)

* **Binary State:** Computer electronic circuits operate on only two voltage states:
  * **`1`** = High Voltage = **TRUE** = ON
  * **`0`** = Low Voltage = **FALSE** = OFF
* **Logic Gate:** An electronic circuit that takes one or more binary inputs and produces a single binary output based on logical rules.
* **Truth Table:** A structured table displaying all possible binary input combinations and their corresponding output.
* **ASCII:** **A**merican **S**tandard **C**ode for **I**nformation **I**nterchange (7-bit / 8-bit alphanumeric character code).
* **ISCII:** **I**ndian **S**cript **C**ode for **I**nformation **I**nterchange (8-bit code for Indian languages).

---

### ⚡ 2. The 3 Primary Logic Gates (Definitions, Formulas & Tables)

#### 1. AND Gate (`Y = A · B`)
* **Rule:** Output is **1 ONLY when ALL inputs are 1**.
| Input A | Input B | Output Y (A · B) |
| :---: | :---: | :---: |
| 0 | 0 | **0** |
| 0 | 1 | **0** |
| 1 | 0 | **0** |
| 1 | 1 | **1** |

---

#### 2. OR Gate (`Y = A + B`)
* **Rule:** Output is **1 if AT LEAST ONE input is 1**.
| Input A | Input B | Output Y (A + B) |
| :---: | :---: | :---: |
| 0 | 0 | **0** |
| 0 | 1 | **1** |
| 1 | 0 | **1** |
| 1 | 1 | **1** |

---

#### 3. NOT Gate (Inverter) (`Y = A'` or `Y = ~A`)
* **Rule:** Output is the **opposite** of the input (flips 0 to 1, and 1 to 0).
| Input A | Output Y (A') |
| :---: | :---: |
| 0 | **1** |
| 1 | **0** |

---

### 🔄 3. Universal Gates (Guaranteed 2-Mark Board Question)

> **Board Question:** *"Why are NAND and NOR called Universal Gates?"*  
> **Standard Answer:** *"NAND and NOR are called Universal Gates because any basic logic operation (AND, OR, NOT) can be implemented using only NAND gates or only NOR gates without needing any other gate."*

* **NAND Gate (`Y = (A · B)'`):** An AND gate followed by a NOT gate.
  * `0 NAND 0 = 1` | `0 NAND 1 = 1` | `1 NAND 0 = 1` | `1 NAND 1 = 0`
* **NOR Gate (`Y = (A + B)'`):** An OR gate followed by a NOT gate.
  * `0 NOR 0 = 1` | `0 NOR 1 = 0` | `1 NOR 0 = 0` | `1 NOR 1 = 0`

---

### 🔀 4. XOR Gate (Exclusive OR) (`Y = A ⊕ B`)
* **Rule:** Output is **1 ONLY when inputs are DIFFERENT**. If inputs are identical, output is 0.
| Input A | Input B | Output Y (A ⊕ B) |
| :---: | :---: | :---: |
| 0 | 0 | **0** (Same) |
| 0 | 1 | **1** (Different) |
| 1 | 0 | **1** (Different) |
| 1 | 1 | **0** (Same) |

---

### 🎯 5. Quick Decimal-to-Binary Conversion (Example: Convert 990 to Binary)

* Successive division by 2, recording remainders from bottom to top:
  * 990 ÷ 2 = 495 (Rem 0)
  * 495 ÷ 2 = 247 (Rem 1)
  * 247 ÷ 2 = 123 (Rem 1)
  * 123 ÷ 2 = 61 (Rem 1)
  * 61 ÷ 2 = 30 (Rem 1)
  * 30 ÷ 2 = 15 (Rem 0)
  * 15 ÷ 2 = 7 (Rem 1)
  * 7 ÷ 2 = 3 (Rem 1)
  * 3 ÷ 2 = 1 (Rem 1)
  * 1 ÷ 2 = 0 (Rem 1)
* **Result (Bottom to Top):** `(990)₁₀ = (1111011110)₂`

---
*Created for M. Haresh Kumar — NIOS Enrolment No. 080355263008 — Keep for Final Exam Revision*
