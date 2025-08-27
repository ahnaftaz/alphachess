"""
Configuration for our entire model and training of AlphaZero.
"""

class Config:
    """Basic configuration for AlphaZero training."""
    
    def __init__(self):
        # Game settings
        self.board_size = (6, 7)  # Connect Four: 6 rows x 7 columns
        self.num_actions = 7  # 7 possible columns to drop pieces
        
        # Network settings
        self.learning_rate = 3e-4  # How fast networks learn (0.0003). Lower = more stable but slower
        self.batch_size = 32  # Number of training examples processed at once. Higher = more stable gradients
        
        # MCTS settings  
        self.num_simulations = 10  # MCTS tree searches per move. More = stronger play but slower
        self.c_puct = 1.0  # Exploration vs exploitation balance. Higher = more exploration of new moves
        
        # Training settings
        self.num_iterations = 100  # Main training loops. Each iteration = self-play + network training
        self.games_per_iteration = 10  # Self-play games generated per iteration for training data
        
        # TODO: Add more configuration options as needed