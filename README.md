# Google \# Hash Code 2018

Solutions and code for the [Google \# Hash Code 2018 Challenge](https://hashcode.withgoogle.com) of our Team _Gyrating Flibbittygibbitts_.

![HashCode 2018 Banner](HashCode2018.png)

> Hash Code is a team programming competition organized by Google for students
> and industry professionals across Europe, the Middle East and Africa.
> You pick your team and programming language, we pick a Google engineering 
> problem for you to solve.
>
> _from [\# Hash Code 2018](https://hashcode.withgoogle.com)_

## Final Round

The problem statement will be added once available.
Our solution is in the [Final Round folder](Final%20Round).

## Online Qualification Round

The problem statement will be added once available.
Our solution is in the [Online Qualification Round folder](Online%20Qualification%20Round).

## Practice Round

The problem statement can be found [here](Practice%20Round/pizza.pdf).
Our solution is in the [Practice Round folder](Practice%20Round).

> Did you know that at any given time, someone is cutting pizza somewhere around the world?
> The decision about how to cut the pizza sometimes is easy, but sometimes it’s ​really hard:
> you want just the right amount of tomatoes and mushrooms on each slice.
> If only there was a way to solve this problem using technology...
>
> _from [Practice Problem for Hash Code, Hash Code 2018](Practice%20Round/pizza.pdf)_

## Getting Started

### Prerequisites

The current version requires in particular the following libraries / versions.
See [requirements.txt](requirements.txt) for the full list of requirements.

The easiest way to install those dependencies is by using the [requirements.txt](requirements.txt) file with `pip3`.
```commandline
pip3 install -r requirements.txt
```

### Programming \/ *Solver* structure

The solutions are called from the `main.py` program of the corresponding round,
e.g. [Online Qualification Round/main.py](Online%20Qualification%20Round/main.py),
with the `--solver SOLVER` argument describing a solver in the
[solver](Online%20Qualification%20Round/solver) directory and
`input` being an input file from the
[input](Online%20Qualification%20Round/input) directory.

See the `help` below for more details.

```bash
$ python3 main.py -h
usage: main.py [-h] [--output OUTPUT] [--solver SOLVER] input

positional arguments:
  input            input file

optional arguments:
  -h, --help       show this help message and exit
  --output OUTPUT  output file
  --solver SOLVER
```

The `main.py` instantiates the solver with the input string, e.g.
`Solver(args.input)`.
Then the `solve()` method is invoked and in case an `--output` path is set,
the `write(args.output)` method is called with the given output string.

Therefor each solution/approach to a problem - let's call that a *solver* -
needs to inherit from the `class BaseSolver` in the `solver` directory of the
corresponding round (Final, Qualification, Practice).

The baseclass ensures, that the solver has a `__init__` method, which has `input_str` as an argument,
which is the the filepath of the given input.
This methods needs to take care of e.g. input parsing.

The `solve()` method solves the *problem* and holds the solution in memory.

The `write()` method writes a correct output file which can be submitted
online.

Together with the output file one can submit the corresponding solver file.  
Happy coding!

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

Sebastian Brodehl / [@sbrodehl](https://github.com/sbrodehl)  
Tobias Kremer / [@tbkr](https://github.com/tbkr)  
Dennis Meyer / [@snakebite1457](https://github.com/snakebite1457)  
Moritz Schmidtgen / [@mschmi10](https://github.com/mschmi10)

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details
