# TODO
# - as-needed fix: drop libssh2 dep from curl

# During its initialization, PycURL checks that the actual libcurl version
# is not lower than the one used when PycURL was built.
# Yes, that should be handled by library versioning (which would then get
# automatically reflected by rpm).
# For now, we have to reflect that dependency.
%define		libcurl_ver %(rpm -q --qf '%|E?{%{E}:}|%{V}' curl-devel | sed 's/package .* is not installed/ERROR/' || echo ERROR)

%define 	module	pycurl
Summary:	Free and easy-to-use client-side URL transfer library
Summary(pl.UTF-8):	Łatwa w użyciu biblioteka obsługi URL od strony klienta
Name:		python-%{module}
Version:	7.19.0
Release:	2
License:	LGPL
Group:		Libraries/Python
Source0:	http://pycurl.sourceforge.net/download/%{module}-%{version}.tar.gz
# Source0-md5:	919d58fe37e69fe87ce4534d8b6a1c7b
Patch0:		%{name}-no-static-libs.patch
URL:		http://pycurl.sourceforge.net/
BuildRequires:	curl-devel >= 7.19
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	curl-libs >= %{libcurl_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pycurl is Python interface to curl library - free and easy-to-use
client-side URL transfer library, supporting FTP, FTPS, HTTP, HTTPS,
GOPHER, TELNET, DICT, FILE and LDAP. libcurl supports HTTPS
certificates, HTTP POST, HTTP PUT, FTP uploading, kerberos, HTTP form
based upload, proxies, cookies, user+password authentication, file
transfer resume, HTTP proxy tunneling and more!

%description -l pl.UTF-8
pycurl jest interfejsem języka Python do biblioteki libcurl -
wolnodostępnej i łatwej w użyciu biblioteki operacji na URL-ach od
strony klienta, obsługującej FTP, FTPS, HTTP, HTTPS, GOPHER, TELNET,
DICT, FILE i LDAP. libcurl obsługuje także certyfikaty HTTPS, HTTP
POST, HTTP PUT, uploady FTP, kerberos, upload plików przez HTTP oparty
na formularzach, proxy, ciasteczka, uwierzytelnienie, wznawianie
przesyłania plików, tunelowanie proxy i wiele innych.

%package doc
Summary:	Documentation for pycurl Python module
Summary(pl.UTF-8):	Dokumentacja do modułu Pythona pycurl
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This module contains documentation files for pycurl Python module.

%description doc -l pl.UTF-8
Moduł zawierający dokumentację dla modułu Pythona pucurl.

%package examples
Summary:	Examples for pycurl Python module
Summary(pl.UTF-8):	Przykładowe programy do modułu Pythona pycurl
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This module contains examples for pycurl Python module.

%description examples -l pl.UTF-8
Moduł zawierający przykładowe programy do modułu Pythona pycurl.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0

%build
%{__python} setup.py build \
	--debug

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT%{_docdir}/pycurl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{py_sitedir}/*.so
%dir %{py_sitedir}/curl
%{py_sitedir}/curl/*.py[co]
%{py_sitedir}/pycurl-*.egg-info

%files doc
%defattr(644,root,root,755)
%doc doc/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
