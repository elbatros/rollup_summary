### How do I get set up? ###
clone the repository it has everything setup with virtual environment
```
	cd rollup_summary
	source venv/bin/activate
	python summary.py
	python summary.py y m d
	python summary.py y m
	python summary.py y
```	
# README #

Summarizing the data helps
us understand it and see patterns. A common summary is the ROLLUP summary,
which aggregates a table of data by grouping on every prefix of the list of
dimensional columns.

For example, if you had some sales data like:
```
y m d value
2016 3 28 100
2016 3 29 123
2016 3 30 50
2016 4 1 50
. . . rolling up the value column by summing it over the y, m and d columns
would give you:
y m d value
2016 3 28 100
2016 3 29 123
2016 3 30 50
2016 3 273
2016 4 1 50
2016 4 50
2016 323
323
```

Please use the input.txt file to change the input for the program
