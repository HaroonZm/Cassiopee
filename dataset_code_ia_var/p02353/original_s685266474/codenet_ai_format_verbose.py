class LazySegmentTree:
    """
    General purpose Lazy Segment Tree for efficient range queries and range updates.

    op: Binary associative operation for range queries.
    op_identity: Identity element for op.
    comp: Binary associative operation for update composition.
    comp_identity: Identity element for comp.
    apply: Function to apply an update.
    """

    @classmethod
    def with_all_identity(cls, range_query_op, range_query_identity, update_compose_op, update_identity, apply_update, num_elements):
        internal_size = 2 << (num_elements - 1).bit_length()
        return cls(
            range_query_op,
            range_query_identity,
            update_compose_op,
            update_identity,
            apply_update,
            [range_query_identity] * internal_size,
            [update_identity] * internal_size
        )

    @classmethod
    def from_raw_data(cls, range_query_op, range_query_identity, update_compose_op, update_identity, apply_update, data_list):
        segment_size = 1 << (len(data_list) - 1).bit_length()
        segment_data = [range_query_identity] * (2 * segment_size)
        segment_data[segment_size:segment_size + len(data_list)] = data_list

        for index in reversed(range(segment_size)):
            segment_data[index] = range_query_op(segment_data[2 * index], segment_data[2 * index + 1])
        return cls(
            range_query_op,
            range_query_identity,
            update_compose_op,
            update_identity,
            apply_update,
            segment_data,
            [update_identity] * segment_size
        )

    def __init__(self, range_query_op, range_query_identity, update_compose_op, update_identity, apply_update, segment_tree_data, lazy_update_data):
        self.range_query_op = range_query_op
        self.range_query_identity = range_query_identity
        self.update_compose_op = update_compose_op
        self.update_identity = update_identity
        self.apply_update = apply_update
        self.segment_tree_data = segment_tree_data
        self.lazy_update_data = lazy_update_data
        self.segment_size = len(self.segment_tree_data) // 2
        self.tree_depth = self.segment_size.bit_length() - 1
        self.left_indices = [0] * self.tree_depth
        self.right_indices = [0] * self.tree_depth

    def _record_indices(self, index, indices):
        mask = index // (index & -index)
        index >>= 1
        for depth in reversed(range(self.tree_depth)):
            indices[depth] = index if index < mask else 0
            index >>= 1

    def _propagate_all_lazy_updates_top_down(self):
        seg_data = self.segment_tree_data
        lazy_data = self.lazy_update_data
        apply_update = self.apply_update
        compose_update = self.update_compose_op
        update_identity = self.update_identity
        segment_halflen = self.segment_size >> 1

        for left_idx, right_idx in zip(self.left_indices, self.right_indices):
            if left_idx > 0:
                pending_update = lazy_data[left_idx]
                if pending_update != update_identity:
                    lazy_data[left_idx] = update_identity
                    child_left = left_idx << 1
                    child_right = (left_idx << 1) | 1
                    lazy_data[child_left] = compose_update(lazy_data[child_left], pending_update)
                    seg_data[child_left] = apply_update(seg_data[child_left], pending_update, segment_halflen)
                    lazy_data[child_right] = compose_update(lazy_data[child_right], pending_update)
                    seg_data[child_right] = apply_update(seg_data[child_right], pending_update, segment_halflen)
            if left_idx < right_idx:
                pending_update = lazy_data[right_idx]
                if pending_update != update_identity:
                    lazy_data[right_idx] = update_identity
                    child_left = right_idx << 1
                    child_right = (right_idx << 1) | 1
                    lazy_data[child_left] = compose_update(lazy_data[child_left], pending_update)
                    seg_data[child_left] = apply_update(seg_data[child_left], pending_update, segment_halflen)
                    lazy_data[child_right] = compose_update(lazy_data[child_right], pending_update)
                    seg_data[child_right] = apply_update(seg_data[child_right], pending_update, segment_halflen)
            segment_halflen >>= 1

    def _recalculate_all_parents_bottom_up(self):
        seg_data = self.segment_tree_data
        op = self.range_query_op
        for left_idx, right_idx in zip(reversed(self.left_indices), reversed(self.right_indices)):
            if left_idx > 0:
                seg_data[left_idx] = op(seg_data[2 * left_idx], seg_data[2 * left_idx + 1])
            if left_idx < right_idx:
                seg_data[right_idx] = op(seg_data[2 * right_idx], seg_data[2 * right_idx + 1])

    def update_range(self, update_left, update_right, update_value):
        lazy_data = self.lazy_update_data
        seg_data = self.segment_tree_data
        compose_update = self.update_compose_op
        apply_update = self.apply_update

        update_left += self.segment_size
        update_right += self.segment_size
        self._record_indices(update_left, self.left_indices)
        self._record_indices(update_right, self.right_indices)
        self._propagate_all_lazy_updates_top_down()
        coverage = 1
        while update_left < update_right:
            if update_left & 1:
                lazy_data[update_left] = compose_update(lazy_data[update_left], update_value)
                seg_data[update_left] = apply_update(seg_data[update_left], update_value, coverage)
                update_left += 1
            if update_right & 1:
                update_right -= 1
                lazy_data[update_right] = compose_update(lazy_data[update_right], update_value)
                seg_data[update_right] = apply_update(seg_data[update_right], update_value, coverage)
            update_left >>= 1
            update_right >>= 1
            coverage <<= 1
        self._recalculate_all_parents_bottom_up()

    def query_range(self, query_left, query_right):
        seg_data = self.segment_tree_data
        op = self.range_query_op

        query_left += self.segment_size
        query_right += self.segment_size
        self._record_indices(query_left, self.left_indices)
        self._record_indices(query_right, self.right_indices)
        self._propagate_all_lazy_updates_top_down()

        left_accumulator = self.range_query_identity
        right_accumulator = self.range_query_identity
        while query_left < query_right:
            if query_left & 1:
                left_accumulator = op(left_accumulator, seg_data[query_left])
                query_left += 1
            if query_right & 1:
                query_right -= 1
                right_accumulator = op(seg_data[query_right], right_accumulator)
            query_left >>= 1
            query_right >>= 1
        return op(left_accumulator, right_accumulator)


import sys
input_read = sys.stdin.buffer.read
input_readline = sys.stdin.buffer.readline

from operator import add as sum_operator

if __name__ == '__main__':
    num_elements, num_queries = map(int, input_readline().split())
    query_and_update_data_iterator = map(int, input_read().split())

    segment_tree = LazySegmentTree.with_all_identity(
        range_query_op=sum_operator,
        range_query_identity=0,
        update_compose_op=lambda old_update, new_update: old_update if new_update is None else new_update,
        update_identity=None,
        apply_update=lambda prev_value, update_val, segment_length: prev_value if update_val is None else update_val * segment_length,
        num_elements=num_elements
    )

    try:
        while True:
            operation_type = next(query_and_update_data_iterator)
            if operation_type:
                query_left = next(query_and_update_data_iterator)
                query_right = next(query_and_update_data_iterator) + 1
                print(segment_tree.query_range(query_left, query_right))
            else:
                update_left = next(query_and_update_data_iterator)
                update_right = next(query_and_update_data_iterator) + 1
                update_value = next(query_and_update_data_iterator)
                segment_tree.update_range(update_left, update_right, update_value)
    except StopIteration:
        pass