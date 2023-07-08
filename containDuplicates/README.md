# Contains Duplicates 

### Solution: 



1. It begins by initializing an empty set called `hashSet`.
   - The set will be used to store unique elements encountered so far.

2. It iterates over each element `num` in the `nums` list.
   - For each element, it checks if it already exists in the `hashSet`.
   - If it does, it means a duplicate element has been found, and the function returns `True`.

3. If the loop completes without finding any duplicates, it adds the element `num` to the `hashSet`.

4. After the loop ends, it means no duplicates were found, so the function returns `False`.

The time complexity of this program is O(n), where n is the length of the `nums` list.
- The loop iterates over each element in the list, and the average time complexity for adding an element to a set is O(1).
- Therefore, the overall time complexity is proportional to the number of elements in the list.

The space complexity of this program is O(n), where n is the number of unique elements in the `nums` list.
- In the worst case, if all elements in the `nums` list are unique, the set `hashSet` will store all elements, resulting in a space complexity of O(n).
- In the best case, if all elements in the `nums` list are duplicates, the set `hashSet` will only store one element, resulting in a space complexity of O(1).