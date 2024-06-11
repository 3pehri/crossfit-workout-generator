import random

exercises = ["Push-ups", "Pull-ups", "Squats", "Deadlifts", "Burpees", "Lunges"]
sets = random.randint(3, 5)
reps = random.randint(10, 20)

print("Today's CrossFit workout:")
for _ in range(sets):
    exercise = random.choice(exercises)
    print(f"{reps} reps of {exercise}")
