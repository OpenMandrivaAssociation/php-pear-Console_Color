%define		_class		Console
%define		_subclass	Color
%define		upstream_name	%{_class}_%{_subclass}

Summary:	Easily use ANSI console colors in your application
Name:		php-pear-%{upstream_name}
Version:	1.0.3
Release:	11
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Console_Color/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Source1:	php-pear-Console_Color.rpmlintrc
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
You can use Console_Color::convert to transform colorcodes like %%r
into ANSI control codes. 'print Console_Color::convert("%%rHello
World!%%n");' would print "Hello World" in red, for example.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml

