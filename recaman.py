from matplotlib.patches import Arc
import matplotlib.pyplot as plt

def generate_recaman_sequence(final_number):
    '''generate the recaman sequence'''
    counter = 0
    position = 0
    result = []
    while (position <= final_number):
        if (position-counter <= 0 or position-counter in result):
            position = counter + position
        else:
            position -= counter
        result.append(position)
        counter += 1
    print(result)
    return result

def plot_recaman_sequence(sequence):

    fig, ax = plt.subplots(figsize=(1, 1))

    size = 1

    for _ in sequence:
        if (sequence[size] < final_number):
            p = (sequence[size-1]+sequence[size])/2
            if size % 2 == 0:
                t1 = 0
                t2 = 180
            else:
                t1 = -180
                t2 = 0
            c = Arc((p, 0), size, size, theta1=t1, theta2=t2, lw=1.5)
            size += 1
            ax.add_artist(c)

    plt.xlim([0, max(sequence)+1])
    plt.ylim([-size, size])
    ax.set_aspect('equal',)
    plt.show()

if __name__ == "__main__":
    
    final_number = 90
    plot_recaman_sequence(generate_recaman_sequence(final_number))
