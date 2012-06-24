%define 	module	pycurl
Summary:	Free and easy-to-use client-side URL transfer library
Summary(pl):	�atwa w u�yciu biblioteka obs�ugi URL od strony klienta
Name:		python-%{module}
Version:	7.14.1
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://pycurl.sourceforge.net/download/%{module}-%{version}.tar.gz
# Source0-md5:	a1531cc14d2e112404be991c260c93c8
URL:		http://pycurl.sourceforge.net/
BuildRequires:	curl-devel >= 7.14.1
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-modules
Requires:	curl >= 7.14.1
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pycurl is Python interface to curl library - free and easy-to-use
client-side URL transfer library, supporting FTP, FTPS, HTTP, HTTPS,
GOPHER, TELNET, DICT, FILE and LDAP. libcurl supports HTTPS
certificates, HTTP POST, HTTP PUT, FTP uploading, kerberos, HTTP form
based upload, proxies, cookies, user+password authentication, file
transfer resume, HTTP proxy tunneling and more!

%description -l pl
pycurl jest interfejsem j�zyka Python do biblioteki libcurl -
wolnodost�pnej i �atwej w u�yciu biblioteki operacji na URL-ach od
strony klienta, obs�uguj�cej FTP, FTPS, HTTP, HTTPS, GOPHER, TELNET,
DICT, FILE i LDAP. libcurl obs�uguje tak�e certyfikaty HTTPS, HTTP
POST, HTTP PUT, uploady FTP, kerberos, upload plik�w przez HTTP oparty
na formularzach, proxy, ciasteczka, uwierzytelnienie, wznawianie
przesy�ania plik�w, tunelowanie proxy i wiele innych.

%package doc
Summary:	Documentation for pycurl Python module
Summary(pl):	Dokumentacja do modu�u Pythona pycurl
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This module contains documentation files for pycurl Python module.

%description doc -l pl
Modu� zawieraj�cy dokumentacj� dla modu�u Pythona pucurl.

%package examples
Summary:	Examples for pycurl Python module
Summary(pl):	Przyk�adowe programy do modu�u Pythona pycurl
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This module contains examples for pycurl Python module.

%description examples -l pl
Modu� zawieraj�cy przyk�adowe programy do modu�u Pythona pycurl.

%prep
%setup -q -n %{module}-%{version}

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
