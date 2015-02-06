%define upstream_name    Audio-Beep
%define upstream_version 0.11

%define debug_package %{nil}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    6

Summary:    Audio::Beep player module using the B<beep> program
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Audio/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl-devel

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*
