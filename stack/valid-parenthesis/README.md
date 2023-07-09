# Valid Parenthesis 

### Solution

1. The code initializes an empty list called `stack`. This list will be used as a stack to store opening characters encountered so far.

2. It defines a dictionary `closeToOpen` that maps each closing character to its corresponding opening character.
   - This mapping is used to check if a closing character has a matching opening character on top of the stack.

3. It iterates over each character `c` in the string `s`.

4. If `c` is a closing character (')', ']', or '}'):
   - It checks if the stack is not empty and the top element of the stack matches the corresponding opening character for `c` in the `closeToOpen` dictionary.
   - If they match, it means a valid pair of opening and closing characters is found, so the top element is removed from the stack.
   - If they don't match, it means the string is not valid, and the function returns `False`.

5. If `c` is an opening character (not a closing character):
   - It is added to the stack.

6. After processing all characters in the string, it checks if the stack is empty.
   - If the stack is empty, it means all opening characters have been matched with closing characters, and the string is valid, so it returns `True`.
   - If the stack is not empty, it means there are unmatched opening characters, and the string is not valid, so it returns `False`.

The time complexity of this code is O(n), where n is the length of the string `s`.
- The code iterates over each character in the string once, performing constant-time operations for each character.

The space complexity of this code is O(n), where n is the length of the string `s`.
- The space used by the stack can grow up to the length of the string in the worst case.
- Additionally, the `closeToOpen` dictionary takes constant space since it contains a fixed number of entries (3 entries for the three types of closing characters).
- Therefore, the overall space complexity is proportional to the length of the string.