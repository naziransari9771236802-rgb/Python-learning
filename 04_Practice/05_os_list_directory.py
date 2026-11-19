import os

# Specify directory path
directory_path = "/"

# Get directory contents
contents = os.listdir(directory_path)

# Print directory contents
print("Directory Contents:")

for item in contents:
    print(item) 