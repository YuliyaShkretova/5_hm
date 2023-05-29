from pathlib import Path

import resources


def image(file_name):
    return str(
        Path(resources.__file__).parent.joinpath(file_name).absolute()
    )


