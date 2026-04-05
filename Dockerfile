FROM quay.io/pypa/manylinux_2_34

COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/

RUN dnf install ninja-build git -y

RUN git clone https://github.com/abseil/abseil-cpp.git --branch 20250814.1

WORKDIR "/abseil-cpp"

RUN cmake -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-fPIC"
RUN cmake --build build
RUN cmake --install ./build --prefix=/usr

WORKDIR "/"

ENTRYPOINT [ "bash" ]
STOPSIGNAL SIGTERM
