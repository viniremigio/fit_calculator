# Fit Calculator

A gist of how you can calculate the amount of calories per day you should eat in order to **gain**, 
**lose** or **maintain** your weight!

## How to run

```
python -m fitapp <weight> <height> <age> <goal: lose|gain|maitain>
```

or if you want to run with **Docker**:

```
docker build -t fitapp:test .
docker run fitapp:test
```

## TODO
- Save locally metrics **[OK]**
- Docker Container **[OK]**
- Unit tests support **[OK]**
- Pass parameters with argparse