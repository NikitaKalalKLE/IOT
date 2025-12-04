
images = [
    ("C:/Users/student/Downloads/dog.jfif", 1920, 1080),
    ("C:/Users/student/Downloads/flower.jfif", 1280, 720),
    ("C:/Users/student/Downloads/greenery.jfif", 3000, 2000)
]

areas = [(name, w, h, w*h) for name, w, h in images]

largest = max(areas, key=lambda x: x[3])
smallest = min(areas, key=lambda x: x[3])

print("Largest:", largest)
print("Smallest:", smallest)
