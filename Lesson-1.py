import random

# Lists of story elements
characters = ['Alice', 'Bob', 'Charlie', 'Eve']
locations = ['forest', 'castle', 'beach', 'mountain']
actions = ['discovered', 'found', 'encountered', 'explored']
objects = ['treasure', 'magic potion', 'mysterious key', 'ancient artifact']

# Generate a random story
def generate_story():
    character = random.choice(characters)
    location = random.choice(locations)
    action = random.choice(actions)
    obj = random.choice(objects)

    story = f"Once upon a time, {character} embarked on an adventure to the {location}. "
    story += f"While exploring, {character} {action} a {obj}. "
    story += f"It shimmered in the sunlight, emitting an otherworldly glow. "
    story += f"Excitedly, {character} picked it up and continued the journey. "
    story += f"They couldn't wait to unravel the mysteries hidden within."

    return story

# Generate and print the story
story = generate_story()
print(story)