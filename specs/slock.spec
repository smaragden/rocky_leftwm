	
#%%global _hardened_build 1
 
Name:           slock
Version:        1.4
Release:        17%{?dist}
Summary:        Simple X display locker
License:        MIT
URL:            http://tools.suckless.org/%{name}
Source0:        http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
Patch0:         %{name}-1.4-libxcrypt.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  xorg-x11-proto-devel
 
%description
This is the simplest X screen locker we are aware of.  It is stable and
quite a lot people in this community are using it every day when they
are out with friends or fetching some food from the local pub.
 
%prep
%setup -q
%patch0 -p1
sed -e 's/^CFLAGS =/CFLAGS +=/g' -e 's/^LDFLAGS = -s/LDFLAGS +=/g' -i config.mk
sed -e 's/explicit_bzero\.c//' -i config.mk && rm -f explicit_bzero.c
sed -e 's/^\t@/\t/' -i Makefile
sed -e 's/nogroup/nobody/' config.def.h > config.h
 
%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
make %{?_smp_mflags}
 
%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
 
%files
%license LICENSE
%doc README
%attr(4755, root, root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
# There is no freedesktop.org .desktop file because slock is basically a helper
# binary for light windowmanagers, and it shouldn't appear in applications menu
