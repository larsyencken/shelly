# Shelly: shell tools for data analysis

Shelly's your friend. She helps bring interactivity and understanding to streaming data in the shell.

## Current status

The tools are useful, but are still being iterated on. They're likely to change in future.

## Commands

### drop

Like UNIX ``tail``, but takes a regex predicate to match against. Silently drops lines from the input until the desired condition is reached.

```
$ seq 100 | shelly drop --until 94
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
$ shelly random | head -n 5
0.19728902696
0.0793430590319
0.167234982902
0.19273188477
0.912588535256
```

### range

Display the running range of a stream of numbers.

```
$ shelly random | head -n 5 | shelly range
               min                max              delta
    0.515829248552     0.952509451768     0.436680203216
```

Range also understands numeric unix timestamps.

```
$ cat userlogs.timestamps | shelly range -t
                  min                   max        delta
  2012-09-17 19:41:43   2012-11-18 14:35:39      61 days
```

### subsample

Randomly drop a given proportion of lines from the input stream.

```
$ seq 100 | shelly subsample 0.05
9
37
73
93
99
```

### take

Like UNIX ``head``, but takes a regex predicate to match against. If ``--while`` is used, it pipes input until a mismatch occurs. If ``--until`` occurs, it pipes input until a match occurs.

```
$ seq 100 | shelly take --until 8
1
2
3
4
5
6
7
```

### trickle

Artificially cap the rate at which data moves through a shell pipe, with random delays. Use it like `tail -f logfile | shelly trickle 0.1` to see about `1/0.1 = 10` lines per second. Trickle operates on a line-by-line basis, with random delays between lines (for asthetics). For a super-reliable fixed byte rate, use instead the `pv` command instead, e.g. `pv -L 100k`.

## Future ideas

### New commands

- `symbolic`: perform symbolic math on the input
- `reduce`: reduce the input with a given operator

### Improvements

- `range`: mirror summaries provided by R, providing running standard devation and quartiles
