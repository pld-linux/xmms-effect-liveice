Summary:	LiveIce Plugin for XMMS
Name:		xmms-effect-liveice
Version:	1.0.0
Release:	2
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://star.arm.ac.uk/~spm/software/liveice-xmms.tar.gz
URL:		http://star.arm.ac.uk/~spm/software/liveice.html
BuildRequires:	xmms-devel >= 1.0.0
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6

%description
LiveIce Plugin for XMMS

LiveIce XMMS is an effects plugin for xmms which sends streams to
IceCast and provides a limited set of functions similar to those
provided by liveice but without half the hassle. LiveIce XMMS lacks
many of the features of the full version of LiveIce but provides the
main functions needed to stream from xmms. Much of this simplicity
comes from the GUI which was designed by Peter from the XMMS team.

%prep
%setup -q -n LiveIce-%{version}
%build
libtoolize --copy --force
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT;
install -d $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT;

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmms/Effect/*so
%attr(755,root,root) %{_libdir}/xmms/Effect/*la
