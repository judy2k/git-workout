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

    dt = "2005-04-07T14:13:13"
    clone.index.add([str(file_path)])
    clone.index.commit(
        "This is the first commit.", author_date=dt, commit_date=dt
    )

    file_path.write_text(
        """
This is the start of a great file.

And now we should push.
""".lstrip()
    )

    dt = "2005-04-07T15:13:13"
    clone.index.add([str(file_path)])
    clone.index.commit(
        "This is the second commit.", author_date=dt, commit_date=dt
    )

    clone.remotes[0].push()

    #
    # Local-only commits: ----------------------------------------------------
    #

    file_path.write_text(
        """
This is the start of a great file.

Here's a bit more.
""".lstrip()
    )

    dt = "2005-04-07T16:13:13"
    clone.index.add([str(file_path)])
    # We'll tag this one
    commit = clone.index.commit(
        "This is the third commit.", author_date=dt, commit_date=dt
    )
    c = clone.create_tag("a-tag", commit)
    print("Just tagged:", c)

    file_path.write_text(
        """
I've basically decided to start again.
""".lstrip()
    )

    dt = "2005-04-08T13:13:13"
    clone.index.add([str(file_path)])
    clone.index.commit(
        "This is the fourth commit.", author_date=dt, commit_date=dt
    )

    file_path.write_text(
        """
I've basically decided to start again.
This is one day going to be great.
""".lstrip()
    )

    dt = "2005-04-08T14:13:13"
    clone.index.add([str(file_path)])
    clone.index.commit(
        "This is the fifth commit.", author_date=dt, commit_date=dt
    )

    file_path.write_text(
        """
Okay, this is done now.
""".lstrip()
    )

    dt = "2005-04-08T15:13:13"
    clone.index.add([str(file_path)])
    clone.index.commit(
        "This is the sixth commit.", author_date=dt, commit_date=dt
    )

    return clone
