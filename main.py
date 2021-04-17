
import subprocess
import os
import stat
st = os.stat('glove/glove.sh')
os.chmod('glove/glove.sh', st.st_mode | stat.S_IEXEC)
cmd = ["./glove.sh", "var_um", "var_dois", "var_tres", "var_quatro", "var_cinco", "var_seis"]
treinar_glove = subprocess.Popen(cmd,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='glove')
output, errors = treinar_glove.communicate()
treinar_glove.wait()
print('output:')
print(output.decode('utf-8'))
print('errors:')
print(errors.decode('utf-8'))