
import subprocess
cmd = ["./src/teste.sh"]
treinar_glove = subprocess.Popen(cmd,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="glove")
output, errors = treinar_glove.communicate()
print(output)
print(errors)
treinar_glove.wait()
