Name: libbltscommon1
Summary: Common BLTS functions
Version: 0.4.7
Release: 1
License: GPLv2
URL: https://github.com/mer-qa/blts-common
Source0: %{name}-%{version}.tar.gz
BuildRequires: flex
BuildRequires: bison
BuildRequires: libxml2-devel

%package devel
Summary: Common BLTS functions devel package
Requires: %{name} = %{version}-%{release}
Provides: libbltscommon-devel

%description
Common functions used in BLTS project test assets gathered in one library

%description devel
This package contains libbltscommon1 development files

%prep
%autosetup -n %{name}-%{version}

%build
./autogen.sh
%configure
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/*.a
mkdir -p $RPM_BUILD_ROOT/var/log/tests/blts/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%attr(1777,root,root) /var/log/tests/blts
%license COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%license COPYING
%doc README README.ParameterVariation
%{_libdir}/*.so
/usr/include/*.h
%{_libdir}/pkgconfig/*.pc

