%define 	module	pycurl
Summary:	Free and easy-to-use client-side URL transfer library
Summary(pl.UTF-8):	Łatwa w użyciu biblioteka obsługi URL od strony klienta
Name:		python-%{module}
Version:	7.15.5.1
Release:	2
License:	LGPL
Group:		Libraries/Python
Source0:	http://pycurl.sourceforge.net/download/%{module}-%{version}.tar.gz
# Source0-md5:	464cfbeba150d99d92a407c7c8b751de
Patch0:		%{name}-curl.patch
URL:		http://pycurl.sourceforge.net/
BuildRequires:	curl-devel >= 7.15.5
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	curl-libs >= 7.15.5
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
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{py_sitedir}/*.so
%dir %{py_sitedir}/curl
%{py_sitedir}/curl/*.py[co]

%files doc
%defattr(644,root,root,755)
%doc doc/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
