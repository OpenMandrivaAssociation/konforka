%define rev r243

%define	major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Convenience library for common KIN project code
Name:		konforka
Version:	0.0.1
Release:	%mkrel 0.%{rev}.10
Group:		System/Libraries
License:	MIT
URL:		http://kin.klever.net/konforka/
Source0:	%{name}-%{version}-%{rev}.tar.bz2
Patch0:		konforka-linkage_fix.diff
Patch1:		konforka-gcc43.diff
BuildRequires:	autoconf automake libtool
BuildRequires:	pkgconfig
BuildRequires:	libpqxx-devel
BuildRequires:	doxygen
BuildRequires:	libxslt-proc
BuildRequires:	postgresql-devel

%description
Convenience library for common KIN project code.

konforka library is a convenience library which is supposed to soak in some
code common to our projects. It is not likely that you want to try this out
unless you need it as a dependency for other project. This is why you
should not expect a lengthier description here.

%package -n	%{libname}
Summary:	Convenience library for common KIN project code
Group:          System/Libraries

%description -n	%{libname}
Convenience library for common KIN project code.

konforka library is a convenience library which is supposed to soak in some
code common to our projects. It is not likely that you want to try this out
unless you need it as a dependency for other project. This is why you
should not expect a lengthier description here.

%package -n	%{develname}
Summary:	Static library and header files for the konforka library
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}
Provides:	%{mklibname %{name} 0}-devel = %{version}
Obsoletes:	%{mklibname %{name} 0}-devel

%description -n	%{develname}
Convenience library for common KIN project code.

konforka library is a convenience library which is supposed to soak in some
code common to our projects. It is not likely that you want to try this out
unless you need it as a dependency for other project. This is why you
should not expect a lengthier description here.

This package contains the static konforka library and its header files.

%prep

%setup -q -n %{name}
%patch0 -p0
%patch1 -p0

%build
autoreconf -fi
%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

# cleanups
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc AUTHORS COPYING NEWS
%{_libdir}/*.so.*

%files -n %{develname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-0.r243.10mdv2012.0
+ Revision: 773225
- various fixes

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-0.r243.9mdv2011.0
+ Revision: 612656
- the mass rebuild of 2010.1 packages

* Tue Feb 16 2010 Funda Wang <fwang@mandriva.org> 0.0.1-0.r243.8mdv2010.1
+ Revision: 506452
- rebuild

* Mon Oct 05 2009 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-0.r243.7mdv2010.0
+ Revision: 453959
- fix build
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Jul 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-0.r243.5mdv2009.0
+ Revision: 233800
- fix linkage
- fix deps
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-0.r243.4mdv2008.0
+ Revision: 68891
- conform to the 2008 specs


* Sat Jan 13 2007 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-0.r243.3mdv2007.0
+ Revision: 108398
- rebuild
- fix deps
- fix deps
- fix deps
- Import konforka

* Sat Jan 13 2007 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-0.r243.1mdv2007.1
- initial Mandriva package

