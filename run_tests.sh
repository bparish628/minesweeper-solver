#! /bin/bash
echo -e "INTERMEDIATE,0,0\nBEGINNER,0,0" > stats.sav && python minesweeper.py --beginner-solver && python minesweeper.py --intermediate-solver