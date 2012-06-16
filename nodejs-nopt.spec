%define		git_hash 51b1869
%define		pkg	nopt
Summary:	Node.js option parsing
Name:		nodejs-%{pkg}
Version:	1.0.10
Release:	2
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/nopt
# download from https://github.com/isaacs/%{pkg}/tarball/%%{version}
Source0:	isaacs-%{pkg}-%{version}-0-g%{git_hash}.tar.gz
# Source0-md5:	d72434b028241bd406a48d29eec64656
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
Requires:	nodejs
Requires:	nodejs-abbrev
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An option parsing library for Node.js and its package manager (npm).

%prep
%setup -qc
mv isaacs-%{pkg}-*/* .

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
