Summary:	xditview application
Summary(pl):	Aplikacja xditview
Name:		xorg-app-xditview
Version:	0.99.2
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/app/xditview-%{version}.tar.bz2
# Source0-md5:	feeea439c548a59f8b7bdd8cc7f33f6f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
# for dir (only?)
Requires:	xorg-data-xbitmaps
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xditview application.

%description -l pl
Aplikacja xditview.

%prep
%setup -q -n xditview-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/app-defaults/*
%{_includedir}/X11/bitmaps/*
%{_mandir}/man1/*.1x*
