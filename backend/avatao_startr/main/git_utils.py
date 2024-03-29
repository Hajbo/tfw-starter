from git import Repo


def _add_and_commit(repo, message, author_name, author_email) -> None:
    repo.git.add("--all")
    repo.git.commit("-m", message, author=f"{author_name} <{author_email}>")


def init_starter_repo(path, user_name, user_email) -> None:
    repo = Repo.init(path, mkdir=False)

    with repo.config_writer() as config:
        config.set_value("user", "name", user_name)
        config.set_value("user", "email", user_email)

    _add_and_commit(repo, "TFW starter initialized", user_name, user_email)
