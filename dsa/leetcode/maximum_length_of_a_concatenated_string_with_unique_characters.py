class Solution:
    def get_max_len_concatenated_str(self, arr, ind, included_set):
        if ind == len(arr):
            return len(included_set)

        if len(set(arr[ind])) != len(arr[ind]):
            return self.get_max_len_concatenated_str(arr, ind+1, included_set)

        without_count = self.get_max_len_concatenated_str(arr, ind+1, included_set)
        current_set = set(arr[ind])
        combined_set = included_set.union(current_set)
        with_count = 0
        if len(combined_set) == (len(included_set) + len(current_set)):
            with_count = self.get_max_len_concatenated_str(arr, ind+1, combined_set)
        return max(without_count, with_count)

    def maxLength(self, arr: List[str]) -> int:
        return self.get_max_len_concatenated_str(arr, 0, set())