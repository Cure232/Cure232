import random
from collections import namedtuple

Point = namedtuple('Point', 'X Y')
"""
Point represents a coordinate with X and Y values.
"""

Shape = namedtuple('Shape', 'X Y Width Height')
"""
Shape represents a geometric figure with:
- X and Y coordinates for the top-left corner
- Width and Height dimensions.
"""

Block = namedtuple('Block', 'template start_pos end_pos name next')
"""
Block represents a Tetris block with:
- template: The layout of the block as a grid of characters.
- start_pos: The top-left coordinate of the block.
- end_pos: The bottom-right coordinate of the block.
- name: The type of the block (e.g., 'S', 'Z').
- next: The index of the next rotation state.
"""

# The design of block shapes: Initially, I designed them as 4x4 grids because the maximum length and width are 4.
# This way, rotation is simplified by just replacing one shape with another.
# To implement this, fixing the top-left corner coordinate is sufficient.

# S-shaped block
S_BLOCK = [Block(['.OO',
                  'OO.',
                  '...'], Point(0, 0), Point(2, 1), 'S', 1),
           Block(['O..',
                  'OO.',
                  '.O.'], Point(0, 0), Point(1, 2), 'S', 0)]

# Z-shaped block
Z_BLOCK = [Block(['OO.',
                  '.OO',
                  '...'], Point(0, 0), Point(2, 1), 'Z', 1),
           Block(['.O.',
                  'OO.',
                  'O..'], Point(0, 0), Point(1, 2), 'Z', 0)]

# I-shaped block
I_BLOCK = [Block(['.O..',
                  '.O..',
                  '.O..',
                  '.O..'], Point(1, 0), Point(1, 3), 'I', 1),
           Block(['....',
                  '....',
                  'OOOO',
                  '....'], Point(0, 2), Point(3, 2), 'I', 0)]

# O-shaped block
O_BLOCK = [Block(['OO',
                  'OO'], Point(0, 0), Point(1, 1), 'O', 0)]

# J-shaped block
J_BLOCK = [Block(['O..',
                  'OOO',
                  '...'], Point(0, 0), Point(2, 1), 'J', 1),
           Block(['.OO',
                  '.O.',
                  '.O.'], Point(1, 0), Point(2, 2), 'J', 2),
           Block(['...',
                  'OOO',
                  '..O'], Point(0, 1), Point(2, 2), 'J', 3),
           Block(['.O.',
                  '.O.',
                  'OO.'], Point(0, 0), Point(1, 2), 'J', 0)]

# L-shaped block
L_BLOCK = [Block(['..O',
                  'OOO',
                  '...'], Point(0, 0), Point(2, 1), 'L', 1),
           Block(['.O.',
                  '.O.',
                  '.OO'], Point(1, 0), Point(2, 2), 'L', 2),
           Block(['...',
                  'OOO',
                  'O..'], Point(0, 1), Point(2, 2), 'L', 3),
           Block(['OO.',
                  '.O.',
                  '.O.'], Point(0, 0), Point(1, 2), 'L', 0)]

# T-shaped block
T_BLOCK = [Block(['.O.',
                  'OOO',
                  '...'], Point(0, 0), Point(2, 1), 'T', 1),
           Block(['.O.',
                  '.OO',
                  '.O.'], Point(1, 0), Point(2, 2), 'T', 2),
           Block(['...',
                  'OOO',
                  '.O.'], Point(0, 1), Point(2, 2), 'T', 3),
           Block(['.O.',
                  'OO.',
                  '.O.'], Point(0, 0), Point(1, 2), 'T', 0)]

BLOCKS = {'O': O_BLOCK,
          'I': I_BLOCK,
          'Z': Z_BLOCK,
          'T': T_BLOCK,
          'L': L_BLOCK,
          'S': S_BLOCK,
          'J': J_BLOCK}


def get_block():
    """
    Randomly select a block and return it.

    Returns:
        Block: A randomly selected block instance.
    """
    block_name = random.choice('OIZTLSJ')
    b = BLOCKS[block_name]
    idx = random.randint(0, len(b) - 1)
    return b[idx]


def get_next_block(block):
    """
    Get the next rotational state of the block.

    Args:
        block (Block): The current block.

    Returns:
        Block: The next rotation state of the block.
    """
    b = BLOCKS[block.name]
    return b[block.next]
