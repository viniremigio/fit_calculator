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
docker run fitapp:test --weight 90 --height 176 --age 35 --goal lose
```

### Expected Output:
```
INFO:root:Input: Weight = 90.0kg | Height = 176cm | Age = 35 | Goal = lose
INFO:root:Output: TMB = 1830.0 kcal | TotalCalPerDay = 2836.0 kcal | TotalMaintenance_Lose = 2268.8 kcal
INFO:root:Calories: Protein = 900.0 kcal | Fat = 648.0 | Carbo = 720.8 kcal
INFO:root:Protein = 225.0 g | Fat = 72.0 g | Carbo = 180.0 g
```

## TODO
- Save locally metrics **[OK]**
- Docker Container **[OK]**
- Unit tests support **[OK]**
- Pass parameters with argparse **[OK]**