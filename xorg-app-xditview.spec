Summary:	xditview application
Summary(pl.UTF-8):	Aplikacja xditview
Name:		xorg-app-xditview
Version:	1.0.1
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xditview-%{version}.tar.bz2
# Source0-md5:	e9a7192ef29453b8c810ddd556a463c0
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
# for dir (only?)
Requires:	xorg-data-xbitmaps
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xditview application.

%description -l pl.UTF-8
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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xditview
%{_datadir}/X11/app-defaults/Xditview*
%{_includedir}/X11/bitmaps/*dblarrow
%{_mandir}/man1/xditview.1x*
