%define		_class		Console
%define		_subclass	Color
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	Easily use ANSI console colors in your application
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	%mkrel 5
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/Console_Color/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
You can use Console_Color::convert to transform colorcodes like %%r
into ANSI control codes. 'print Console_Color::convert("%%rHello
World!%%n");' would print "Hello World" in red, for example.

In PEAR status of this package is: %{_status}.

%prep
%setup -q -c

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/pear/%{_class}

install -m 644 %{_pearname}-%{version}/*.php \
    %{buildroot}%{_datadir}/pear/%{_class}

install -d -m 755 %{buildroot}%{_datadir}/pear/packages
install -m 644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_pearname}-%{version}/examples/*
%dir %{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/packages/%{_pearname}.xml


