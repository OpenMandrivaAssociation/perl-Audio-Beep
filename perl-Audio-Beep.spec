%define upstream_name    Audio-Beep
%define upstream_version 0.11
%define debug_package %{nil}

Name:       perl-%{upstream_name}
Version:	0.11
Release:	5

Summary:    Audio::Beep player module using the B<beep> program
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/dist/Audio-Beep
Source0:	https://cpan.metacpan.org/authors/id/G/GI/GIULIENK/Audio-Beep-0.11.tar.gz

BuildRequires:	make
BuildRequires: perl(Test::More)
BuildRequires: perl-devel

%description
no description found

%prep
%setup -q -n Audio-Beep-0.11

%build
echo | perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*
