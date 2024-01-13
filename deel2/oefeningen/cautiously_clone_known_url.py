import subprocess


def clone_repo():
    # repo url
    url = "idk"
    # pad voor cloning
    clone_path = "E:\School\Python advanced\GitlabAutomatiseren\deel2/githubclone"

    print(f"Cloning repo van {url} naar {clone_path}")
    # check als de url bestaat
    try:
        # gitbuh clone command
        subprocess.run(["git", "clone", url,
                        clone_path], check=True)
        print("Repository clone succes!")
    except:
        print(f"Fout bij het klonen van de repository: {url}")


clone_repo()
