Name     : golang-github-gorilla-mux 
Version  : 0
Release  : 4
URL      : https://github.com/gorilla/mux/archive/49c024275504f0341e5a9971eb7ba7fa3dc7af40/mux-49c0242.tar.gz
Source0  : https://github.com/gorilla/mux/archive/49c024275504f0341e5a9971eb7ba7fa3dc7af40/mux-49c0242.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires: go
BuildRequires: golang-github-gorilla-context

%description
mux
===
[![GoDoc](https://godoc.org/github.com/gorilla/mux?status.svg)](https://godoc.org/github.com/gorilla/mux)
[![Build Status](https://travis-ci.org/gorilla/mux.png?branch=master)](https://travis-ci.org/gorilla/mux)

%prep
%setup -q -n mux-49c024275504f0341e5a9971eb7ba7fa3dc7af40

%build

%install
%global gopath /usr/lib/golang
%global library_path github.com/gorilla/mux
rm -rf %{buildroot}
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for file in $(find . -iname "*.go") ; do
     install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
     cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
done

%check
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/gorilla/mux/bench_test.go
/usr/lib/golang/src/github.com/gorilla/mux/doc.go
/usr/lib/golang/src/github.com/gorilla/mux/mux.go
/usr/lib/golang/src/github.com/gorilla/mux/mux_test.go
/usr/lib/golang/src/github.com/gorilla/mux/old_test.go
/usr/lib/golang/src/github.com/gorilla/mux/regexp.go
/usr/lib/golang/src/github.com/gorilla/mux/route.go
