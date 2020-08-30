import subprocess
import shlex


def cmd_lst(*args):
    return ['multipass', ] + list(filter(bool, args))


def delete(name, purge=True):
    """
    this purges the instance immediately by default
    :param name:
    :param purge:
    :return:
    """

    return subprocess.check_output(cmd_lst('delete', '--purge' if purge else '', shlex.quote(name)))


def launch(name, image=None, cpus='1', mem='512m', disk='5G'):
    return subprocess.check_output(cmd_lst('launch', '--name', shlex.quote(name),
                                           '--cpus', shlex.quote(str(cpus)), '--mem', shlex.quote(str(mem)),
                                           '--disk', shlex.quote(str(disk)),
                                           image))


def exec(name, cmd):
    return subprocess.check_output(cmd_lst('exec', shlex.quote(name), *cmd))
