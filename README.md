# Shelly: shell tools for data analysis

Shelly's your friend. She helps bring interactivity and understanding to streaming data in the shell.

## Commands

### drop

Like UNIX ``tail``, but takes a regex predicate to match against. Silently drops lines from the input until the desired condition is reached.

```
$ seq 100 | drop --until 94
94
95
96
97
98
99
100
```

### exists

Filter a stream of filenames to only those which exist (or the reverse).

### random

Generate an infinite stream of random numbers.

```
$ random | head -n 5
0.19728902696
0.0793430590319
0.167234982902
0.19273188477
0.912588535256
```

### range

Display the running range of a stream of numbers.

```
$ random | head -n 5 | range
               min                max              delta
    0.515829248552     0.952509451768     0.436680203216
```

### subsample

Randomly drop a given proportion of lines from the input stream.

```
$ seq 100 | subsample 0.05
9
37
73
93
99
```

### take

Like UNIX ``head``, but takes a regex predicate to match against. If ``--while`` is used, it pipes input until a mismatch occurs. If ``--until`` occurs, it pipes input until a match occurs.

```
$ seq 100 | take --until 8
1
2
3
4
5
6
7
```

### trickle

Artificially cap the rate at which data moves through a shell pipe.

## Future ideas

### New commands

- `symbolic`: perform symbolic math on the input
- `reduce`: reduce the input with a given operator

### Improvements

- `range`: mirror summaries provided by R, providing running standard devation and quartiles
