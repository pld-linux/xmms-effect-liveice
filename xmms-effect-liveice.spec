Summary:	LiveIce Plugin for XMMS
Summary(pl):	Wtyczka LiveIce dla XMMS-a
Name:		xmms-effect-liveice
Version:	1.0.0
Release:	7
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://star.arm.ac.uk/~spm/software/liveice-xmms.tar.gz
# Source0-md5:	81d057e47044d05dc65e81dc0b5927e6
URL:		http://star.arm.ac.uk/~spm/software/liveice.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.0.0
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LiveIce XMMS is an effects plugin for XMMS which sends streams to
IceCast and provides a limited set of functions similar to those
provided by liveice but without half the hassle. LiveIce XMMS lacks
many of the features of the full version of LiveIce but provides the
main functions needed to stream from XMMS. Much of this simplicity
comes from the GUI which was designed by Peter from the XMMS team.

%description -l pl
LiveIce XMMS jest wtyczk± dla XMMS-a, która wysy³a strumienie po IceCast
i zapewnia ograniczony zestaw funkcji podobnych do tych, które daje
liveice. LiveIce XMMS nie ma wielu funkcji pe³nej wersji liveice, ale
zawiera funkcje potrzebne do dostarczania strumienia z XMMS-a. Wiêkszo¶æ
funkcji jest dostêpna z GUI zaprojektowanego przez Petera z zespo³u
XMMS.

%prep
%setup -q -n LiveIce-%{version}
%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT;

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{xmms_effect_plugindir}/*.so
