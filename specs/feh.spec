Summary:	A fast and light Imlib2-based image viewer
Name:		feh
Version:	3.8
Release:	1
License:	MIT
Group:		Amusements/Graphics
URL:		http://feh.finalrewind.org/
Source:		http://feh.finalrewind.org/feh-%{version}.tar.bz2

BuildRequires:	imlib2-devel libcurl-devel libXinerama-devel libXt-devel
#BuildRequires:	giblib-devel


%description
feh is an X11 image viewer aimed mostly at console users. Unlike most other
viewers, it does not have a fancy GUI, but simply displays images. It is
controlled via commandline arguments and configurable key/mouse actions.


%prep
%setup -q


%build
#%{__make} CFLAGS="${CFLAGS:-%optflags}" PREFIX=%{_prefix}
%{__make} PREFIX=%{_prefix}


%install
%{__rm} -rf %{buildroot}
%{__make} install-{bin,man,font,img} PREFIX=%{_prefix} DESTDIR=%{buildroot} 

# cleanup
find %{buildroot} -type f -name '*-cam*' -exec rm -f {} \;


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root)
%{_bindir}/*
%{_mandir}/*
%{_datadir}/%{name}/*

%doc AUTHORS ChangeLog COPYING TODO examples/
