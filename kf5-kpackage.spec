%define		kdeframever	5.67
%define		qtver		5.9.0
%define		kfname		kpackage

Summary:	Library to load and install packages as plugins
Name:		kf5-%{kfname}
Version:	5.67.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	6bf9110d2c3746fdf0c70cc8451c3596
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdoctools-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Library to load and install packages as plugins.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/qt5/plugins/kpackage/packagestructure
%ninja_install -C build

%find_lang lib%{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f lib%{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
%{_datadir}/qlogging-categories5/kpackage.categories
%attr(755,root,root) %{_bindir}/kpackagetool5
%attr(755,root,root) %ghost %{_libdir}/libKF5Package.so.5
%attr(755,root,root) %{_libdir}/libKF5Package.so.*.*
%dir %{_libdir}/qt5/plugins/kpackage
%dir %{_libdir}/qt5/plugins/kpackage/packagestructure
%{_mandir}/man1/kpackagetool5.1*
%lang(ca) %{_mandir}/ca/man1/kpackagetool5.1*
%lang(de) %{_mandir}/de/man1/kpackagetool5.1*
%lang(es) %{_mandir}/es/man1/kpackagetool5.1*
%lang(it) %{_mandir}/it/man1/kpackagetool5.1*
%lang(nl) %{_mandir}/nl/man1/kpackagetool5.1*
%lang(pt) %{_mandir}/pt/man1/kpackagetool5.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kpackagetool5.1*
%lang(sv) %{_mandir}/sv/man1/kpackagetool5.1*
%lang(uk) %{_mandir}/uk/man1/kpackagetool5.1*
%{_datadir}/kservicetypes5/kpackage-generic.desktop
%{_datadir}/kservicetypes5/kpackage-genericqml.desktop
%{_datadir}/kservicetypes5/kpackage-packagestructure.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KPackage
%{_includedir}/KF5/kpackage_version.h
%{_libdir}/cmake/KF5Package
%attr(755,root,root) %{_libdir}/libKF5Package.so
