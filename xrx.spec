%define major		0
%define libname		%mklibname %name %major
%define libname_nest	%mklibname %{name}nest %major
%define develname	%mklibname %name -d
%define staticname	%mklibname %name -d -s

Name: xrx
Version: 1.0.1
Release: %mkrel 8
Summary: RX helper program 
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: x11-xtrans-devel	>= 1.0.4
BuildRequires: libx11-devel	>= 1.1.3
BuildRequires: libxaw-devel	>= 1.0.4

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

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

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

%post -n %libname_nest -p /sbin/ldconfig
%postun -n %libname_nest -p /sbin/ldconfig

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
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %buildroot
