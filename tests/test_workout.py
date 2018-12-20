import workout

from git import Repo


def test_workout():
    assert workout.main is not None


def test_repo_fixture(temp_repo):
    assert isinstance(temp_repo, Repo)
    assert len(list(temp_repo.iter_commits())) == 6
    for c in temp_repo.iter_commits("@{push}.."):
        print(c.committed_datetime, c.hexsha[:7], c.message)
    print(temp_repo.tags)
    print(temp_repo.tags["a-tag"].commit.hexsha[:7])
    assert False
