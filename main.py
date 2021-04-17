
import subprocess
import os
import stat
st = os.stat('teste.sh')
os.chmod('teste.sh', st.st_mode | stat.S_IEXEC)
cmd = ["bash", "./teste.sh", "AQUI", "ALI"]
treinar_glove = subprocess.Popen(cmd,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, errors = treinar_glove.communicate()
print(output)
print(errors)
treinar_glove.wait()
