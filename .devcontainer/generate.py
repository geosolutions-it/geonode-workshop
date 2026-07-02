import os
import argparse
import jinja2
import shutil
from pathlib import Path

jenv = jinja2.Environment()

launch_template = jenv.from_string(
"""
{
    "version": "0.2.0",
    "configurations": [
        
        {
            "name": "Python Debugger: Django",
            "type": "debugpy",
            "request": "launch",
            "args": [
                "runserver",
                "0.0.0.0:8000"
            ],
            "django": true,
            "autoStartBrowser": false,
            "program": "/usr/src/{{project}}/manage.py"
        }
    ]
}
"""
)

workspace_template = jenv.from_string(
"""
{
	"folders": [
		{
			"path": ".."
		},
		{
			"path": "../../local/lib/python3.10/dist-packages"
		}
	],
	"settings": {}
}
"""
)

devcontainer_template = jenv.from_string(
"""
// For format details, see https://aka.ms/devcontainer.json. For config options, see the README at:
// https://github.com/microsoft/vscode-dev-containers/tree/v0.194.0/containers/docker-existing-docker-compose
// If you want to run as a non-root user in the container, see .devcontainer/docker-compose.yml.
{
	"name": "Debug Docker Compose",

	// Update the 'dockerComposeFile' list if you have more compose files or use different names.
	// The .devcontainer/docker-compose.yml file contains any overrides you need/want to make.
	"dockerComposeFile": [
		"../docker-compose.yml",
		"docker-compose.yml"
	],

	// The 'service' property is the name of the service for the container that VS Code should
	// use. Update this value and .devcontainer/docker-compose.yml to the real service name.
	"service": "django",

	// The optional 'workspaceFolder' property is the path VS Code should open by default when
	// connected. This is typically a file mount in .devcontainer/docker-compose.yml
	"workspaceFolder": "/usr/src",

	// Set *default* container specific settings.json values on container create.
    "customizations": {
        "vscode": {
            "settings": {
                "terminal.integrated.profiles.linux": {
                    "/bin/bash": {
                        "path": "/bin/bash",
                        "args": [
                            "-l"
                        ]
                    }
                },
                "terminal.integrated.defaultProfile.linux": "bash"
            },

            // Add the IDs of extensions you want installed when the container is created.
            "extensions": [
                "ms-python.python",
                "batisteo.vscode-django",
                "mrorz.language-gettext",
                "eamodio.gitlens", // Note: User preference
                "bigonesystems.django" // Note: User preference
            ]
        }
    },

	// Use 'forwardPorts' to make a list of ports inside the container available locally.
	"forwardPorts": [
		8000,
		8080,
		5432,
		5678
	],

	// Uncomment the next line if you want start specific services in your Docker Compose config.
	// "runServices": [],

	// Uncomment the next line if you want to keep your containers running after VS Code shuts down.
	// "shutdownAction": "none",

	// Uncomment the next line to run commands after the container is created - for example installing curl.
	// "postCreateCommand": "apt-get update && apt-get install -y curl",

	// Uncomment to connect as a non-root user if you've added one. See https://aka.ms/vscode-remote/containers/non-root.
	// "remoteUser": "vscode"
}
"""
)

docker_compose_template = jenv.from_string(
"""
services:

  django:
    ports:
      - "8000:8000"
    volumes:
    - './src:/usr/src/${COMPOSE_PROJECT_NAME}'
    - './.devcontainer/.vscode:/usr/src/.vscode'
    - statics:/mnt/volumes/statics
    - geoserver-data-dir:/geoserver_data/data
    - backup-restore:/backup_restore
    - data:/data
    - tmp:/tmp
    healthcheck:
      test: "echo 'Alive'"
    entrypoint: ["/usr/src/${COMPOSE_PROJECT_NAME}/entrypoint.sh"]
    command: sleep infinity
"""
)

docker_sh_template = jenv.from_string(
"""
docker compose -f ../docker-compose.yml -f docker-compose.yml "$@"
"""
)

def render(project):
    Path(".vscode").mkdir(exist_ok=True)
    with open(".vscode/launch.json","w") as fout:
        fout.write(launch_template.render(project=project))
    with open(".vscode/src.code-workspace.json","w") as fout:
        fout.write(workspace_template.render(project=project))
    with open("devcontainer.json","w") as fout:
        fout.write(devcontainer_template.render(project=project))
    with open("docker-compose.yml","w") as fout:
        fout.write(docker_compose_template.render(project=project))
    with open("docker.sh","w") as fout:
        fout.write(docker_sh_template.render())
    
    os.chmod("docker.sh", 0o755)

    env_file_src = Path("../.env")
    env_file_dst = Path("./.env")
    generate_env = True
    if env_file_dst.exists():
        generate_env = False
        res = input("There's already an .env file. Do you want to overwrite it? (y/n))")
        if "y" in res.lower():
            generate_env = True
    if generate_env:
        if env_file_src.exists():
            shutil.copyfile(env_file_src, env_file_dst)
        else:
            print("I couldn't find an .env file inside the root folder of the project. Plesae create one with create_envfile.py")



if __name__=="__main__":
    parser = argparse.ArgumentParser(
                    prog='Devcontainer generator for GeoNode',
                    description='Generate a VS Code devcontainer configuration to develop GeoNode with Docker')
    parser.add_argument('project', help="Project's module (ex. geonode_demo)")

    args = parser.parse_args()
    render(args.project)