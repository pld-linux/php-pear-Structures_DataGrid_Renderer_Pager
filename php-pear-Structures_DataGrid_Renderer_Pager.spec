%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	DataGrid_Renderer_Pager
%define		_status		beta
%define		_pearname	Structures_DataGrid_Renderer_Pager
Summary:	%{_pearname} - Renderer driver using PEAR::Pager
Summary(pl.UTF-8):   %{_pearname} - sterownik renderera korzystający z PEAR::Pager
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8c9950ffce7cd96d26d96e51c2232daa
URL:		http://pear.php.net/package/Structures_DataGrid_Renderer_Pager/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.4.9
Requires:	php-pear-Pager >= 2.4.0
Requires:	php-pear-Structures_DataGrid >= 0.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Renderer driver for Structures_DataGrid using PEAR::Pager.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza sterownik renderera do PEAR::Pager dla
Structures_DataGrid.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/DataGrid/Renderer/Pager.php
