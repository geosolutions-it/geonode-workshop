# Geonode Workshop
A minimal [GeoNode 4.2.0 Project](https://github.com/GeoNode/geonode-project/tree/master), for educational purposes and local testing.

[Install Docker](https://docs.docker.com/engine/install/) for your OS, then just run:
```bash
git clone https://github.com/geosolutions-it/geonode-workshop.git
cd geonode-workshop
docker compose build
docker compose up -d
```

:tea: Take a cup of tea, and relax. The build and startup will take some time.

:clock1: In a few minutes your local GeoNode will be visible at [http://localhost](http://localhost)

:+1: Login with `admin:geonode`

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