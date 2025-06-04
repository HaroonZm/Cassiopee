class CombinatorialFunctionsTwelvefold:

    def __init__(self, maximum_size, modulus, precompute_tables=True):

        self.modulus = modulus

        self.factorial = [0 for _ in range(maximum_size + 1)]
        self.inverse_factorial = [0 for _ in range(maximum_size + 1)]
        self.factorial[0] = 1
        self.inverse_factorial[0] = 1

        for index in range(maximum_size):
            self.factorial[index + 1] = self.factorial[index] * (index + 1) % modulus

        self.inverse_factorial[maximum_size] = pow(self.factorial[maximum_size], modulus - 2, modulus)

        for index in range(maximum_size - 1, -1, -1):
            self.inverse_factorial[index] = self.inverse_factorial[index + 1] * (index + 1) % modulus

        if precompute_tables:
            self._build_combinatorial_tables(maximum_size)

    def _build_combinatorial_tables(self, table_size):

        self.stirling_second_kind = [
            [0 for _ in range(table_size + 1)]
            for _ in range(table_size + 1)
        ]
        self.bell_numbers_table = [
            [0 for _ in range(table_size + 1)]
            for _ in range(table_size + 1)
        ]
        self.integer_partitions_table = [
            [0 for _ in range(table_size + 1)]
            for _ in range(table_size + 1)
        ]
        self.stirling_second_kind[0][0] = 1
        self.bell_numbers_table[0][0] = 1

        for num_elements in range(table_size):
            for num_subsets in range(table_size):
                self.stirling_second_kind[num_elements + 1][num_subsets + 1] = (
                    self.stirling_second_kind[num_elements][num_subsets] +
                    (num_subsets + 1) * self.stirling_second_kind[num_elements][num_subsets + 1]
                ) % self.modulus

        for num_elements in range(table_size):
            for num_subsets in range(table_size):
                self.bell_numbers_table[num_elements + 1][num_subsets + 1] = (
                    self.bell_numbers_table[num_elements + 1][num_subsets] +
                    self.stirling_second_kind[num_elements + 1][num_subsets + 1]
                ) % self.modulus

        for max_integer in range(table_size):
            self.integer_partitions_table[0][max_integer] = 1

        for total in range(table_size):
            for max_integer in range(table_size):
                if total - max_integer >= 0:
                    value = (
                        self.integer_partitions_table[total + 1][max_integer] +
                        self.integer_partitions_table[total - max_integer][max_integer + 1]
                    )
                else:
                    value = self.integer_partitions_table[total + 1][max_integer]
                self.integer_partitions_table[total + 1][max_integer + 1] = value % self.modulus

    def solve(
        self,
        num_elements,
        num_subsets,
        require_distinct_elements=False,
        require_distinct_subsets=False,
        exclude_empty_subsets=False,
        force_multiplicity_greater_than_one=False
    ):

        assert not (exclude_empty_subsets and force_multiplicity_greater_than_one)

        option_distinct_elements = require_distinct_elements
        option_distinct_subsets = require_distinct_subsets
        option_exclude_empty = exclude_empty_subsets
        option_multiplicity_gt1 = force_multiplicity_greater_than_one

        table_index = (
            int(option_distinct_elements) * 3 +
            int(option_distinct_subsets) * 6 +
            int(option_exclude_empty) +
            int(option_multiplicity_gt1) * 2
        )

        compute_methods = [
            self._solve_case_1,
            self._solve_case_2,
            self._solve_case_3,
            self._solve_case_4,
            self._solve_case_5,
            self._solve_case_6,
            self._solve_case_7,
            self._solve_case_8,
            self._solve_case_9,
            self._solve_case_10,
            self._solve_case_11,
            self._solve_case_12
        ]
        return compute_methods[table_index](num_elements, num_subsets)

    def _solve_case_1(self, num_elements, num_subsets):
        # Case 1: All mappings (k^n)
        return pow(num_subsets, num_elements, self.modulus)

    def _solve_case_2(self, num_elements, num_subsets):
        # Case 2: Surjective mappings (injective mapping count)
        if num_subsets - num_elements < 0:
            return 0
        return self.factorial[num_subsets] * self.inverse_factorial[num_subsets - num_elements] % self.modulus

    def _solve_case_3(self, num_elements, num_subsets):
        # Case 3: Surjection mappings (Stirling number * k!)
        return self.stirling_second_kind[num_elements][num_subsets] * self.factorial[num_subsets] % self.modulus

    def _solve_case_4(self, num_elements, num_subsets):
        # Case 4: Multisets (n+k-1 choose n)
        if num_subsets == 0:
            return 0
        return (
            self.factorial[num_elements + num_subsets - 1] *
            self.inverse_factorial[num_elements] *
            self.inverse_factorial[num_subsets - 1]
        ) % self.modulus

    def _solve_case_5(self, num_elements, num_subsets):
        # Case 5: Multisets with distinct objects (k choose n)
        if num_subsets - num_elements < 0:
            return 0
        return (
            self.factorial[num_subsets] *
            self.inverse_factorial[num_elements] *
            self.inverse_factorial[num_subsets - num_elements]
        ) % self.modulus

    def _solve_case_6(self, num_elements, num_subsets):
        # Case 6: Combinations with repetition (n-1 choose k-1)
        if num_elements - num_subsets < 0 or num_subsets == 0:
            return 0
        return (
            self.factorial[num_elements - 1] *
            self.inverse_factorial[num_subsets - 1] *
            self.inverse_factorial[num_elements - num_subsets]
        ) % self.modulus

    def _solve_case_7(self, num_elements, num_subsets):
        # Case 7: Bell number table value
        return self.bell_numbers_table[num_elements][num_subsets]

    def _solve_case_8(self, num_elements, num_subsets):
        # Case 8: All ones if possible
        if num_subsets - num_elements < 0:
            return 0
        return 1

    def _solve_case_9(self, num_elements, num_subsets):
        # Case 9: Stirling numbers only
        return self.stirling_second_kind[num_elements][num_subsets]

    def _solve_case_10(self, num_elements, num_subsets):
        # Case 10: Integer partitions table
        return self.integer_partitions_table[num_elements][num_subsets]

    def _solve_case_11(self, num_elements, num_subsets):
        # Case 11: All ones if possible
        if num_subsets - num_elements < 0:
            return 0
        return 1

    def _solve_case_12(self, num_elements, num_subsets):
        # Case 12: Integer partitions minus k
        if num_elements - num_subsets < 0:
            return 0
        return self.integer_partitions_table[num_elements - num_subsets][num_subsets]


number_of_elements, number_of_subsets = map(int, input().split())

combinatorial_solver = CombinatorialFunctionsTwelvefold(1000, 10 ** 9 + 7, False)

# Example: solve for "exclude_empty_subsets=True", "require_distinct_subsets=True" (12th context)
result = combinatorial_solver.solve(
    number_of_elements,
    number_of_subsets,
    require_distinct_elements=False,
    require_distinct_subsets=True,
    exclude_empty_subsets=True,
    force_multiplicity_greater_than_one=False
)

print(result)