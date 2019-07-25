# a b init都会执行
from src.pkg.a import b

b.hello()

from src.pkg import a

print(a.os.getcwd())
