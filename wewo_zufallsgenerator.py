import random

# Define the list of names
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivan", "Jack", "Katie", "Liam", "Mia", "Nathan", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tina", "Ursula", "Victor", "Wendy", "Xavier", "Yvonne", "Zach"]

# Define dependencies: keys can only be picked if the corresponding value has been picked.
# For example, "Charlie" can only be picked if "Alice" is picked.
dependencies = {
    "Alice": "Charlie",
    "Charlie": "Alice",
    "David": "Bob",
    "Bob": "David",
    "Grace": "Eve",
    "Eve": "Grace"
}

def pick_names(names, dependencies, N, couple_probability=0.5):
    # Initialize an empty set to store the selected names
    selected_names = set()

    while len(selected_names) < N:
        # Pick a random name from the list
        name = random.choice(names)
        
        # Check if the name has a dependency
        if name in dependencies:
            
            # Randomly decide whether to add the dependent name
            if random.random() < couple_probability:
                
                # If the dependent name is not in the selected names, add it first
                if dependencies[name] not in selected_names:
                    selected_names.add(dependencies[name])

                # Add the randomly chosen name to the selected names
                selected_names.add(name)
            else:
                
                # Skip this name and continue to the next iteration
                continue
        else:
            # If the name has no dependencies, simply add it to the selected names
            selected_names.add(name)
    
    return list(selected_names)

# Test the function with N=5
N = 10
couple_probability = 0.5 # 0: never allow couples, 1: always allow couples, 0.5: allow couples with 50% probability
picked_names = pick_names(names, dependencies, N, couple_probability)
print("Randomly picked names:", picked_names)

# TESTING THE SELECTION FREQUENCY
import matplotlib.pyplot as plt
M = 100000
fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(15, 15))
ax = ax.flatten()
for i, couple_probability in enumerate([0, 0.25, 0.5, 0.75, 1]):
    print(i, couple_probability)
    results = []
    for _ in range(M):
        picked_names = pick_names(names, dependencies, N, couple_probability)
        results.extend(picked_names)
    name_counts = {name: results.count(name) for name in names}
    ax[i].hist(name_counts, bins=len(names), density=True, weights=[v for v in name_counts.values()], alpha=1, color="C" + str(i))
    ax[i].set_title(f"Doppelpack-Wahrscheinlichkeit = {couple_probability}")
    ax[i].set_xlabel("Names")
    ax[i].set_xticklabels(names, rotation=45)
    
fig.tight_layout()
fig.savefig("selection_frequency.pdf")
