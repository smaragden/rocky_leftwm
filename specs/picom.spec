# Note: compton fork renamed to 'picom' since version 7.5
 
%global oldname compton-ng
 
Name:           picom
Version:        9.1
Release:        1%{?dist}
Summary:        Lightweight compositor for X11 (previously a compton fork)
 
License:        MPLv2.0 and MIT
URL:            https://github.com/yshui/picom
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libev-devel
BuildRequires:  meson
BuildRequires:  uthash-devel
BuildRequires:  dbus-devel
BuildRequires:  libconfig-devel
BuildRequires:  libdrm-devel
BuildRequires:  libev-devel
BuildRequires:  libX11-devel
BuildRequires:  libX11-xcb
BuildRequires:  libXext-devel
BuildRequires:  libxcb-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  meson
BuildRequires:  pcre-devel
BuildRequires:  pixman-devel
BuildRequires:  uthash-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-renderutil-devel
BuildRequires:  xorg-x11-proto-devel

#BuildRequires:  pkgconfig(dbus-1)
#BuildRequires:  pkgconfig(gl)
#BuildRequires:  pkgconfig(libconfig)
#BuildRequires:  pkgconfig(libpcre)
#BuildRequires:  pkgconfig(libxdg-basedir)
#BuildRequires:  pkgconfig(pixman-1)
#BuildRequires:  pkgconfig(x11)
#BuildRequires:  pkgconfig(xcb-composite)
#BuildRequires:  pkgconfig(xcb-damage)
#BuildRequires:  pkgconfig(xcb-image)
#BuildRequires:  pkgconfig(xcb-present)
#BuildRequires:  pkgconfig(xcb-randr)
#BuildRequires:  pkgconfig(xcb-render)
#BuildRequires:  pkgconfig(xcb-renderutil)
#BuildRequires:  pkgconfig(xcb-shape)
#BuildRequires:  pkgconfig(xcb-xfixes)
#BuildRequires:  pkgconfig(xcb-xinerama)
#BuildRequires:  pkgconfig(xcb)
#BuildRequires:  pkgconfig(xext)
#BuildRequires:  pkgconfig(xproto)
 
Requires:       hicolor-icon-theme
 
Conflicts:      compton%{?_isa}
 
Provides:       %{oldname}%{?_isa} = %{version}-%{release}
 
Obsoletes:      %{oldname} =< 7.5-1
 
%description
This is forked from the original Compton because that seems to have become
unmaintained.
 
The current battle plan of this fork is to refactor it to make the code
possible to maintain, so potential contributors won't be scared away when they
take a look at the code.
 
We also try to fix bugs.
 
 
%prep
%autosetup -p1
 
 
%build
%meson -Dbuild_docs=true
%meson_build
 
%install
%meson_install
 
%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
 
 
%files
%license COPYING LICENSES/MPL-2.0 LICENSES/MIT
%doc README.md CONTRIBUTORS picom.sample.conf
%{_bindir}/%{name}*
%{_bindir}/compton*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
