import subprocess
from pathlib import Path

if __name__ == '__main__':
    path = Path(__file__)
    dir_path = path.parent.resolve()
    text_path = dir_path / 'text.txt'
    config_path = dir_path / 'config.yml'
    exec_path = dir_path.parent.parent / 'hercules-extraction.py'

    out_path = dir_path / 'translation_extraction_export_sample.ttl'

    cp = subprocess.run(['python', str(exec_path), '--file', str(text_path), '--config', str(config_path), '--out', str(out_path)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    print('stdout:')
    print(cp.stdout)
    print('stderr:')
    print(cp.stderr)
