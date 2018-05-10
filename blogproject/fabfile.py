from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/0xiamu/blogproject.git"

env.user = 'xiamu'
env.password = 'hlqawxy'
env.hosts = ['120.79.208.180']
env.port = '22'


def deploy():
    source_folder = '/home/xiamu/sites/natsumexyz/blogproject/blogproject'

    run('cd %s && git pull' % source_folder)
    run('''
        cd {} &&
        ../../env/bin/pip install -r requirements.txt &&
        ../../env/bin/python3 manage.py collectstatic --noinput &&
        ../../env/bin/python3 manage.py migrate
        '''.format(source_folder))
    sudo('systemctl restart gunicornxyz')
    sudo('service nginx reload')