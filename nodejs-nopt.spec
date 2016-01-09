%define		pkg	nopt
Summary:	Node.js option parsing
Name:		nodejs-%{pkg}
Version:	3.0.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	ee4fe9b98110d1df8ba2564039eab415
URL:		https://github.com/isaacs/nopt
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
Requires:	nodejs
Requires:	nodejs-abbrev < 2.0.0
Requires:	nodejs-abbrev >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An option parsing library for Node.js and its package manager (npm).

%prep
%setup -qc
mv package/* .

%{__sed} -i -e '1s,^#!.*node,#!/usr/bin/node,' bin/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{nodejs_libdir}/%{pkg}}
cp -a package.json lib bin $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

ln -s %{nodejs_libdir}/%{pkg}/bin/%{pkg}.js $RPM_BUILD_ROOT%{_bindir}/%{pkg}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/%{pkg}
%dir %{nodejs_libdir}/%{pkg}
%{nodejs_libdir}/%{pkg}/package.json
%{nodejs_libdir}/%{pkg}/lib
%dir %{nodejs_libdir}/%{pkg}/bin
%attr(755,root,root) %{nodejs_libdir}/%{pkg}/bin/nopt.js
%{_examplesdir}/%{name}-%{version}
