# While Loop Practice (PE8)

**Objective:** Solve problems using `while` loops (digit extraction, sequences, and logic).

## Instructions
Open `PE8exercises.py` and complete the functions.

### Exercise 1: `count_digits(number)`
Count how many digits are in a positive integer without converting it to a string.
* **Logic:** While the number is greater than 0, divide it by 10 (integer division) to "chop off" the last digit. Count how many times you do this.
* **Return:** The count of digits.

### Exercise 2: `collatz_steps(n)`
Calculate the number of steps to reach 1 using the Collatz conjecture.
* **Logic:** While `n` is not 1:
    * If `n` is even, divide it by 2.
    * If `n` is odd, multiply by 3 and add 1.
    * Increment a step counter.
* **Return:** The total steps.

### Exercise 3: `sum_until_threshold(limit)`
Find how many natural numbers (1, 2, 3...) you must add together before the sum strictly exceeds the `limit`.
* **Logic:** Loop to add 1, then 2, then 3... to a running total. Stop when `total > limit`.
* **Return:** The last number added (the count of numbers).

### Exercise 4: `manual_remainder(numerator, denominator)`
Find the remainder of a division without using the `%` operator.
* **Logic:** While `numerator` is greater than or equal to `denominator`, keep subtracting `denominator` from `numerator`.
* **Return:** The final value of `numerator` (which is the remainder).

### Exercise 5: `reverse_integer(n)`
Reverse the digits of a number mathematically (e.g., 123 -> 321).
* **Logic:** While `n > 0`:
    1. Get the last digit (`n % 10`).
    2. Add it to a `reversed` variable (remember to multiply `reversed` by 10 first to shift digits left).
    3. Remove the last digit from `n` (`n // 10`).
* **Return:** The reversed number.
