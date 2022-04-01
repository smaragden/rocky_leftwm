# Optimize for build time or performance
%bcond_with release_build

%global debug_package %{nil}

Name:           leftwm
Version:        0.2.11
Release:        1%{?dist}
Summary:        Tiling window manager for Adventurers

License:        MIT
URL:            http://leftwm.org/
Source0:        https://github.com/leftwm/leftwm/archive/%{version}/%{name}-%{version}.tar.gz

#BuildRequires:  cargo
#BuildRequires:  rust

%description
Left is a tiling window manager written in rust for stability and performance.
The core of left is designed to do one thing and one thing well. Be a window
manager. Because you probably want more than just a black screen LeftWM is built
around the concept of theming. With themes you can choose between different bar
/ compositor / background / colors, whatever makes you happy.

LeftWM has been built from the very beginning to support multiple screens and
has been built around ultrawide monitors. You will see this with the default key
bindings.

Left is NOT
-----------

- Left is not a compositor.
- Left is not a lock screen.
- Left is not a bar there are lots of good bars out there. With themes, picking
  one is as simple as setting a symlink.


%prep
%autosetup -p1


%build
#%if %{with release_build}
#cargo build --release
#%else
#cargo build
#%endif


%install
%if %{with release_build}
cargo install --root=%{buildroot}%{_prefix} --path=leftwm --release
%else
cargo install --root=%{buildroot}%{_prefix} --path=leftwm --debug
%endif
rm -f   %{buildroot}%{_prefix}/.crates.toml \
        %{buildroot}%{_prefix}/.crates2.json
install -m 0644 -Dp %{name}.desktop %{buildroot}%{_datadir}/xsessions/%{name}.desktop


%files
%license LICENSE.md
%doc README.md CHANGELOG
%{_bindir}/leftwm*
%{_datadir}/xsessions/%{name}.desktop
