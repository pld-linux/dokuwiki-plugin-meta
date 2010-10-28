%define		plugin		meta
Summary:	Dokuwiki Plugin to Set Metadata
Name:		dokuwiki-plugin-%{plugin}
Version:	20060415
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.chimeric.de/_src/plugin-meta.tgz
# Source0-md5:	81f428efcce5b0193bf0be51c8919e1c
URL:		http://www.dokuwiki.org/plugin:meta
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20061106
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
mv %{plugin}/* .

version=$(awk -F"'" '/date/&&/=>/{print $4}' syntax.php)
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
