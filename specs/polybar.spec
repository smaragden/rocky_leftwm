	
%global url1    https://github.com/%{name}
 
Name:           polybar
Version:        3.6.1
Release:        1%{?dist}
Summary:        Fast and easy-to-use status bar
 
# BSD 2-clause "Simplified" License
# ---------------------------------
# lib/concurrentqueue/
#
# Expat License
# -------------
# lib/i3ipcpp/
# lib/xpp/
#
License:        MIT and BSD
URL:            https://polybar.github.io/
Source0:        %{url1}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
 
# Bundled libs

#cairo-devel
#libuv
#xcb-util-devel
#libxcb-devel
#xcb-proto
#xcb-util-image-devel
#xcb-util-wm-devel
#libuv-devel
#alsa-lib-devel
#pulseaudio-libs-devel
#jsoncpp-devel
#libnl3-devel

BuildRequires:  libuv-devel
BuildRequires:  cmake >= 3.1
BuildRequires:  gcc-c++
BuildRequires:  git-core
#BuildRequires:  i3-devel
BuildRequires:  libmpdclient-devel
BuildRequires:  libnl3-devel
BuildRequires:  python3 >= 3.5
BuildRequires:  python3-sphinx
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-wm-devel
#BuildRequires:  xcb-util-xrm-devel
 
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(jsoncpp) >= 1.7.7
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb)
 
%description
Polybar aims to help users build beautiful and highly customizable status bars
for their desktop environment, without the need of having a black belt in shell
scripting.
 
 
%prep
%setup -q

mkdir -p {,doc/}%{_vpath_builddir}
 
 
%build
# Build man page
# %cmake                              \
#    -B $PWD/doc/%{_vpath_builddir}  \
#    -S $PWD/doc
# %make_build -C doc/%{_vpath_builddir} doc_man
 
%cmake                                  \
    -DBUILD_DOC=false                   \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo   \
    -B $PWD/%{_vpath_builddir}          \
    -S $PWD
%make_build -C %{_vpath_builddir}
 
 
%install
%make_install -C %{_vpath_builddir}
 
# Install man page
# install -Dpm 0644 doc/%{_vpath_builddir}/man/%{name}.1 \
#     %{buildroot}/%{_mandir}/man1/%{name}.1
 
 
%files
%license LICENSE
%doc README.md SUPPORT.md
%{_bindir}/%{name}
%{_bindir}/%{name}-msg
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/
%config(noreplace) %{_sysconfdir}/%{name}/config.ini
#%{_docdir}/%{name}/config
#%{_mandir}/man1/*.1*
