from pathlib import Path

p = Path('.')

# Listing subdirectories
sub_dirs = [x for x in p.iterdir() if x.is_dir()]
print(sub_dirs)

# Listing Python files recursively
print(list(p.glob('**/*.py')))

# Navigating inside a directory tree
p = Path('/etc')
q = p / 'init.d' / 'rsync'
print(q)
print(q.resolve())

# Querying path properties
print(q.exists())
print(q.is_dir())
