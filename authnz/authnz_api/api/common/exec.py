import subprocess

def run_authnz_db(args):
    res = subprocess.run(args, capture_output=True)
    if res.returncode != 0 or len(res.stdout) < 1:
        raise Exception("command '%s' failed: return code '%i'" % (args, res.returncode))
        return None
    return res
