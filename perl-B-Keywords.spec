#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	B
%define	pnam	Keywords
Summary:	B::Keywords - Lists of reserved barewords and symbol names
#Summary(pl.UTF-8):	
Name:		perl-B-Keywords
Version:	1.06
Release:	1
License:	GPL v2 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JJ/JJORE/B-Keywords-1.06.tar.gz
# Source0-md5:	24f311df8a5f0174cc465e1949082db3
URL:		http://search.cpan.org/dist/B-Keywords/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
B::Keywords supplies seven arrays of keywords: @Scalars, @Arrays,
@Hashes, @Filehandles, @Symbols, @Functions, and @Barewords. The @Symbols
array includes the contents of each of @Scalars, @Arrays, @Hashes, and
@Filehandles.  Similarly, @Barewords adds a few non-function keywords
and operators to the @Functions array.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/B/*.pm
%{_mandir}/man3/*
