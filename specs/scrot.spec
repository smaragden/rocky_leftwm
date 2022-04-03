Name:    scrot
Version: 1.7
Release: 1%{?dist}
Summary: Simple command-line screenshot utility for X
License: MIT-feh
Url:     https://github.com/resurrecting-open-source-projects/scrot/
Source:  https://github.com/resurrecting-open-source-projects/scrot/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: imlib2-devel
BuildRequires: libX11-devel
BuildRequires: libXcomposite-devel
BuildRequires: libbsd-devel

%description
scrot is a simple command line screen capture utility, it uses imlib2 to grab and save images.

%prep
%autosetup

%build
./autogen.sh
./configure --prefix=%{buildroot}%{_prefix}
make all


%install
make install

%files
%license COPYING
%doc AUTHORS README.md ChangeLog scrot.png
%{_bindir}/*
%{_mandir}/man1/*
