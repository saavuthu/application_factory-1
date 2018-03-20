import subprocess
import falcon


class AnsibleResource(object):
    def run_command(self, command):
        p = subprocess.Popen(command,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return iter(p.stdout.readline, b'')

    def update_hostentry(self, host_add):
        f = open('hosts','w')
        f.write(host_add)
        f.close()

    def run_ansible(self, host_ip,application_file):
        self.update_hostentry(host_ip)
        command = 'ansible-playbook -i hosts apps/'+application_file+' -u cloud'
        command = command.split()
        result = []
        for t in run_command(command): result.append(t)
        return result

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('html/index.html', 'r') as f:
            resp.body = f.read()

app = falcon.API()
app.add_route('/', AnsibleResource())
# print  run_ansible('84.39.39.130', 'tomcat.yml')
