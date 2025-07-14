#
# Conditional build:
%bcond_without	opengl		# build without opengl
#
Summary:	Turn based strategy game with isometric graphic
Summary(pl.UTF-8):	Turowa gra strategiczna z grafiką izometryczną
Name:		mars
Version:	0.2.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/mars/%{name}-%{version}-src.tar.gz
# Source0-md5:	c86674cd1fd6d0045e43218d929eb391
Patch0:		%{name}-install.patch
Patch1:		%{name}-opt.patch
URL:		http://sourceforge.net/projects/mars/
%{?with_opengl:BuildRequires:	OpenGL-devel}
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	scons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mars, Land of No Mercy is a turn based strategy game with isometric
graphic.

The player is the leader of a mercenary group that works on the Red
Planet in the period of the terrestrian colonization.

%description -l pl.UTF-8
Mars, Land of No Mercy jest turową strategią z izometryczną grafiką.

Gracz staje na czele najemnej grupy, która pracuje na Czerwonej
Planecie w okresie wczesnej kolonizacji.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%scons \
	strip=no \
	with_opengl=%{?with_opengl:yes}%{!?with_opengl:no}

%install
rm -rf $RPM_BUILD_ROOT
# required by scons
install -d $RPM_BUILD_ROOT

%scons install \
	strip=no \
	with_opengl=%{?with_opengl:yes}%{!?with_opengl:no} \
	root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
