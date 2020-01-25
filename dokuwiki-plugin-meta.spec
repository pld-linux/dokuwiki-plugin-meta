%define		subver	2015-07-24
%define		ver		%(echo %{subver} | tr -d -)
%define		plugin		meta
%define		php_min_version 5.3.0
Summary:	Dokuwiki Plugin to Set Metadata
Name:		dokuwiki-plugin-%{plugin}
Version:	%{ver}
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/dokufreaks/plugin-meta/archive/8752219/%{plugin}-%{subver}.tar.gz
# Source0-md5:	c335f4ffd1ca022948955093a4d84dea
URL:		https://www.dokuwiki.org/plugin:meta
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20061106
Requires:	php(core) >= %{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
This plugin allows you to set metadata for a page. This is useful for
overriding default DokuWiki metadata, for example if you want to
display someone else than the user who pasted the text into the wiki
as the author of a blog entry.

%prep
%setup -qc
mv *-%{plugin}-*/* .

# nothing to do with tests
%{__rm} -r _test

%build
version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.txt
