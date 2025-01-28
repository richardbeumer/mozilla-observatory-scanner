# Mozilla Observatory Scanner

Scanner to scan a list of endpoints with [Mozilla Observatory](https://observatory.mozilla.org/)

## Run local

To run loccaly perform the following steps
1. Create Python virtual environment and install the requirements in it.
```
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

2. Set variables:

```
export SITES='["sites", "to", "scan"]'
export SLACK_WEBHOOK=<your-slack-webhook>
```

3. Run the code:
```
cd src
python scanner.py
```

## DevContainer

You can also run from a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers)

1. Start the devContainer. 
```
vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=<url-of-this-forked-repo>
```

2. Set variables:
```
export SITES=["sites", "to", "scan"]
export SLACK_WEBHOOK=<your-slack-webhook>
```

3. Run the code from a terminal in the container.
```
cd src
python scanner.py
```
