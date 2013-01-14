Summary:	xditview application to display ditroff output on an X display
Summary(pl.UTF-8):	Aplikacja xditview - wyświetlanie wyjścia ditroff na ekranie X
Name:		xorg-app-xditview
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xditview-%{version}.tar.bz2
# Source0-md5:	a9a49c84477be93cdd1cd7726d758574
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 1.8
# for dir (only?)
Requires:	xorg-data-xbitmaps
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xditview application displays ditroff output on an X display.

%description -l pl.UTF-8
Aplikacja xditview wyświetla wyjście ditroff na ekranie X.

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xditview
%{_datadir}/X11/app-defaults/Xditview*
%{_includedir}/X11/bitmaps/[lr]dblarrow
%{_mandir}/man1/xditview.1x*
