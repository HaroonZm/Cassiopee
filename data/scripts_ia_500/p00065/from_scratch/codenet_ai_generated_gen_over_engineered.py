from collections import defaultdict
from typing import List, Tuple, Dict, Protocol, Iterator


class TransactionRecord:
    def __init__(self, customer_id: int, transaction_day: int) -> None:
        self.customer_id = customer_id
        self.transaction_day = transaction_day

    def __repr__(self):
        return f"TransactionRecord(customer_id={self.customer_id}, transaction_day={self.transaction_day})"


class TransactionDataParser(Protocol):
    def parse(self, raw_data: List[str]) -> List[TransactionRecord]:
        ...


class SimpleTransactionDataParser:
    def parse(self, raw_data: List[str]) -> List[TransactionRecord]:
        records = []
        for line in raw_data:
            if not line.strip():
                continue
            parts = line.strip().split(",")
            if len(parts) != 2:
                continue  # skip malformed lines
            cid, day = parts
            records.append(TransactionRecord(int(cid), int(day)))
        return records


class TransactionAggregator:
    def __init__(self) -> None:
        self.data: Dict[int, List[TransactionRecord]] = defaultdict(list)

    def add_transactions(self, records: List[TransactionRecord]) -> None:
        for rec in records:
            self.data[rec.customer_id].append(rec)

    def get_transaction_counts(self) -> Dict[int, int]:
        return {cid: len(txns) for cid, txns in self.data.items()}


class ConsecutiveMonthAnalyzer:
    def __init__(self, this_month_data: List[TransactionRecord], last_month_data: List[TransactionRecord]) -> None:
        self.this_month_aggregator = TransactionAggregator()
        self.last_month_aggregator = TransactionAggregator()
        self.this_month_aggregator.add_transactions(this_month_data)
        self.last_month_aggregator.add_transactions(last_month_data)

    def analyze(self) -> List[Tuple[int, int]]:
        this_month_counts = self.this_month_aggregator.get_transaction_counts()
        last_month_counts = self.last_month_aggregator.get_transaction_counts()
        consecutive_customers = set(this_month_counts.keys()) & set(last_month_counts.keys())
        results = []
        for cid in consecutive_customers:
            total_count = this_month_counts[cid] + last_month_counts[cid]
            results.append((cid, total_count))
        results.sort(key=lambda x: x[0])
        return results


class TransactionDataInputSplitter:
    def __init__(self, lines: List[str]) -> None:
        self.lines = lines

    def split(self) -> Tuple[List[str], List[str]]:
        # Split input by empty line into last month and this month data
        idx = None
        for i, line in enumerate(self.lines):
            if line.strip() == "":
                idx = i
                break
        if idx is None:
            # no empty line, assume all lines belong to this month only, last month empty
            return [], self.lines
        last_month_data = self.lines[:idx]
        this_month_data = self.lines[idx + 1 :]
        return this_month_data, last_month_data


def main():
    import sys

    raw_lines = [line.rstrip("\n") for line in sys.stdin]

    splitter = TransactionDataInputSplitter(raw_lines)
    this_month_raw, last_month_raw = splitter.split()

    parser = SimpleTransactionDataParser()
    this_month_records = parser.parse(this_month_raw)
    last_month_records = parser.parse(last_month_raw)

    analyzer = ConsecutiveMonthAnalyzer(this_month_records, last_month_records)
    result = analyzer.analyze()

    for cid, count in result:
        print(cid, count)


if __name__ == "__main__":
    main()