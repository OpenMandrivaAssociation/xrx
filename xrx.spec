Name: xrx
Version: 1.0.1
Release: %mkrel 4
Summary: RX helper program 
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxau-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: x11-xtrans-devel >= 1.0.0

%description
The xrx helper program may be used with any Web browser to interpret documents
in the RX MIME type format and start remote applications.

%files
%defattr(-,root,root)
%{_bindir}/xrx
%{_mandir}/man1/xrx.1x.bz2

#------------------------------------------------------------------------------

%define lib_name_xrx %mklibname xrx 0

%package -n %lib_name_xrx
Group: Development/X11
Summary: Core xrx library

%post -n %lib_name_xrx -p /sbin/ldconfig
%postun -n %lib_name_xrx -p /sbin/ldconfig

%description -n %lib_name_xrx
Core xrx library

%files -n %lib_name_xrx
%defattr(-,root,root,-)
%{_libdir}/libxrx.so.*
%{_mandir}/man1/libxrx.1x.bz2

#------------------------------------------------------------------------------

%define lib_name_xrxnest %mklibname xrxnest 0

%package -n %lib_name_xrxnest
Group: Development/X11
Summary: Core xrx library

%description -n %lib_name_xrxnest
Core xrx library

%post -n %lib_name_xrxnest -p /sbin/ldconfig
%postun -n %lib_name_xrxnest -p /sbin/ldconfig

%files -n %lib_name_xrxnest
%defattr(-,root,root,-)
%{_libdir}/libxrxnest.so.*

#------------------------------------------------------------------------------

%package devel
Group: Development/X11
Summary: Development package for xrx
Requires: %lib_name_xrx = %version-%release
Requires: %lib_name_xrxnest = %version-%release

Requires: %{name} >= %{version}

%description devel
Core xrx library

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/*.la

#------------------------------------------------------------------------------

%package static-devel
Group: Development/X11
Summary: Development package for xrx

%description static-devel
Core xrx library

%files static-devel
%defattr(-,root,root,-)
%{_libdir}/*.a

#------------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot




