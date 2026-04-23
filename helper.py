import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend to avoid conflict with pygame on macOS
import matplotlib.pyplot as plt

plt.ion()

def plot(scores, mean_scores):
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.savefig('training_plot.png')  # Save plot to file instead of displaying