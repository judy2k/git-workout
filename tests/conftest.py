from pathlib import Path

from pytest import fixture

from git import Repo


@fixture()
def temp_repo(tmp_path: Path):
    origin_path = tmp_path / "origin"
    clone_path = tmp_path / "clone"
    file_path = clone_path / "the_file.txt"

    origin = Repo.init(str(origin_path), bare=True)
    clone = origin.clone(clone_path)
    file_path.write_text(
        """
This is the start of a great file.
""".lstrip()
    )
    clone.index.add([str(file_path)])
    clone.index.commit("This is the first commit.")
    return clone
