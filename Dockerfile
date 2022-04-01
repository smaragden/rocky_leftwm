FROM rockylinux:8

RUN dnf install -y epel-release gcc rpm-build rpm-devel rpmlint make diffutils patch rpmdevtools dnf-plugins-core \
&& dnf config-manager --set-enabled powertools \
&& yum clean all
RUN useradd rpmbuild -u 5002 -g users -p rpmbuild
RUN curl https://static.rust-lang.org/dist/rust-1.59.0-x86_64-unknown-linux-gnu.tar.gz | tar xvz \
&& rust-1.59.0-x86_64-unknown-linux-gnu/install.sh \
&& rm -rf /rust-1.59.0-x86_64-unknown-linux-gnu

COPY rpm_build.sh rpm_build.sh
ENTRYPOINT [ "./rpm_build.sh" ]
