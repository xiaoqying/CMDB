
import os,django
from django.contrib.auth.hashers import make_password, check_password
import hashlib
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CMDB.settings")
ps = "yingzizhu"
#
dj_ps = make_password(ps,'pbkdf2_sha256')
print(dj_ps)
# ch=check_password(121212,dj_ps)
# print(ch)
# hash = hashlib.md5()
# hash.update(ps.encode())
# print(hash)
# print(hash.hexdigest())
a = 'pbkdf2_sha256$36000$pbkdf2_sha256$s4TuGb3Kh7/is56FZPqgFA9/+/u1/JmGrzOjgiTMLZ8='