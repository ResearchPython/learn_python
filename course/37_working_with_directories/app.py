from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft
# /usr/local
# Relative path

path = Path("../1_variables")
print(path.exists())

path = Path("wtf")
print(path.mkdir())
print(path.rmdir())

path = Path()
for file in path.glob('../*'):
    print(file)
