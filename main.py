
import subprocess
import os
import stat
st = os.stat('glove/demo.sh')
os.chmod('glove/demo.sh', st.st_mode | stat.S_IEXEC)
cmd = ["./demo.sh"]
treinar_glove = subprocess.Popen(cmd,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='glove')
output, errors = treinar_glove.communicate()
print(output)
print(errors)
treinar_glove.wait()
print(output)
print(errors)