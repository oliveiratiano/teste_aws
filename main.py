
import subprocess
cmd = ["./demo.sh", "varum", "vardois"]
treinar_glove = subprocess.Popen(cmd,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="glove")
output, errors = treinar_glove.communicate()
print(output)
print(errors)
import pdb; pdb.set_trace()
treinar_glove.wait()
