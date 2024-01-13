import subprocess


def clone_repo():
    # repo url
    url = "https://github.com/AP-IT-GH/projectopdracht-canuski.git"
    # pad voor cloning
    clone_path = "E:\School\Python advanced\GitlabAutomatiseren\deel2/githubclone"

    print(f"Cloning repo van {url} naar {clone_path}")

    # gitbuh clone command
    subprocess.run(["git", "clone", url,
                    clone_path], check=True)
    print("Repository clone succes!")


clone_repo()
