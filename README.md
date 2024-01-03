# PokeBerries
API to get pokeberries information.

## Overview

This API looks for information regarding PokeBerries and growth times, then process the times to calculate additional information, including:
* Min / Max values
* Mean
* Median
* Variance
* Frequencies for each growth value

Additionally, it returns a with the names of each berry.

Another feature is that it can show an histogram showing this last set of values (frquencies).

## Endpoints

### /
Shows a short explanation of the two following endpoints.

### /allBerryStats
Gathers information from all the poke berries and returns a json with the every berry name and some statistical data calculated from the growth time values.

### /growthTimesHistogram
Generates an histogram with the growth time values of every berry.


## Getting Started

### Installation

Clone the repository locally:
```git
'git clone https://github.com/ilotrob/PokeBerries.git'
```

Then, on the root directory, run the command:
```python
'python -m pip install -r requirements.txt'
```

### Running the application
From the root directory, run the following command:
```python
'python -m app'
```


### Execute unit-tests
From the root directory, and with the application running, execute the following command:
```python
'python -m pytest'
```