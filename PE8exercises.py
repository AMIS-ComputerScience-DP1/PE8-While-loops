def count_digits(number):
    """
    Ex 1: Count digits by continuously dividing by 10 until 0.
    """
    count = 0
    # TODO: Write while loop here
    
    return count

def collatz_steps(n):
    """
    Ex 2: Return steps to reach 1. (Even: n/2, Odd: 3n+1).
    """
    steps = 0
    # TODO: Write while loop here

    return steps

def sum_until_threshold(limit):
    """
    Ex 3: Add 1+2+3... Stop when sum > limit. Return the last number added.
    """
    total = 0
    number = 0
    # TODO: Write while loop here
    
    return number

def manual_remainder(numerator, denominator):
    """
    Ex 4: Calculate remainder of numerator / denominator using subtraction only.
    """
    # TODO: Write while loop here
    
    return numerator

def next_power_of_two(limit):
    """
    Ex 5: Find the first power of 2 that is greater than limit.
    Example: if limit is 10, powers are 1, 2, 4, 8, 16... return 16.
    """
    current_power = 1
    # TODO: Write while loop here
    
    return current_power


# ====================================================================
#  STUDENT TESTING SECTION
#  Run this file to test your code.
# ====================================================================

if __name__ == "__main__":
    def run_test(test_name, expected, actual):
        print(f"--- {test_name} ---")
        print(f"Expected: {expected}")
        print(f"Actual:   {actual}")
        
        if expected == actual:
            print("Result:   ✅ PASS\n")
            return True
        else:
            print("Result:   ❌ FAIL\n")
            return False

    total_tests = 0
    passed_tests = 0

    print("\n========================= STARTING TESTS =========================\n")

    # --- Test 1: Count Digits ---
    result = count_digits(9876)
    if run_test("Ex 1: count_digits(9876)", 4, result): passed_tests += 1
    total_tests += 1

    # --- Test 2: Collatz Steps ---
    result = collatz_steps(6)
    if run_test("Ex 2: collatz_steps(6)", 8, result): passed_tests += 1
    total_tests += 1

    # --- Test 3: Sum Until Threshold ---
    result = sum_until_threshold(10)
    if run_test("Ex 3: sum_until_threshold(10)", 5, result): passed_tests += 1
    total_tests += 1

    # --- Test 4: Manual Remainder ---
    result = manual_remainder(25, 7)
    if run_test("Ex 4: manual_remainder(25, 7)", 4, result): passed_tests += 1
    total_tests += 1

    # --- Test 5: Next Power of Two ---
    # Limit is 10. Powers: 1, 2, 4, 8, 16. 16 > 10.
    result = next_power_of_two(10)
    if run_test("Ex 5: next_power_of_two(10)", 16, result): passed_tests += 1
    total_tests += 1

    print("==================================================================")
    print(f"Final Score: {passed_tests}/{total_tests}")
