%bcond clang 1

# TDE variables
%define tde_pkg twin-style-suse2
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	TDE window decoration from SUSE 9.3
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/themes/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils
BuildRequires:	gettext

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes


BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
This is a port of the SUSE 9.3 KDE Window decoration extracted from SUSE.

It features in additon to the original theme several new button
styles and a changeable titlebar image.

A color scheme for TDE is provided too.


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README TODO
%{tde_prefix}/%{_lib}/trinity/twin3_SUSE2.la
%{tde_prefix}/%{_lib}/trinity/twin3_SUSE2.so
%{tde_prefix}/%{_lib}/trinity/twin_SUSE2_config.la
%{tde_prefix}/%{_lib}/trinity/twin_SUSE2_config.so
%{tde_prefix}/share/apps/tdedisplay/color-schemes/SUSE2.kcsrc
%{tde_prefix}/share/apps/twin/SUSE2.desktop
%{tde_prefix}/share/apps/twin/pics/SUSE2/

