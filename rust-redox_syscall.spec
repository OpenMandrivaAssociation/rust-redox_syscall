%bcond_with check
%global debug_package %{nil}

%global crate redox_syscall

Name:           rust-%{crate}
Version:        0.2.10
Release:        1
Summary:        Rust library to access raw Redox system calls

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/redox_syscall
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(bitflags/default) >= 1.1.0 with crate(bitflags/default) < 2.0.0)
%endif

%global _description %{expand:
Rust library to access raw Redox system calls.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(redox_syscall) = 0.2.10
Requires:       cargo
Requires:       (crate(bitflags/default) >= 1.1.0 with crate(bitflags/default) < 2.0.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(redox_syscall/default) = 0.2.10
Requires:       cargo
Requires:       crate(redox_syscall) = 0.2.10

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 27 2022 Bernhard Rosenkränzer <bernhard.rosenkraenzer.ext@huawei.com> - 0.2.10-1
- Initial package
