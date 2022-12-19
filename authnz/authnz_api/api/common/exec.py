import subprocess

def run_authnz_db(args):
    res = subprocess.run(args, capture_output=True)
    if res.returncode != 0:
        raise Exception("command '%s' failed: return code '%i', stdout '%s', stderr '%s'" % (args, res.returncode, res.stdout, res.stderr))
        return None
    return res
