class Vendor:
    def __init__(self, name: str):
        self.name = name
        self.morning_sales = 0
        self.afternoon_sales = 0

    def set_sales(self, morning: int, afternoon: int):
        self.morning_sales = morning
        self.afternoon_sales = afternoon

    @property
    def total_sales(self) -> int:
        return self.morning_sales + self.afternoon_sales


class Dataset:
    def __init__(self, vendor_names):
        self.vendors = {name: Vendor(name) for name in vendor_names}

    def set_vendor_sales(self, name: str, morning: int, afternoon: int):
        if name in self.vendors:
            self.vendors[name].set_sales(morning, afternoon)

    def get_top_vendor(self):
        return max(self.vendors.values(), key=lambda v: v.total_sales)


class InputReader:
    def __init__(self):
        self.vendor_names = ['A', 'B', 'C', 'D', 'E']

    def __iter__(self):
        return self

    def __next__(self) -> Dataset:
        lines = []
        for _ in range(5):
            line = input().strip()
            if line == "0 0":
                if len(lines) == 0:
                    raise StopIteration
                else:
                    # If zero zero encountered in the middle of dataset, stop
                    raise StopIteration
            lines.append(line)

        # Confirm no premature end
        if any(s == '0 0' for s in lines):
            raise StopIteration

        morning_sales = []
        for line in lines:
            ms = list(map(int, line.split()))
            if len(ms) != 2:
                raise ValueError("Invalid input format")
            morning_sales.append(ms[0])
        afternoon_sales = []
        for line in lines:
            ms = list(map(int, line.split()))
            afternoon_sales.append(ms[1])

        dataset = Dataset(self.vendor_names)
        for i, name in enumerate(self.vendor_names):
            dataset.set_vendor_sales(name, morning_sales[i], afternoon_sales[i])

        return dataset


def main():
    import sys
    input = sys.stdin.readline
    vendor_names = ['A', 'B', 'C', 'D', 'E']

    while True:
        lines = []
        for _ in range(5):
            line = input().strip()
            if line == "0 0":
                return
            lines.append(line)
        # Also read morning and afternoon counts for 5 lines
        next_lines = []
        for _ in range(5):
            line = input().strip()
            if line == "0 0":
                return
            next_lines.append(line)

        dataset = Dataset(vendor_names)
        for i in range(5):
            morning = int(lines[i].split()[0])
            afternoon = int(next_lines[i].split()[1])
            dataset.set_vendor_sales(vendor_names[i], morning, afternoon)

        top = dataset.get_top_vendor()
        print(f"{top.name} {top.total_sales}")


if __name__ == "__main__":
    main()