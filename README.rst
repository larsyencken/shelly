=====================================
Shelly: shell tools for data analysis
=====================================

Commands
========

drop
----

Like UNIX ``tail``, but takes a regex predicate to match against. Silently
drops lines from the input until the desired condition is reached.

take
----

Like UNIX ``head``, but takes a regex predicate to match against. If
``--while`` is used, it pipes input until a mismatch occurs. If ``--until``
occurs, it pipes input until a match occurs.

random
------

Generate an infinite stream of random variables.

trickle
-------

Speed-control over a shell pipe.

Cool ideas
==========

- symbolic: perform symbolic math on the input
- reduce: reduce the input with a given operator
