%define		git_hash 51b1869
%define		pkg	nopt
Summary:	Node.js option parsing
Name:		nodejs-%{pkg}
Version:	1.0.10
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/nopt
# download from https://github.com/isaacs/%{pkg}/tarball/%%{version}
Source0:	isaacs-%{pkg}-%{version}-0-g%{git_hash}.tar.gz
# Source0-md5:	d72434b028241bd406a48d29eec64656
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-abbrev
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An option parsing library for Node.js and its package manager (npm).

%prep
%setup -qc
mv isaacs-%{pkg}-*/* .

#%nodejs_fixshebang bin/%{pkg}.js

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}
cp -p lib/%{pkg}.js $RPM_BUILD_ROOT%{nodejs_libdir}

install -d $RPM_BUILD_ROOT%{_bindir}
cp -p bin/%{pkg}.js $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/%{pkg}.js
%{nodejs_libdir}/%{pkg}.js
%{_examplesdir}/%{name}-%{version}
