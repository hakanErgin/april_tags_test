FROM jjanzic/docker-python3-opencv:opencv-4.0.0

# ENV PYTHONUNBUFFERED 1
# ENV PYTHONPATH "${PYTHONPATH}:/app"

# fix "ImportError: libapriltag.so.3: cannot open shared object file: No such file or directory"
# https://github.com/AprilRobotics/apriltag/issues/46
ENV LD_LIBRARY_PATH "/usr/local/lib:${LD_LIBRARY_PATH}"

WORKDIR /app
COPY . /app

RUN pip install --trusted-host pypi.python.org --upgrade pip \
    && pip install opencv-python \
    # && pip install --trusted-host pypi.python.org -r requirements.txt \
    && git clone https://github.com/AprilRobotics/apriltag.git /home/apriltag \
    && cd /home/apriltag \
    # fix missing site-packages in /root/.local/lib/python3.7/
    # && ln -s /usr/local /root/.local \
    && cmake . \
    && make install

CMD python test.py