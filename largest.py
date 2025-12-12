images =[
    ("G:/cartoon_kid_.png",1920,1080),
    ("G:/beautiful-flowers-rose.jpg",1280,1080),
    ("G:/dog.jpeg",2000,1080)
    ]
areas =[(name,w,h,w*h)for name,w,h in images]

largest = max(areas,key=lambda x:x[3])
smallest =min(areas, key=lambda x:x[3])

print("Largest:", largest)
print("Smallest:", smallest)

