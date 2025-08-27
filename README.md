# AlphaZero Connect Four

AlphaZero implementation for Connect Four using Monte Carlo Tree Search and neural networks.

## Project Structure

```
src/
├── main.py            # Main entry point and orchestration
├── config.py          # Configuration settings
├── alphazero_model.py # Combined model (policy + value heads) as in original AlphaZero
├── mcts.py            # Monte Carlo Tree Search implementation
└── trainer.py         # Training loop coordination
```

## Getting Started

1. Install dependencies:
```bash
uv sync
```

2. Run the demo script:
```bash
uv run src/main.py
```

## Implementation Status

This project currently contains **stub files only**. Each component needs to be implemented:

- AlphaZeroModel - Combined model/ agent with policy and value heads
- MCTS - Tree search algorithm implementation
- AlphaZeroTrainer - Self-play and training coordination

## Dependencies

- pettingzoo[classic] - Connect Four environment
- torch - Neural networks (when implemented)  
- numpy - Array operations (when needed)
- tqdm - Progress bars (when needed)