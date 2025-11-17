podman run --name matplotlib.python --rm -dit python /bin/bash -c "sleep inf"
podman exec -it matplotlib.python /bin/bash -c "adduser --disabled-password matplotlib"
podman exec -itu matplotlib matplotlib.python /bin/bash -c "cd /home/matplotlib && pip install matplotlib"
podman cp ./01.py matplotlib.python:/home/matplotlib/01.py
podman exec -it matplotlib.python /bin/bash -c "chown matplotlib:matplotlib /home/matplotlib/01.py"
podman exec -itu matplotlib matplotlib.python /bin/bash -c "cd /home/matplotlib && python ./01.py"
podman cp matplotlib.python:/home/matplotlib/function_plot.png function_plot.png
podman stop matplotlib.python
imv ./function_plot.png
