%define libname %mklibname KF6Completion
%define devname %mklibname KF6Completion -d
%define git 20231010

Name: kf6-kcompletion
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kcompletion/-/archive/master/kcompletion-master.tar.bz2#/kcompletion-%{git}.tar.bz2
Summary: Powerful completion framework, including completion-enabled lineedit and combobox
URL: https://invent.kde.org/frameworks/kcompletion
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6Config)
Requires: %{libname} = %{EVRD}

%description
Powerful completion framework, including completion-enabled lineedit and combobox

%package -n %{libname}
Summary: Powerful completion framework, including completion-enabled lineedit and combobox
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Powerful completion framework, including completion-enabled lineedit and combobox

%package -n %{libname}-designer
Summary: Qt Designer support for %{name} widgets
Group: System/Libraries
Requires: %{libname} = %{EVRD}
Supplements: qt6-qttools-designer

%description -n %{libname}-designer
Qt Designer support for %{name} widgets

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Powerful completion framework, including completion-enabled lineedit and combobox

%prep
%autosetup -p1 -n kcompletion-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kcompletion.*

%files -n %{devname}
%{_includedir}/KF6/KCompletion
%{_libdir}/cmake/KF6Completion
%{_qtdir}/doc/KF6Completion.*

%files -n %{libname}
%{_libdir}/libKF6Completion.so*

%files -n %{libname}-designer
%{_qtdir}/plugins/designer/kcompletion6widgets.so
