# Shelly: shell tools for data analysis

Shelly's your friend. She helps bring interactivity and understanding to streaming data in the shell.

## Commands

### drop

Like UNIX ``tail``, but takes a regex predicate to match against. Silently drops lines from the input until the desired condition is reached.

### exists

Filter a stream of filenames to only those which exist (or the reverse).

### random

Generate an infinite stream of random numbers.

### take

Like UNIX ``head``, but takes a regex predicate to match against. If ``--while`` is used, it pipes input until a mismatch occurs. If ``--until`` occurs, it pipes input until a match occurs.

### trickle

Artificially cap the rate at which data moves through a shell pipe.

### range

Display the running range of a stream of numbers.

## Future ideas

### New commands

- `symbolic`: perform symbolic math on the input
- `reduce`: reduce the input with a given operator

### Improvements

- `range`: mirror summaries provided by R, providing running, standard devation and quartiles
