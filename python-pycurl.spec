
%include	/usr/lib/rpm/macros.python
%define 	module pycurl
Summary:	free and easy-to-use client-side URL transfer library
Summary(pl):	£atwa w u¿yciu biblioteka obs³ugi URL od strony klienta
Name:		python-%{module}
Version:	7.10.1
Release:	0.1
License:	LGPL
Group:		Libraries/Python
Source0:	http://%{module}.sourceforge.net/download/%{module}-%{version}.tar.gz
# Source0-md5:	ea14b6ecaf23e3a40aa63a56007c4d28
URL:		http://pycurl.sourceforge.net/
BuildRequires:	rpm-pythonprov
Requires:	python
Requires:	curl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pycurl is Python interface to curl library - free and easy-to-use
client-side URL transfer library, supporting FTP, FTPS, HTTP, HTTPS,
GOPHER, TELNET, DICT, FILE and LDAP. libcurl supports HTTPS
certificates, HTTP POST, HTTP PUT, FTP uploading, kerberos, HTTP form
based upload, proxies, cookies, user+password authentication, file
transfer resume, http proxy tunneling and more!

%description -l pl
pycurl jest interfejsem jêzyka Python do bibliteki libcurl -
wolnodostêpnej i ³atwej w u¿yciu bibliteki operacji na URLach od
strony klienta, obs³uguj±cej FTP, FTPS, HTTP, HTTPS, GOPHER, TELNET,
DICT, FILE i LDAP. libcurl obs³uguje tak¿e certyfikaty HTTPS, HTTP
POST, HTTP PUT, uploady FTP, kerberos, upload plików przez HTTP oparty
na formularzach, proxy, ciasteczka, uwierzytelnienie, wznawianie
przesy³ania plików, tunelowanie proxy i wiele innych.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO examples
%attr(755,root,root) %{py_sitedir}/*.so
