# minesweeper-solver
A minesweeper game with a built in solver.
This game requires python 2.7 to be install on your system. This was also only tested on a unix machine.

There are no test cases provided considering this is using a random generated board.

## Running the program
To play a minesweeper game: (you can use @hint as your move if you need help solving it)
```
python minesweeper.py
```

To run the solver:
```
python minesweeper.py --beginner-solver
OR
python minesweeper.py --intermediate-solver
```

To reset the .sav file:
```
echo -e "INTERMEDIATE,0,0\nBEGINNER,0,0" > stats.sav
```


## Running Tests
The point of this project is to test the winability of a game of minesweeper with a solver. This includes both beginner and intermediate boards.

For testing purposes, it will just be using a random board each time, so there is no specific input besides running the solvers (i.e. `python minesweeper.py --beginner-solver` ). After it's run it will create/append to the `stats.sav` file the wins and games played (which is persisted between games). If you want to reset it you can run `echo -e "INTERMEDIATE,0,0\nBEGINNER,0,0" > stats.sav`.

This will produce some results on the win percentage of the solver. This is just printing out the `stats.sav` file.

If you want a quick and easy command to run both solvers and reset the `stat.sav` file run:
```
echo -e "INTERMEDIATE,0,0\nBEGINNER,0,0" > stats.sav && python minesweeper.py --beginner-solver && python minesweeper.py --intermediate-solver
```

If you want to change the amount of times to run the solver, open up `minesweeper.py` and change the `TIMES_TO_RUN_SOLVER` to equal whatever number you want.