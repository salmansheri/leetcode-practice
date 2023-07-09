# Valid Anagrams

### Solution

1. The program starts by checking if the lengths of the strings `s` and `t` are different. If they are not equal, it immediately returns `False` because two strings of different lengths cannot be anagrams.

2. It initializes two empty dictionaries, `countS` and `countT`, to store the counts of each character in the respective strings.

3. It iterates over the range of indices from 0 to the length of `s` (or `t` since they have the same length).

4. Inside the loop, it increments the count of the character `s[i]` in `countS` using the `countS.get(s[i], 0) + 1` expression.

   - The `get` method retrieves the current count of the character `s[i]` from `countS`. If the character is not present, it returns 0.
   - It then increments the count by 1 and assigns the updated value back to `countS[s[i]]`.

5. Similarly, it updates the count of the character `t[i]` in `countT`.

6. After counting the characters in both strings, it iterates over the unique characters in `countS` using the `for` loop.

7. For each character `c` in `countS`, it checks if the count of `c` in `countS` is equal to the count of `c` in `countT`. If they are not equal, it means `s` and `t` are not anagrams, so it returns `False`.

8. If the loop completes without finding any discrepancies, it means all characters in `s` and `t` have the same counts, and the function returns `True`.

The time complexity of this program is O(n), where n is the length of the strings `s` and `t`.

- The program iterates over the strings once to count the characters, which takes O(n) time.
- The subsequent loop iterates over the unique characters in `countS`, which takes O(k) time, where k is the number of unique characters in `s` and `t`. However, k is at most the number of distinct characters in the character set, which is typically constant and independent of the input size.

The space complexity of this program is O(k), where k is the number of unique characters in `s` and `t`.

- The dictionaries `countS` and `countT` store the counts of characters, and the number of unique characters is proportional to k.
- In the worst case, if all characters in `s` and `t` are unique, the space complexity will be O(n).
- In the best case, if all characters in `s` and `t` are the same, the space complexity will be O(1).
