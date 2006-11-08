#
# TODO: 
# - the game crashes with SDL Parachute deployed error,
#   it doesn't if we install the game and run it from the dir
#   where it was build, so theres probably more to install - 
#   find out what it is
#
# Conditional build:
%bcond_without	opengl		# build without opengl
#
Summary:	Turn based strategy game with isometric graphic
Summary(pl):	Turowa gra strategiczna z grafik± izometryczn±
Name:		mars
Version:	0.2.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/mars/%{name}-%{version}-src.tar.gz
# Source0-md5:	4ad8a9009af5947d6e69159eab47a923
Patch0:		%{name}-path.patch
URL:		http://www.marsnomercy.org/
%{?with_opengl:BuildRequires:	OpenGL-devel}
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	scons
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mars, Land of No Mercy is a turn based strategy game with isometric
graphic.

The player is the leader of a mercenary group that works on the Red
Planet in the period of the terrestrian colonization.

%description -l pl
Mars, Land of No Mercy jest turow± strategi± z izometryczn± grafik±.

Gracz staje na czele najemnej grupy, która pracuje na Czerwonej
Planecie w okresie wczesnej kolonizacji.

%prep
%setup -q
%patch0 -p1
%{__sed} -i 's@data/@%{_datadir}/%{name}/@' src/{mars.cpp,Functions.cpp}
%{__sed} -i 's@data/@%{_datadir}/%{name}/@' data/xml/ngg/light.xml
%{__sed} -i 's@data/@%{_datadir}/%{name}/@' data/xml/player.xml

%build
scons \
	with_opengl=%{?with_opengl:yes}%{!?with_opengl:no}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install %{name} $RPM_BUILD_ROOT%{_bindir}/
cp -r data/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
