# Geonode Workshop
A minimal [GeoNode 5 Project](https://github.com/GeoNode/geonode-project/tree/master), for educational purposes and local testing.

[Install Docker](https://docs.docker.com/engine/install/) for your OS, then just run:
```bash
git clone https://github.com/geosolutions-it/geonode-workshop.git
cd geonode-workshop
python3 create-envfile.py
docker compose build
docker compose up -d
```

:tea: Take a cup of tea, and relax. The build and startup will take some time.

:clock1: In a few minutes your local GeoNode will be visible at [http://localhost](http://localhost)

:+1: The login access will be printed inside the .env file under `ADMIN_USERNAME` and `ADMIN_PASSWORD`

## Custom Setup

 * You can adapt the `.env` file if you want to change the default secrets and configuration.
 * You can also re-generate the `.env` file thrugh the `create-envfile.py` script

    `create-envfile.py` accepts the following arguments:

    - `--https`: Enable SSL. It's disabled by default
    - `--env_type`: 
    - When set to `prod` `DEBUG` is disabled and the creation of a valid `SSL` is requested to Letsencrypt's ACME server
    - When set to `test`  `DEBUG` is disabled and a test `SSL` certificate is generated for local testing
    - When set to `dev`  `DEBUG` is enabled and no `SSL` certificate is generated
    - `--hostname`: The URL that whill serve GeoNode (`localhost` by default)
    - `--email`: The administrator's email. Notice that a real email and a valid SMPT configurations are required if  `--env_type` is seto to `prod`. Letsencrypt uses to email for issuing the SSL certificate 
    - `--geonodepwd`: GeoNode's administrator password. A random value is set if left empty
    - `--geoserverpwd`: GeoNode's administrator password. A random value is set if left empty
    - `--pgpwd`: PostgreSQL's administrator password. A random value is set if left empty
    - `--dbpwd`: GeoNode DB user role's password. A random value is set if left empty
    - `--geodbpwd`: GeoNode data DB user role's password. A random value is set if left empty
    - `--clientid`: Client id of Geoserver's GeoNode Oauth2 client. A random value is set if left empty
    - `--clientsecret`: Client secret of Geoserver's GeoNode Oauth2 client. A random value is set if left empty

Example USAGE

```bash
python create-envfile.py -f /opt/core/geonode-project/file.json \
--hostname localhost \
--https \
--email random@email.com \
--geonodepwd gn_password \
--geoserverpwd gs_password \
--pgpwd pg_password \
--dbpwd db_password \
--geodbpwd _db_password \
--clientid 12345 \
--clientsecret abc123 
```

Example JSON expected:

```JSON
{
"hostname": "value",
"https": "value",
"email": "value",
"geonodepwd": "value",
"geoserverpwd": "value",
"pgpwd": "value",
"dbpwd": "value",
"geodbpwd": "value",
"clientid": "value",
"clientsecret": "value"
} 
```

## Install project for development

Is also possible to start the project in development mode using the [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers).

In the project inside the `.devcontainer` folder there is a `generate.py` file. This file allow the developer to create all the files required to run the project in development mode.

Steps to generate the project for development:

1) Generate the .env file as described in the [Custom Setup](https://github.com/geosolutions-it/geonode-workshop#custom-setup)
2) Enter in the `.devcontainer` folder
3) Run the `generate.py` file by specifying the project name. In this example the project name should be `geonode_project` 
```
cd .devcontainer
python3 generate.py geonode_project
```
4) The script will generate a different files and it should look like the following tree

```
(geonode) ➜  geonode-workshop git:(main) ✗ tree .devcontainer 
.devcontainer
├── .env
├── .vscode/
├────── launch.json
├── devcontainer.json
├── docker-compose.yml
├── docker.sh
└── generate.py
```

5) Use the docker.sh to run the containers `./docker.sh up -d --build`
6) After the build, use the devcontainers utils to enter in the django container `SHIFT + CTRL + P` and click on `Reopen in container`
7) Automatically the system will recognize the `launch.json` file to run the django application and therefore GeoNode