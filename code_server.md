
fix google cloud key

    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - \
    && sudo apt update -y \
    && sudo apt upgrade -y

````bash
wget https://nodejs.org/dist/v14.17.6/node-v14.17.6-linux-armv7l.tar.xz \
&& tar -xf node-v14.17.6-linux-armv7l.tar.xz \
&& cd node-v14.17.6-linux-armv7l/ && sudo cp -R * /usr/local/ \
&& node -v && npm -v \
&& sudo npm install --global yarn \
&& curl -fsSL https://code-server.dev/install.sh | sh \
&& sudo mkdir /home/pi/.config/code-server
```` 

    sudo nano /home/pi/.config/code-server/config.yaml

Add the following to your config file:

````
---
bind-addr: 0.0.0.0:8080
auth: password
password: 1234567890
cert: false
````

Get code server path

    yarn global bin

Let's configure it as a service which will start when the Pi boots so that you don't always have to do it manually.

    sudo nano /lib/systemd/system/code-server.service

Add the following to the service file:

````
[Unit]
Description=code-server
After=network.target

[Service]
Type=simple
Environment=PASSWORD=1234567890
ExecStart=/home/pi/.yarn/bin/code-server --bind-addr 0.0.0.0:8080 --user-data-dir /var/lib/code-server --auth password
Restart=always

[Install]
WantedBy=multi-user.target
````

````bash
sudo mkdir /var/lib/code-server && sudo systemctl daemon-reload && sudo systemctl start code-server && sudo systemctl enable code-server
````

Get status

    sudo systemctl status code-server

To stop the service manually:

    sudo systemctl stop code-server

To set opencv to the root python3
    
    # Optional
    sudo cp /usr/local/lib/python3.7/site-packages/cv2/python-3.7/cv2.py3cv4.1.1.so /usr/local/lib/python3.7/site-packages/cv2/python-3.7/cv2.so    
    
    # Add cv2 to root packages
    sudo cp -r /usr/local/lib/python3.7/site-packages/cv2 /usr/local/lib/python3.7/dist-packages/

Update pip

    /usr/bin/python3 -m pip install --upgrade pip

Set python3 to python and append pythonpath

    sudo nano /root/.bashrc

Add this lines

    alias python=python3
    export PYTHONPATH="${PYTHONPATH}:/home/pi/home_of_pi"

Then update changes

    source /root/.bashrc