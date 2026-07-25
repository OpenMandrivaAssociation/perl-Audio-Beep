%define upstream_name    Audio-Beep
%define upstream_version 0.11

%define debug_package %{nil}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    7

Summary:    Audio::Beep player module using the B<beep> program
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/dist/Audio-Beep
Source0:    https://cpan.metacpan.org/authors/id/G/GI/GIULIENK/Audio-Beep-%{upstream_version}.tar.gz

BuildRequires:	make
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
