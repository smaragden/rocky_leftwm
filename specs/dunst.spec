Name:     dunst
Version:  1.8.1
Release:  2%{?dist}
Summary:  Simple and configurable notification-daemon
Group:    User Interface/X
License:  BSD and MIT
URL:      https://dunst-project.org
Source0:  https://github.com/dunst-project/%{name}/archive/refs/tags/v%{version}.tar.gz

Requires: dbus

# keep this sorted please
BuildRequires: cairo-devel
BuildRequires: dbus-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires: libnotify-devel
BuildRequires: libpng-devel
#BuildRequires: lib64xdg-basedir-devel
BuildRequires: libXft-devel
BuildRequires: libXinerama-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libX11-devel
BuildRequires: pango-devel
BuildRequires: systemd
BuildRequires: /usr/bin/pod2man

Provides: desktop-notification-daemon


%description
Dunst is a highly configurable and lightweight notification daemon with the
similar look and feel to dmenu.


%prep
%setup -q


%build
make %{?_smp_mflags} VERSION=%{version} PREFIX=%{_prefix} EXTRACFLAGS="%{optflags}" WAYLAND=0


%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} WAYLAND=0


%files
%doc AUTHORS CHANGELOG.md LICENSE README.md RELEASE_NOTES
%{_bindir}/%{name}
%{_bindir}/%{name}ctl
%{_bindir}/%{name}ify
%{_datadir}/dbus-1/services/org.knopwob.%{name}.service
%{_userunitdir}/%{name}.service
%{_prefix}/etc/xdg/dunst/dunstrc
%{_datadir}/man/man1/%{name}.1.gz
%{_datadir}/man/man1/%{name}ctl.1.gz
%{_datadir}/man/man5/%{name}.5.gz
