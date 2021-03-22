import os
import subprocess


def generate(text, filename):
    return _generate_demo(text, filename)


def _generate_demo(text, filename):
    """This function uses the demo Tacotron 2 persian trained by @hamedhemati to generate speech from text

    Args:
        text (str): the input text. should be normalized
        filename (str): the filename (without extension) to save the output speech in
    """
    # configs
    tacotron_path = 'Tacotron-2-Persian'
    script_path = f'scripts/persian_commonvoice_demo/generate.sh'
    output_path = "../outputs"
    lang = 'fa'

    # we should call a subprocess to run.
    # TODO: create a callable python function instead of calling a subprocess
    command = [script_path, text, filename, output_path]
    print(' '.join(command))
    print(subprocess.run(command, cwd=tacotron_path))