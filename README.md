# snake-game-ai

reinforcement learning agent that learns to play snake using deep q-learning.

## how it works

- the agent sees 11 features: danger (straight/left/right), current direction, and food location
- uses a simple neural net (11 → 256 → 3) to pick between going straight, turning right, or turning left
- trains with experience replay (100k memory buffer) and epsilon-greedy exploration
- epsilon decays over the first 80 games, then the agent relies on what it learned

## stack

- python, pytorch, pygame, numpy, matplotlib

## setup

```
python -m venv venv
source venv/bin/activate
pip install torch pygame numpy matplotlib
```

## run

```
python agent.py
```

training progress saves to `training_plot.png`. best model saves to `model/model.pth`.
