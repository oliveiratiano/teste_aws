
import subprocess
cmd = ["(cd glove && ./demo.sh)"]
treinar_glove = subprocess.Popen(cmd,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, errors = treinar_glove.communicate()
treinar_glove.wait()
print(output)
print(errors)