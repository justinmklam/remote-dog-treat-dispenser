# Remote Dog Treat Dispenser

## Installation

```bash
sudo apt install authbind

# Configure access to port 80
sudo touch /etc/authbind/byport/80
sudo chmod 777 /etc/authbind/byport/80
```

Launch the web app:

```bash
authbind --deep python3 app.py
```

Remote port forward to [serveo.net](http://serveo.net/):

```bash
 ssh -R treats-for-nala:80:localhost:80 serveo.net
# Forwarding HTTP traffic from https://treats-for-nala.serveo.net
# Press g to start a GUI session and ctrl-c to quit.
 ```

## Development

Create `app/.env` and add the following contents to run the app with mocked hardware dependencies:

```bash
export FLASK_DEBUG=true
export MOCK=true
export CAMERA=opencv
```
