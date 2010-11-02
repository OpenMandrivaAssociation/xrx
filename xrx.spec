Name:		xrx
Version:	1.0.4
Release:	%{mkrel 1}
Summary:	RX helper program 
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	libx11-devel >= 1.0.0
BuildRequires:	libxau-devel >= 1.0.0
BuildRequires:	libxext-devel >= 1.0.0
BuildRequires:	libxt-devel >= 1.0.0
BuildRequires:	libxaw-devel >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	x11-xtrans-devel >= 1.0.0
# for npapi.h
BuildRequires:	xulrunner-devel

%description
The xrx helper program may be used with any Web browser to interpret documents
in the RX MIME type format and start remote applications.

%package plugin
Group:		Development/X11
Summary:	RX browser plugins
Obsoletes:	%{mklibname xrx 0} < %{version}-%{release}
Obsoletes:	%{mklibname xrxnest 0} < %{version}-%{release}
Obsoletes:	%{mklibname xrx -d} < %{version}-%{release}
Obsoletes:	%{mklibname xrx -d -s} < %{version}-%{release}

%description plugin
Mozilla-type browser plugins to allow the handling of documents in the
RX MIME type format to start remote applications.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_libdir}/mozilla/plugins
mv %{buildroot}%{_libdir}/*.so %{buildroot}%{_libdir}/mozilla/plugins
rm -f %{buildroot}%{_libdir}/*.*a

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xrx
%{_mandir}/man1/xrx.1*

%files plugin
%defattr(-,root,root,-)
%{_libdir}/mozilla/plugins/*.so
%{_mandir}/man1/libxrx.1*

