from typing import Dict # this adds type hinting for Dict
from collections import defaultdict

def count_characters(word: str) -> Dict[str, int]:
    output = defaultdict(int)

    for char in word:
        output[char] += 1
    
    return dict(output)




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
