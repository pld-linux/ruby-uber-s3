#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	uber-s3
Summary:	A simple & very fast S3 client supporting sync / async HTTP adapters
Name:		ruby-%{pkgname}
Version:	0.2.4
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	0df59babd03c6c6b2e664118dc4e4526
URL:		http://github.com/nulayer/uber-s3
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	ruby-rake
BuildRequires:	ruby-rspec < 2.8
BuildRequires:	ruby-rspec >= 2.7.0
%endif
Requires:	ruby-mime-types < 2
Requires:	ruby-mime-types >= 1.17
Requires:	ruby-rubygems >= 1.3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple & very fast S3 client supporting sync / async HTTP adapters.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
