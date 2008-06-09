%define name		xrx
%define version		1.0.1
%define release		%mkrel 8

%define major		0
%define libname		%mklibname %name %major
%define libname_nest	%mklibname %{name}nest %major
%define develname	%mklibname %name -d
%define staticname	%mklibname %name -d -s

Name: %{name}
Version: %{vernsion}
Release: %{release}
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
%{_mandir}/man1/xrx.1*

#------------------------------------------------------------------------------

%package -n %libname
Group: Development/X11
Summary: Core xrx library

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%description -n %libname
Core xrx library.

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/libxrx.so.%{major}*
%{_mandir}/man1/libxrx.1*

#------------------------------------------------------------------------------

%package -n %libname_nest
Group: Development/X11
Summary: Core xrx library

%description -n %libname_nest
Core xrx library.

%if %mdkversion < 200900
%post -n %libname_nest -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname_nest -p /sbin/ldconfig
%endif

%files -n %libname_nest
%defattr(-,root,root,-)
%{_libdir}/libxrxnest.so.%{major}*

#------------------------------------------------------------------------------

%package -n %develname
Group: Development/X11
Summary: Development package for xrx
Requires: %libname = %version-%release
Requires: %libname_nest = %version-%release

Requires: %{name} >= %{version}
Obsoletes: xrx-devel
Provides: %{name}-devel

%description -n %develname
Core xrx library development headers.

%files -n %develname
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/*.la

#------------------------------------------------------------------------------

%package -n %staticname
Group: Development/X11
Summary: Static development package for xrx
Obsoletes: xrx-static-devel
Provides: %{name}-static-devel

%description -n %staticname
Core xrx library static development headers.

%files -n %staticname
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
%makeinstall_std

%clean
rm -rf %buildroot
